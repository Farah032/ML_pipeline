from flask import Flask, render_template,request,json
from src.pipeline.prediction_pipeline import PredictionPipeline, CustomClass
'''
from src.logger import logging
from src.exception import CustomException
import os, sys
'''

#create object of flask class and pass the name of the module as argument
app = Flask(__name__)

#@app.route('/'): This is a Flask decorator that tells the application which URL should trigger the associated function. In this case, '/' refers to the main or home page of the website (e.g., http://127.0.0.1:5000/).
#GET: This method is used to retrieve data from the server. It appends data to the URL and is visible in the browser history, so it should not be used for sensitive information.
#POST: This method is used to send data to the server, often via a form submission, to create or update a resource.
@app.route('/', methods=['GET', 'POST'])

def prediction_data():
    if request.method == "GET":
        return render_template("home.html")
    else:
        data = CustomClass(
            age = int(request.form.get("age")),
            workclass = int(request.form.get("workclass")),
            education_num = int(request.form.get("education_num")),
            marital_status = int(request.form.get("marital_status")),
            occupation = int(request.form.get("occupation")),
            relationship = int(request.form.get("relationship")),
            race = int(request.form.get("race")),
            sex = int(request.form.get("sex")),
            capital_gain = int(request.form.get("capital_gain")),
            capital_loss = int(request.form.get("capital_loss")),
            hours_per_week = int(request.form.get("hours_per_week")),
            native_country = int(request.form.get("native_country"))
        )
        
        final_data = data.get_data_DataFrame()
        pipeline_prediction = PredictionPipeline()
        pred = pipeline_prediction.predict(final_data)
        result = pred

        #write condition for 0 and 1 according to problem statement
        if result == 0:
            return render_template("results.html", final_result = "your yearly income is less than and equal $50K:{}".format(result))
        elif result == 1:
            return render_template("results.html", final_result = "your yearly income is more than and equal $50K:{}".format(result))

if __name__ ==  "__main__":
    app.run(host = "0.0.0.0", debug = True)
            
'''
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
        '''

if __name__ == "__main__":
   # app.run(debug=True)
    app.run(debug=True, use_reloader=False)




