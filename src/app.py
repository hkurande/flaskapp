import os
import json, socket, traceback
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
import joblib
from flask import Flask, jsonify, request


# Load AI Model
lr = joblib.load('model.pkl')
model_columns = joblib.load('model_columns.pkl')

def convert2int(myList):
    myNewList = []
    for i in myList:
        myNewList.append(int(i))
    return myNewList

def getMessage():
    import random
    messages = ["I am one", "I am two", "I am three", "I am four", "I am five"]
    myNum = random.randint(0, len(messages)-1)
    myMessage = messages[myNum]
    # Get current hostname
    hostname = socket.gethostname()
    myMessage = "Message from host: " + hostname + ". " + myMessage
    return myMessage

app = Flask(__name__)

@app.route("/")
def main():
    myOutput = {
        "Owner": "Hemant Kurande",
        "Date": "September 5, 2019",
        "Project Name": "Flask Docker App",
        "Message": getMessage()
    }
    return json.dumps(myOutput)

@app.route('/getMessage')
def hello():
    return getMessage()

@app.route('/predict', methods = ['POST'])
def predict():
    if lr:
        try:
            json_ = request.json
            print(json.dumps(json_))
            #query_df = pd.DataFrame(json_)
            query = pd.get_dummies(pd.DataFrame(json_))
            query = query.reindex(columns=model_columns, fill_value=0)
            prediction = convert2int(list(lr.predict(query)))
            print(prediction)
            return jsonify({'prediction': prediction})
        except:
            return jsonify({'trace': traceback.format_exc()})
    else:
        print('Trained model does not exist')
        return ('Service not available')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8050)