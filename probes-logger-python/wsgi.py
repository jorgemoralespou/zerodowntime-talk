from __future__ import print_function

import os
import json

from flask import Flask, request
from flask_restful import Resource, Api


application = Flask(__name__)

api = Api(application)

class ReadyCheck(Resource):
    def get(self):
        return 'OK'

api.add_resource(ReadyCheck, '/ws/ready')

class LiveCheck(Resource):
    def get(self):
        return 'OK'

api.add_resource(LiveCheck, '/ws/live')
