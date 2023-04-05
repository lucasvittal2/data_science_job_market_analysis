from AbstractionClasses.Preprocessing.DataCleaner import DataCleaner
from pandas import DataFrame

class MissingDataHandler(DataCleaner):
    
    def __init__(self, handling_by):
        self.handling_by = handling_by
    
    def __clean_blank_lines(self, data: DataFrame):
            
            return data.dropna(how='any')
            
        
    def __fill_missing_values(self, data):
        #fill missing values
        pass
    
    def clean_data(self, data):
        
        print("Performing missing values elimination... ")
        
        if self.handling_by == "CLEAN_BLANK_LINES":
            cleaned_data= self.__clean_blank_lines(data)
        elif self.handling_by == "FILL_MISSING_VALUES":
            cleaned_data = self.__fill_missing_values(data)
        else:
            raise NotImplementedError("Missing Handling method not implemented! \n \
                try available methods: 'CLEAN_BLANK_LINES', 'FILL_MISSING_VALUES' ")
        print("missing values elimination DONE !\n")
        return cleaned_data
    
    def process_data(self, data):
         return self.clean_data(data)