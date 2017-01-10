from __future__ import print_function

import os
import json

from flask import Flask, request
from flask_restful import Resource, Api

READYRET='OK'
LIVERET='OK'

application = Flask(__name__)

api = Api(application)

class ReadyCheck(Resource):
    def get(self):
        return READYRET

api.add_resource(ReadyCheck, '/ws/ready')

class LiveCheck(Resource):
    def get(self):
        return LIVERET

api.add_resource(LiveCheck, '/ws/live')


class ReadyUnset(Resource):
    global READYRET
    
    def get(self):
        READYRET='NOK'
        return 'OK'

api.add_resource(ReadyUnset, '/ws/readynot')

class LiveUnset(Resource):
    global LIVERET

    def get(self):
        LIVERET='NOK'
        return 'OK'

api.add_resource(LiveUnset, '/ws/livenot')
