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
    print(args)
    #Can just pass the name of the sport to get image and sport name.
    sport, image = fetch_template_params_for("default")
    return render_template('sport.html', sport=sport, user_image=image)

if __name__ == '__main__':
    app.run(debug=True)
