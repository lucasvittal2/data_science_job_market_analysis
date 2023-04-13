from AbstractionClasses.Preprocessing.DataTransformation import DataTransformation
from pandas import DataFrame, to_datetime
import numpy as np



class DataTypeConversor(DataTransformation):
   
    #Only to datatime conversion
   
    
    def __init__(self, to_type, col, actual_date_format="", to_date_format=""):
        self.to_type=to_type
        self.col = col
        self.actual_date_format = actual_date_format
        self.to_date_format = to_date_format
    
    def __convert_data(self, data: DataFrame):
        
        col = self.col
        to_type = self.to_type
        to_date_format = self.to_date_format
        actual_date_format = self.actual_date_format
        tmp_df = data.copy()
        
        
        if to_type=="TO_DATETIME":
            
            tmp_df[col] = to_datetime( tmp_df[col], format= actual_date_format)
            tmp_df['date_str'] =  tmp_df[col].dt.strftime(to_date_format)
        
        elif to_type == "TO_FLOAT":
            tmp_df[col] = tmp_df[col].astype(np.float64)
            
        elif to_type == "TO_INT":
            tmp_df[col] = tmp_df[col].astype(np.int64)
        
        else:
            raise NotImplemented("This method is not avaible \
                Try some of available methods: 'TO_DATETIME', 'TO_FLOAT', 'TO_INT' ")
    
        return  tmp_df
    
    def transform_data(self,data):
        print("Perform Data conversion... ")
        transformed_data = self.__convert_data(data)
        print("Data conversion DONE !\n")
        return transformed_data
    
    def process_data(self, data):
         return self.transform_data(data)