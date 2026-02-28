from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_tranformation import DataTransformation
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.entity.config_entity import (TrainingPipelineConfig, DataIngestionConfig, 
                                                  DataValidationConfig, DataTransformationConfig)
from networksecurity.logging.logger import logging
import os
import sys

from networksecurity.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig

if __name__=='__main__':
    try:
        trainingpipelineconfig=TrainingPipelineConfig()
        dataingestionconfig=DataIngestionConfig(trainingpipelineconfig)
        data_ingestion=DataIngestion(dataingestionconfig)
        logging.info("Initiate the data ingestion")
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        logging.info("Data Initiation Completed")
        print(dataingestionartifact)

        data_validation_config = DataValidationConfig(trainingpipelineconfig)
        data_validation = DataValidation(dataingestionartifact, data_validation_config)
        logging.info("Initiate the Data validation")
        data_validation_artifact = data_validation.initiate_data_validation()
        logging.info("Data validation completed")
        print(data_validation_artifact)

        data_tranformation_config = DataTransformationConfig(trainingpipelineconfig)
        data_transformation = DataTransformation(data_transformation_config=data_tranformation_config,
                                                  data_validation_artifact=data_validation_artifact)
        logging.info("Initiate the Data Transformation")
        data_transformation_artifact = data_transformation.initiate_data_transformation()
        logging.info("Data Transformation compeltd")
        print(data_transformation_artifact)
        
        

    except Exception as e:
           raise NetworkSecurityException(e,sys)