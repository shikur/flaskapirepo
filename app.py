from flask import Flask

app = Flask(__name__)

@app.route('/') # home page
def homepage():
    return "hello, world"

app.run(port=5000)    
