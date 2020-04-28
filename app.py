# Using flask to make an api
# import necessary libraries and functions
import traceback
from logging.handlers import RotatingFileHandler
from time import strftime
from flask import Flask, jsonify, request
import socket
from waitress import serve
import logging

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
