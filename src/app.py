import os
import json, socket
from flask import Flask
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
        "Project Name": "Flask Docker App"
    }
    return json.dumps(myOutput)

@app.route('/how are you')
def hello():
    return getMessage()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)