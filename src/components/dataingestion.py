import os, sys
import pandas as pd
import numpy as np
from src.logger import logging
from src.exception import CustomException
from dataclasses import dataclass
from sklearn.model_selection import train_test_split

#decorator: A decorator is a design pattern in Python that allows you to modify the behavior of a function or class. It is denoted by the "@" symbol followed by the name of the decorator function. In this case, @dataclass is a decorator that automatically generates special methods for the class, such as __
@dataclass
class DataIngestionConfig:
    train_data_path = os.path.join('artifacts', 'train.csv')
    test_data_path = os.path.join('artifacts', 'test.csv')
    raw_data_path = os.path.join('artifacts', 'raw.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
        
    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion started")
        try:
            logging.info("Data reading using panda library using local system")
            data = pd.read_csv(os.path.join('notebook/data', 'income_cleandata.csv'))
            logging.info("Data read successfully as dataframe")

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)
            data.to_csv(self.ingestion_config.raw_data_path,index=False)
            
            logging.info("Train test split data")

            train_set, test_set = train_test_split(data, test_size= .30, random_state=42)
            #saving data to csv file
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            
            logging.info("Data ingestion completed successfully")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            logging.info("Error occured in data ingestion stage")
            raise CustomException(e, sys)
        

if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()


#/Users/farahjabeen/Desktop/Project-Thesis/ML_pipeline/src/components/dataingestion.py
#/Users/farahjabeen/Desktop/Project-Thesis/ML_pipeline/noteboook/data/income_cleandata.csv