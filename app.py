"""
Starts Recommender Web Server
"""

from flask import Flask
from flask import Flask, abort, request, render_template
from flask import Response
import logging
import glob
import inflection


app = Flask(__name__)

def get_image_data():
    """
    This function is designed to get all the possible images and their names that
    the model will be able to show via the sports template. The model will can use
    this function to search for the image and its corresponding sport name in order to
    display it to the user.


    Returns:
    <list> [(sport, user_image)...]
    """
    #mac
    #user_images = [i.replace('static/img/', "") for i in glob.glob('static/img/*.png')]
    #pc
    #user_images = [i.replace('static\\img\\', "") for i in glob.glob('static\\img\\*.png')]
    user_images = [i.replace('static/img/', "") for i in glob.glob('static/img/*.png')]
    sports = [inflection.titleize(i.replace('.png', "").capitalize().replace("_", " ")) + "!" for i in user_images]
    data = list(zip(sports, user_images))
    return data


def fetch_template_params_for(sport_name="aeronautics"):
    """
    Gets the template parameters that should be used for the /sport route.

    Parameter
    ---------
    sport_name: <string> The name of the specific sport. The default value is
    aeronautics

    Returns
    ---------
    <tuple> (sport, user_image)
    """
    data = get_image_data()
    postfix = '.png'
    try:
        item = list(filter(lambda x: sport_name + postfix in x, data))[0]
    except IndexError:
        print("No Sport Found by that name. Returning the default sport.")
        item = list(filter(lambda x: "aeronautics" + postfix in x, data))[0]
    return item


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/sport', methods=['GET'])
def sport():
    # Params for model are in here!
    args = request.args.to_dict()

    import numpy as np
    from sklearn.externals import joblib

    #replace these with our input parameters
    Age = float(args['age'])
    Height = float(args['height'])
    Weight = float(args['weight'])
    Sex= args['sex']
    Season = args['olympic_game']

    BMI = Weight/((Height/100)*(Height/100))

    Age_mean = 26.11
    Age_std = 5.487983

    Height_mean = 175.853000
    Height_std = 10.858561

    Weight_mean = 71.470500
    Weight_std = 15.815916

    BMI_mean = 22.890782
    BMI_std = 3.288332

    normalized_Age = (Age - Age_mean)/Age_std
    normalized_Height = (Height - Height_mean)/Height_std
    normalized_Weight = (Weight - Weight_mean)/Weight_std
    normalized_BMI = (BMI - BMI_mean)/BMI_std

    if (Sex=="Male") or (Sex=="male") :
        normalized_Sex0= -0.92110197
        normalized_Sex1=  0.92110197
    else:
        normalized_Sex0= 1.08565613
        normalized_Sex1= -1.08565613

    if (Season=="Summer") or (Season=="summer"):
        normalized_Season0= -0.61742649
        normalized_Season1=  0.61742649
    else:
        normalized_Season0= 1.61962601
        normalized_Season1= -1.61962601

    # Make the array
    #Year of 0 for the mean year
    #hard-code US population proportion of 0.69322825 which is the normalized value for US
    #hard-code COUNTRY-USA as 4.01173492 which is the normalized value for US
    my_array = np.array([normalized_Age,  normalized_Height,  normalized_Weight, 0,  normalized_BMI, 0.69322825,
    4.01173492,  normalized_Season0, normalized_Season1, normalized_Sex0,  normalized_Sex1])

    rf_jl = joblib.load("rf_finalized.joblib")
    le_jl = joblib.load("le.joblib")

    sport_code = rf_jl.predict(my_array.reshape(-1, 11))
    sport_name=le_jl.inverse_transform(sport_code[0])
    sport_name=sport_name.lower().replace(" ", "_")

    #Can just pass the name of the sport to get image and sport name.
    sport, image = fetch_template_params_for(sport_name)

    return render_template('sport.html', sport=sport, user_image=image)

if __name__ == '__main__':
    app.run(debug=True)
