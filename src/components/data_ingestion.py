import os
import sys
from src.exception import CustomException
from src.logger import logging 
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig



'''
Is creating a config class with three attributes:

train_data_path: where the training data will be saved

test_data_path: where the testing data will be saved

raw_data_path: where the original raw data will be saved

All of them are stored inside a folder called artifacts/, which is usually used for saving outputs of various ML pipeline steps.

'''

@dataclass
class DataIngestionConfig: 
    train_data_path: str =os.path.join('artifacts',"train.csv")
    test_data_path: str =os.path.join('artifacts',"test.csv")
    raw_data_path: str =os.path.join('artifacts',"data.csv")

'''
Created a class called DataIngestion, and in its constructor (__init__), it instantiates the DataIngestionConfig.

This means:

“when someone creates a DataIngestion object, make sure to also create a DataIngestionConfig and store it as self.ingestion_config.”
'''

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        '''Starts logging the process for visibility and debugging.'''
        logging.info("Entered the data ingestion method or component")
        try:
            df=pd.read_csv('src/notebook/Data/stud.csv')
            logging.info('Read the dataset as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info('Train test split initiated')
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Inmgestion of the data iss completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path


            )


        except Exception as e:
            raise CustomException(e,sys)
        


if __name__=="__main__":
    obj=DataIngestion()

    train_data,test_data=obj.initiate_data_ingestion()

    data_transformation=DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)

    

