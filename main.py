import os
import urllib
import json
import flask
from flask import request, make_response, jsonify, Flask
import requests
from datetime import datetime
response = requests.post('https://orderstatusapi-dot-organization-project-311520.uc.r.appspot.com/api/getOrderStatus',
                        data={
                            "orderId":31313}
                        )
s=(response.text)
s=(s[17:27])
p=datetime.strptime(s,'%Y-%M-%d')


app = Flask(__name__)


# default route
@app.route('/')
def index():
    return 'Hello World!'


# function for responses
def results():
    # build a request object
    req = request.get_json(force=True)
    # fetch action from json
    action = int(req.get('queryResult').get('parameters').get('number'))
    print(action)
    if action == 31313:
        # return a fulfillment response

        return {'fulfillmentText': 'your order' +" "+ str(action) + " " + 'will be shipped on'+" "+ str(p.strftime("%a,%d %b,%Y"))}
    else:
        return {'fulfillmentText': "Please provide a valid orderID"}


# create a route for webhook
@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    # return response
    return make_response(jsonify(results()))


# run the app
if __name__ == '__main__':
    app.run()
