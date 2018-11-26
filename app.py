"""
Starts Recommender Web Server
"""

from flask import Flask
from flask import Flask, abort, request, render_template
from flask import Response
import logging
import glob


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
    sports = [i.replace('.png', "").capitalize().replace("_", " ") for i in user_images]
    data = list(zip(sports, user_images))
    return data


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/sport', methods=['GET'])
def sport():
    # Params for model are in here!
    args = request.args.to_dict()
    print(args)
    return render_template('sport.html', sport='Aeronautics!', user_image='aeronautics.png')

if __name__ == '__main__':
    app.run(debug=True)
