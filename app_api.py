##############################################################################
# Project         : NTT ASSIGNMENT
# Title           : app_api.py
# Description     : This file implements various resources|endpoints for
#                   interface details
# Author          : ANIL GOUD CHERUKU
# Date            : 31-Oct-2020
# Version         : 1.0.0
# Python_version  : 3.6.3
##############################################################################

# Importing all packages required for this script
import os
from logger_creation import setup_logger
from flask import Blueprint, jsonify, make_response, render_template
from flask import abort
from flask_restful import Api, Resource
import logging
import random
import datetime
import get_interfaces


# Have to append a random number to the filename so that the 2 uWSGI worker
# processes do not overwrite each others logs
dt_today = str(datetime.date.today())
rnd_num = str(random.randint(1000, 10000))
rnd_num = 1
log_file = 'NTTGN_AUTOMATION_' + dt_today + '_' + str(rnd_num) + '.log'
LOG_FILENAME = os.path.join('.', log_file)
# initial set up of logger file format for the entire container
setup_logger(LOG_FILENAME)
logger = logging.getLogger(__name__)

app_api = Blueprint('app_api', 'app_api', url_prefix='/NTTGN')


api = Api(app_api)


class InterfaceListAPI(Resource):
    """
    Inherits the Resource class and defines what needs to be done for each
    HTTP PROTOCOL method
    """

    def get(self):

        result = get_interfaces.retrieve_interfaces_from_source()

        response = make_response(jsonify(result), 200)

        return response

    def put(self):
        abort(405)

    def delete(self):
        abort(405)

    def post(self):
        abort(405)


class InterfaceAPI(Resource):
    def get(self, interface):
        result = get_interfaces.retrieve_interface_by_name(interface)
        if result is None:
            abort(404)
        response = make_response(jsonify(result), 200)

        return response

    def put(self, interface):
        abort(405)

    def delete(self, interface):
        abort(405)

    def post(self, interface):
        abort(405)


# add the required resources to the REST API instance
api.add_resource(InterfaceListAPI, '/Interfaces', endpoint='Interfaces_list')
api.add_resource(InterfaceAPI, '/Interfaces/<path:interface>',
                 endpoint='Interface')
