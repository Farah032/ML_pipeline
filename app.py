from flask import Flask 
from src.logger import logging
from src.exception import CustomException
import sys,os

#create object of flask class and pass the name of the module as argument
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])

def index():
    try:
        raise Exception("We are testing our custom exception")
        
    except Exception as e:
        abc = CustomException(e, sys)
        logging.info(abc.error_message)
        return "Welcome to ML pipeline"

if __name__ == "__main__":
    app.run(debug=True)