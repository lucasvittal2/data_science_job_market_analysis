from AbstractionClasses.Preprocessing.DataTransformation import DataTransformation




class DataConversor(DataTransformation):
    
    def __init__(self, to_type, col):
        self.to_type=to_type
        self.col = col
    
    def __convert_data(self, data):
        #convert data
        pass
    def transform_data(self,data):
        transformed_data = self.__convert_data(data)
        return transformed_data