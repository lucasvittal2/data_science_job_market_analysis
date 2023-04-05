from abc import abstractclassmethod
from AbstractionClasses.Preprocessing.PreProcessor import PreProcessor


class DataCleaner(PreProcessor):
    
    @abstractclassmethod
    def clean_data(self,data):
        pass