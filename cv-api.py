#/home/bocchrj/miniconda3/bin/python
# source activate dev01

"""cv-api.py: Curriculum Vitae (CV) API"""

# Generic/Built-in
import json, configparser
from flask import Flask, jsonify, make_response, g
from flask_httpauth import HTTPTokenAuth

# Owned
__author__ = 'Rich Bocchinfuso'
__copyright__ = 'Copyright 2020, CV API'
__credits__ = ['Rich Bocchinfuso']
__license__ = 'MIT'
__version__ = '0.1.0'
__maintainer__ = 'Rich Bocchinfuso'
__email__ = 'rbocchinfuso@gmail.com'
__status__ = 'Dev'

# read and parse config file
config = configparser.ConfigParser()
config.read('config.ini')
config.sections()

app = Flask(__name__)
admin_auth = HTTPTokenAuth(scheme='Bearer')
subscriber_auth = HTTPTokenAuth(scheme='Bearer')

fmt = '%H:%M:%S' # ex. 20110104172008 -> Jan. 04, 2011 5:20:08pm 

admin_tokens = {
    config['auth']['admin_token'].encode('ascii') : "admin"
 }

subscriber_tokens = {
    config['auth']['subscriber_token'].encode('ascii') : "subscriber"
 }
 
@admin_auth.verify_token
def verify_token(token):
    if token in admin_tokens:
        g.current_user = admin_tokens[token]
        return True
    return False
    
@subscriber_auth.verify_token
def verify_token(token):
    if token in subscriber_tokens:
        g.current_user = subscriber_tokens[token]
        return True
    return False

@admin_auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 403)
    # return 403 instead of 401 to prevent browsers from displaying the default auth dialog

@subscriber_auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 403)
    # return 403 instead of 401 to prevent browsers from displaying the default auth dialog

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify({'error': 'Bad request'}), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

# load json data from cv.json
with open(config['local']['json_data']) as json_file:
    cv = json.load(json_file)

# api get
@app.route('/app/api/v1.0/cv', methods=['GET']) 
@subscriber_auth.login_required
def get_cv():
    return jsonify({'cv': [cv]})

# api get specific section
@app.route('/app/api/v1.0/cv/<section>', defaults={}, methods=['GET']) 
@subscriber_auth.login_required
def get_cvsection(section):
    return jsonify({section: [cv[section]]})

# a route to the loader.io token
@app.route("/loaderio-a1bf45ed67f8d31af6d5fc2616f65379/")
def index():
    return "loaderio-a1bf45ed67f8d31af6d5fc2616f65379"

if __name__ == '__main__':
    app.config['JSON_SORT_KEYS'] = False
    #app.run(debug=True,ssl_context='adhoc',host='0.0.0.0',port=80)
    app.run(debug=True, host='0.0.0.0', port=5000)
