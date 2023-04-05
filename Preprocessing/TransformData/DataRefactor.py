from AbstractionClasses.Preprocessing.DataTransformation import DataTransformation



class DataRefactor(DataTransformation):
    
    task: str = ""
    
    def __init__(self, task):
        self.task = task
        
    def __discretize_data(self, data):
        ## Do discretization on data
        pass
    
    def __encode_data(self, data):
        ## Do enconding on data
        pass
    
    def __agregate_data(self, data):
        # Do Aggregation on data
        pass
    
    def transform_data(self, data):
        
        print(" Performing Data Refactoring... ")
        
        if self.task == "DISCRETIZING":
            transformed_data = self.__discretize_data(data)
            
        elif self.task == "ENCODING":
             transformed_data = self.__encode_data(data)
             
        elif self.task == "AGGREGATING":
            transformed_data = self.__agregate_data(data)
        else:
            raise NotImplementedError("Data refactor not available! \n \
                try to impleement one of following available methods :'DISCRETIZING', 'ENCODING', 'AGGREGATING'")
        print("Data Refactoring DONE ! \n")
        return transformed_data
    
    def process_data(self, data):
         return self.transform_data(data)