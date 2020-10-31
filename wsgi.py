##########################################################################
# Project         : NTT ASSIGNMENT
# Title           : wsgi.py
# Description     : module to call the flask application to start
# Author          : ANIL GOUD CHERUKU
# Date            : 30-Oct-2020
# Version         : 1.0.0
# Python_version  : 3.6.3
##########################################################################

# Importing all packages required for this script
from flaskapp import app as application

if __name__ == '__main__':
    application.run(debug=True)
