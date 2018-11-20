"""
Starts Recommender Web Server
"""

from flask import Flask
from flask import Flask, abort, request, render_template
from flask import Response
import logging


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
