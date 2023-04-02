from AbstractionClasses.Preprocessing.DataTransformation import DataTransformation

class DataSplitter(DataTransformation):
    
    
    def __init__(self, delimiter: str, col: str):
        self.delimiter = delimiter
        self.col = col
        
    def __split_data(self,data):
        #split data
        pass

    def transform_data(self, data):
        data_splited = self.__split_data(data)
        return data_splited
    
        
        
