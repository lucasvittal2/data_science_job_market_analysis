from AbstractionClasses.Preprocessing.DataTransformation import DataTransformation
from pandas import DataFrame

class DataReplacer(DataTransformation):
    

    
    def __init__(self, task, on_col,this_char = "", by_char = "", map={}):
        

        self.task = task
        self.map = map
        self.on_col = on_col
        self.this_char = this_char
        self.by_char = by_char    
        
    #This methods can implement simple replacing as well
    def __map_replace(self,data: DataFrame):
        
        on_col = self.on_col
        map = self.map
        
        #Replace data on column
        tmp_df = data.copy()
        tmp_df[on_col] =  tmp_df[on_col].str.strip()
        tmp_df[on_col] =  tmp_df[on_col].replace(map)
        
    
        return tmp_df
    def __replace_char(self, data):
        
        on_col = self.on_col
        this_char= self.this_char
        by_char = self.by_char
        
        
        tmp_df = data.copy()
       
        
        tmp_df [on_col] =  tmp_df[on_col].apply(lambda x: str(x).replace(this_char, by_char))
        

        return tmp_df
    
    def transform_data(self, data: DataFrame):
        
        print("Performing Data Replacement... ")
            
        if self.task == "MAPREPLACING":
            transformed_data = self.__map_replace(data)
            
        elif self.task == "CHARREPLACING":
            transformed_data = self.__replace_char(data)
                
        else:
            raise NotImplemented("This method is not avaible \
                Try some of available methods: 'MAPREPLACING', 'CHARREPLACING' ")
            
        print("Data Replacement DONE !\n")
        return transformed_data
    
    def process_data(self, data):
         return self.transform_data(data)