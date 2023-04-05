from AbstractionClasses.Preprocessing.DataTransformation import DataTransformation
from pandas import DataFrame

class DataSplitter(DataTransformation):
    
    
    def __init__(self, delimiter: str, old_col: str, new_col1: str, new_col2: str):
        self.delimiter = delimiter
        self.old_col = old_col
        self.new_col1 = new_col1
        self.new_col2 = new_col2
        
    def __split_data(self,data: DataFrame):
        
        delimiter = self.delimiter
        old_col = self.old_col
        new_col1 = self.new_col1
        new_col2 = self.new_col2
        
        tmp_df = data.copy()
        tmp_df[[new_col1, new_col2]] = tmp_df[old_col].str.split(delimiter, expand=True).iloc[:,:-2]
        tmp_df.drop(old_col, axis = 1, inplace=True)
        
        return tmp_df
        

    def transform_data(self, data: DataFrame):
        print("Performing Data splitting...")
        data_splited = self.__split_data(data)
        print("Data splitting DONE !\n")
        return data_splited
    
    def process_data(self, data):
         return self.transform_data(data)
    
        
        
