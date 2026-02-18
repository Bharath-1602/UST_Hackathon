from flask import Flask 
import os

app = Flask(__name__)
@app.route('/trigger')

def trigger():
    os.system("The port is Triggered")
    return "Triggered"

app.run(host="127.0.0.1",port=5000)

