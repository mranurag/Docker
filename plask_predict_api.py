# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 12:57:16 2019

@author: AnuragDubey
"""

from flask import Flask,request
from flasgger import Swagger
import pickle
import numpy as np
import pandas as pd
print("yes")

with open("./rf.pkl","rb") as model_pkl:
    model = pickle.load(model_pkl)

app= Flask(__name__)
swagger= Swagger(app)

@app.route("/predict")
def predict_iris():
    """ example endpoint returning prediction of iris
    ---
    parameters:
        - name: s_length
          in: query
          type: number
          required: true
        - name: s_width
          in: query
          type: number
          required: true
        - name: p_length
          in: query
          type: number
          required: true
        - name: p_width
          in: query
          type: number
          required: true
    """
          
    s_length = request.args.get("s_length")
    s_width = request.args.get("s_width")
    p_length = request.args.get("p_length")
    p_width = request.args.get("p_width")
    
    prediction = model.predict(np.array([[s_length,s_width,p_length,p_width]]))
    return str(prediction)


@app.route("/predict_file",methods=["POST"])
def predict_irisFile():
    """ example endpoint returning prediction of iris
    ---
    parameters:
        - name: input
          in: formData
          type: file
          required: true
    """
    
    input_data = pd.read_csv(request.files.get("input"),header=None)
    
    prediction = model.predict(input_data)
    return str(list(prediction))

if __name__=="__main__":
    app.run()
