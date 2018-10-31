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

# Read the scientific data on breast cancer survival,
# Build a LogisticRegression predictor on it
#read pickled data...
#patients = pd.read_csv("haberman.data", header=None)
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