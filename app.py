"""
Starts Recommender Web Server
"""

from flask import Flask
from flask import Flask, abort, request, render_template
from flask import Response
import logging


app = Flask(__name__)


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
