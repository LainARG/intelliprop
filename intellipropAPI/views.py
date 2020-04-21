"""
Routes and views for the flask application.
"""

from datetime import datetime
from intellipropAPI import app
from flask import Flask, request, abort
from flask_restful import Api, Resource, render_template
from joblib import load
import numpy as nppip
from math import log, exp
from Parser import *

app = Flask(__name__)
api = Api(app)

model = load('basic_model.joblib')
mean = np.load('mean.npy')
std = np.load('std.npy')
s = np.load('lstd.npy')
m = np.load('lmean.npy')

app.config['DEFAULT_PARSERS'] = [
    'flask.ext.api.parsers.JSONParser'
]

class PredictPricing(Resource):
    def get(self):
        #Fails when body is empty
        requestJson = request.get_json(force=True)

        #Validate input JSON
        valid_input, message = validate(requestJson)        
        if not valid_input:
            return abort(400, message)

        #Store JSON values in numpy array
        parsed_json = parse(requestJson)

        #Add features
        input_features = add_features(parsed_json)
        #Normalize features
        input_features = np.divide(input_features - mean, std)

        #Predict
        prediction = model.predict(input_features.reshape(1, -1))
        #De-normalize features
        prediction = exp(s * prediction + m)
        
        margin = round(prediction*0.1/10000)*10000
        rounded_prediction = round(prediction/10000)*10000
        low = rounded_prediction - margin
        high= rounded_prediction + margin

        output = {'original_prediction': prediction,
                  'prediction': rounded_prediction,
                  'high': high,
                  'low': low}

        return output            

#Setup the Api resource routing here
#Route the URL to the resource
#TODO: error codes
api.add_resource(PredictPricing, '/')

app.run(host="0.0.0.0", port=4000)
