##########################################################################
# Project         : NTT ASSIGNMENT
# Title           : flaskapp.py
# Description     : This file implements various handlers for Flask
# Author          : ANIL GOUD CHERUKU
# Date            : 30-Oct-2020
# Version         : 1.0.0
# Python_version  : 3.6.3
##########################################################################

# Importing all packages required for this script
import logging
from flask import Flask, jsonify, render_template
from app_api import app_api

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
app.register_blueprint(app_api)
logger = logging.getLogger(__name__)


@app.route('/')
def index():
    """
    index handler.
    :return: returns index template
    """
    return render_template("index.html")


# send email to support
def handle_exception(e):
    logging.debug(e)


if __name__ == "__main__":
    app.run(threaded=True)
