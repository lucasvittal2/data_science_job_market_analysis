from AbstractionClasses.Preprocessing.DataTransformation import DataTransformation
from pandas import DataFrame

class DataReplacer(DataTransformation):
    
    task: str = ""
    map: dict = {}
    
    def __init__(self, task, map):
        self.task = task
        self.map = map    
        
    def __split_data(self, data):
        pass
    
    def __map_replace(self,data):
        pass
    
    def transform_data(self, data):
        
        if self.task == "splitting":
            transformed_data = self.split_data(data)
            
        elif self.task == "mapreplacing":
            transformed_data = self.__map_replace(data)
                
        else:
            transformed_data = None

        return transformed_data