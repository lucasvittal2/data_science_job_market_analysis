from AbstractionClasses.Preprocessing.DataTransformation import DataTransformation


class DuplicationHandler(DataTransformation):
    
    
    def __init__(self, by_col):
        self.by_col = by_col
    
    def __eliminate_duplicates(self,data):
        #handling with duplication
        pass
    
    def transform_data(self, data):
        print("Perform Deduplication Resolution...")
        transformed_data = self.__eliminate_duplicates(data)
        print("Deduplication Resolution DONE !\n")
        return transformed_data
    
    def process_data(self, data):
         return self.transform_data(data)