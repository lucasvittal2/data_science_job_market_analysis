import pandas as pd
import numpy as np


from AbstractionClasses.Preprocessing.PreProcessor import PreProcessor
from ComposeData.DuplicationHandler import DuplicationHandler

class Concatenator(PreProcessor):
    
    def __init__(self):
        self.preprocessor_type =  "concatenator"

    
    def __concat_data(self,dfs): 
        
        return pd.concat(dfs).iloc[:,:-1]
    
    def process_data(self, data):
        
        concat_data = self.__concat_data(data)
        duplicates_free = DuplicationHandler().eliminate_duplicates(concat_data)
        return duplicates_free