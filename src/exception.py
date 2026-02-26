import os, sys
from src.logger import logging

def error_message_detail(error, error_detail:sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in script: [{0}] at line number: [{1}] error message: [{}]".format(file_name, exc_tb.tb_lineno, str(error))
    return error_message

   # line_number = exc_tb.tb_lineno
   
   # error_message = f"Error occurred in script: [{file_name}] at line number: [{line_number}] error message: [{str(error)}]"
   # return error_message


class CustomException(Exception):
#contructor of the class which will take error message and error details as input
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message
    

    if __name__ == "__main__":
        try:
            a = 1/0
        except Exception as e:
            logging.info("We are testing our custom exception")
            raise CustomException(e, sys)