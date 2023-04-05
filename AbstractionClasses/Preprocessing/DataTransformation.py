from abc import abstractclassmethod
from  AbstractionClasses.Preprocessing.PreProcessor import PreProcessor

class DataTransformation(PreProcessor):
    
    @abstractclassmethod
    def transform_data(self, data):
        pass
    