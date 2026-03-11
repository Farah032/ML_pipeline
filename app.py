from flask import Flask 
from src.logger import logging
from src.exception import CustomException
import os, sys

#create object of flask class and pass the name of the module as argument
app = Flask(__name__)

#@app.route('/'): This is a Flask decorator that tells the application which URL should trigger the associated function. In this case, '/' refers to the main or home page of the website (e.g., http://127.0.0.1:5000/).
#GET: This method is used to retrieve data from the server. It appends data to the URL and is visible in the browser history, so it should not be used for sensitive information.
#POST: This method is used to send data to the server, often via a form submission, to create or update a resource.
@app.route('/', methods=['GET', 'POST'])

def index():
    try:
        raise Exception("We are testing our custom exception")
        
    except Exception as e:
        #logging.exception("Exception occurred")
        #abc = CustomException(e, sys)
        #logging.error(abc.error_message)

        abc = CustomException(e, sys)
        logging.error(abc.error_message)
        return "Welcome to ML pipeline"

if __name__ == "__main__":
   # app.run(debug=True)
    app.run(debug=True, use_reloader=False)

