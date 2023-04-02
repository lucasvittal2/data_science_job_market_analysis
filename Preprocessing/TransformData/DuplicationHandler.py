from AbstractionClasses.Preprocessing.DataTransformation import DataTransformation


class DuplicationHandler(DataTransformation):
    
    
    def __init__(self, by_col):
        self.by_col = by_col
    
    def __eliminate_duplicates(self,data):
        #handling with duplication
        pass
    
    def transform_data(self, data):
        transformed_data = self.__eliminate_duplicates(data)
        return transformed_data