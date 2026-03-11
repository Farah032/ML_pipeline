import os, sys
from src.logger import logging



def error_message_detailed(error, error_detailed:sys):
    #exc_info() returns a tuple containing information about the exception that is currently being handled. The tuple contains three elements: the exception type, the exception value, and the traceback object.
    _, _, exc_tb = error_detailed.exc_info()

    file_name = exc_tb.tb_frame.f_code.co_filename

    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )

    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detailed:sys):
        super().__init__(error_message)
        self.error_message = error_message_detailed(error_message, error_detailed = error_detailed)

    def __str__(self):
        return self.error_message
    

if __name__ =="__main__":
    try:
        pass
        #a = 1 / 0

    except Exception as e:
        logging.info("Divison by Zero")
        raise CustomException(e,sys)