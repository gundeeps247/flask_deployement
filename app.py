from flask import Flask
 
app = Flask(__name__)
 
@app.route('/')

def hello_world():
    return 'Hello Pie (from your Miraan a.k.a. Squishy)'