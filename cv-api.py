#/home/bocchrj/miniconda3/bin/python
# source activate dev01
# CV RESTful API servvie
# Rich Bocchinfuso
# cv-api.py

import time, json, datetime, configparser
from flask import Flask, jsonify, abort, make_response, request, url_for, g
from flask_httpauth import HTTPTokenAuth

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

# print (admin_tokens)
# print (subscriber_tokens)
 
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
#     print json.dumps(cv)
#     print(str(datetime.datetime.now()) + ' | info |    ' + str(cvDetails))

# api get
@app.route('/app/api/v1.0/cv', methods=['GET']) 
@subscriber_auth.login_required
def get_cv():
    #     return jsonify(cv)
    return jsonify({'cv': [cv]})

# api get specific section
@app.route('/app/api/v1.0/cv/<section>', defaults={}, methods=['GET']) 
@subscriber_auth.login_required
def get_cvSection(section):
#     return jsonify(cv[section])
    return jsonify({section: [cv[section]]})

if __name__ == '__main__':
    app.config['JSON_SORT_KEYS'] = False
    #app.run(debug=True,ssl_context='adhoc',host='0.0.0.0',port=80)
    app.run(debug=True, host='0.0.0.0', port=5000)
