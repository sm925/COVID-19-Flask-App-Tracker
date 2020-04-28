# Using flask to make an api
# import necessary libraries and functions
import traceback
from logging.handlers import RotatingFileHandler
from time import strftime
from flask import Flask, jsonify, request
import socket
from waitress import serve
import logging


# creating a flask app
app = Flask(__name__)


# expose a get endpoint 
@app.route('/hello_world', methods=['GET'])
def hello_world():
    return jsonify(response='Hello World!')

if __name__ == '__main__':
    app.run(debug=True)
