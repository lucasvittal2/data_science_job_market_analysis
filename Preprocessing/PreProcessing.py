from typing import List
from pandas import DataFrame
from AbstractionClasses.Preprocessing.PreProcessor import PreProcessor
from AbstractionClasses.Preprocessing.DataCleaner import DataCleaner
from AbstractionClasses.Preprocessing.DataTransformation import DataTransformation

class PreProcessing(PreProcessor):
    
    def __init__(self, pre_processors: List[PreProcessor]):
        
        self.pre_processors = pre_processors
    
    
    def process_data(self, data: DataFrame):
        
        tmp_df = data.copy()
       
        for preprocessor in self.pre_processors:
            
            if isinstance( preprocessor, DataCleaner):
                preprocessed_data = preprocessor.clean_data(tmp_df)    
                
            elif isinstance (preprocessor, DataTransformation):
                preprocessed_data =  preprocessor.transform_data(tmp_df)
       
            ## Carry preprocessed data to the next step
            tmp_df = preprocessed_data
        return tmp_df