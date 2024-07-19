#            ------------------------------
#                      Instructions
#            ------------------------------

# Set to current working directory
    # cd C:\Users\Ariel\Google Drive\Personal\Programming\MLMoney\Week 03 - Cybersecurity
# Run app on python
    # python hello.py
# Go to the url it specifies
    # http://127.0.0.1:5000/

# This is a flask web app which allows a user to call an API
# Request will have JSON file to test on ML Model
# Return prediction and probability
# Future versions will have Firebase and Stripe compatability

#            ------------------------------
#                Import Classes, Models
#            ------------------------------

from flask import Flask
import numpy as np
import pandas as pd
import sys

# File management
import json
from flask import request, jsonify
from sklearn.externals import joblib

# Model
MODEL_PATH = 'model.pkl' # The model is saved as a pickle file in the same working directory as this App
#from sklearn.decomposition import PCA
#from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)
app.config["DEBUG"] = True


#            ------------------------------
#                      Prediction
#            ------------------------------

# Home
@app.route('/')
def hello_world():
    return 'Hello, welcome to my credit model API!'

# API test
@app.route("/api/v0/test", methods=['GET']) # Requester will get this data
def info():
    return jsonify(User = 'Ariel Serravalle',
                    Description = 'Testing the API can receive and return JSON')

# Get the prediction
@app.route("/api/v0/predict", methods=['POST']) 
def predict_test():
    xobs = pd.DataFrame([request.json]) # Take the JSON the client uploads, convert to pandas
    loaded_model = joblib.load(MODEL_PATH) # Load the model

    pred = str(loaded_model.predict(xobs)[0]) # make a prediction on the dataframe
    prob = str(loaded_model.predict_proba(xobs)[0][1].round(3)) # Get probability of fraud

    return jsonify(prediction = pred,
                    probability = prob)

#            ------------------------------
#                      Firebase
#            ------------------------------

# Incomplete Firebase functionality to store user data
'''
from flask import Flask, request
from flask_firebase import FirebaseAuth
from flask_login import LoginManager, UserMixin, login_user, logout_user
from flask_sqlalchemy import SQLAlchemy

app.config.from_object(...)

db = SQLAlchemy(app)
auth = FirebaseAuth(app)
login_manager = LoginManager(app)

app.register_blueprint(auth.blueprint, url_prefix='/auth')

'''

#            ------------------------------
#                      Stripe
#            ------------------------------

# Incomplete Stripe functionality to allow payment

'''
import stripe

@app.route('/signup', methods = ['GET'])
def signup():
    # card_data is a json file defined in html
    card_data = request.json

    charge = stripe.Charge.create(
    amount=card_data.amount,
    currency=card_data.currency,
    customer=card_data.customer,
    description=card_data.description,
    metadata=card_data.id
    )
    new_order.charge_id = charge.id
    # store in our database

# Verify the charge_id before allowing API call

'''

app.run()
