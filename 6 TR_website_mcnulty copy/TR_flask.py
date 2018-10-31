from flask import Flask, jsonify, render_template, request


import flask
from sklearn.linear_model import LogisticRegression
import numpy as np
import pandas as pd
import json
import sys


# Initialize the app
app = flask.Flask(__name__)


#---------- MODEL IN MEMORY ----------------#
import pickle

# Read the scientific data on breast cancer survival,
# Build a LogisticRegression predictor on it
#read pickled data...
#patients = pd.read_csv("haberman.data", header=None)
pkl_filename = "./pickles/pickle_model_10_29_2_41.pkl"

with open(pkl_filename, 'rb') as file:  
    pickle_model = pickle.load(file)

#print(pickle_model, file=sys.stderr)

#
#patients.columns=['age','year','nodes','survived']
#patients=patients.replace(2,0)  # The value 2 means death in 5 years, update to more common 0
#
##select best columns
##fit data
#X = patients[['age','year','nodes']]
#Y = patients['survived']
#PREDICTOR = LogisticRegression().fit(X,Y)

#use the predictor to fit the incoming dict data




#---------- URLS AND WEB PAGES -------------#

# Homepage
@app.route("/")
def viz_page():
    """
    Homepage: serve our visualization page, awesome.html
    """
    with open("templates/index.html", 'r') as viz_file:
        return viz_file.read()


def convert_number_to_party(n):
    party =['Republican', 'Democrat', 'Independent', 'No Party']
    return party[n]

def make_output_string(prediction, proba):
	output = f'Random Forest predicts:\n{prediction}\n\nProbabilities:\n{"R":<5s}{proba[0][0]:>7.2f}\n{"D":<5s}{proba[0][1]:>7.2f}\n{"I":<5s}{proba[0][2]:>7.2f}\n{"N":<5s}{proba[0][3]:>7.2f}'
	return output

@app.route('/submission', methods=['POST'])
def submission():
    data = request.get_json('data')

    order = ["VCF0149",
    		 "VCF0851",
    		 "VCF0852",
    		 "VCF0853",
    		 "VCF9131",
    		 "VCF0879a",
    		 "VCF9039",
    		 "VCF9041",
    		 "VCF9016",
    		 "VCF9017",
    		 "VCF0894"]
    
    #determine if data is complete...
    poll_results=[]
    missing_data=[]
    for item in order:
    	try:
    		new_item = data[item]
    		poll_results.append(int(new_item))
    	except:
    		missing_data.append(item)	

    message = f'This is what python sees: {poll_results}'
    print(message, file=sys.stderr)

	#determine if data is complete...
    if len(poll_results) == len(order):
    	message = f'{[poll_results]}'
    else:
    	message = f'missing data for: {missing_data}'

    #use the data to predict outcome and return it
    prediction = pickle_model.predict([poll_results])
    proba = pickle_model.predict_proba([poll_results])
    answer = make_output_string(convert_number_to_party(prediction[0]), proba)

    return answer

#--------- RUN WEB APP SERVER ------------#

# Start the app server on port 80
# (The default website port)
app.run(host='0.0.0.0')
app.run(debug=True)