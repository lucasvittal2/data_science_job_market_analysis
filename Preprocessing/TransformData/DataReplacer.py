from AbstractionClasses.Preprocessing.DataTransformation import DataTransformation
from pandas import DataFrame

from typing import List

class DataReplacer(DataTransformation):
    

    
    def __init__(self, task: str, on_col: str, this: any = "", by: any = "", map: dict={}, values: List[str] = []):
        

        self.task = task
        self.map = map
        self.on_col = on_col
        self.this = this
        self.by = by    
        self.values = values
        
    #This methods can implement simple replacing as well
    def __map_replace(self,data: DataFrame):
        
        on_col = self.on_col
        map = self.map
        map = {str(k).upper(): str(v).upper() for k,v in  map.items()}
        
        #Replace data on column
        tmp_df = data.copy()
        
        #str standadardization
        tmp_df[on_col] =  tmp_df[on_col].str.strip()
        tmp_df[on_col] =  tmp_df[on_col].str.upper()
        
        
        
        tmp_df[on_col] =  tmp_df[on_col].replace(map)
        
    
        return tmp_df
    def __replace_char(self, data: DataFrame):
        
        on_col = self.on_col
        this= self.this
        by = self.by
        
        
        tmp_df = data.copy()
       
        
        tmp_df [on_col] =  tmp_df[on_col].apply(lambda x: str(x).replace(this, by))
        

        return tmp_df
    
    def __replace_if_contains(self, data: DataFrame):
        
        tmp_df = data.copy()
        values = self.values
        on_col = self.on_col
        
        for val in values:
            tmp_df[on_col] = tmp_df[on_col].str.upper()
            tmp_df.loc[ tmp_df[on_col].str.contains(val), on_col] = val

        return tmp_df
        
    
    
    def transform_data(self, data: DataFrame):
        
        print("Performing Data Replacement... ")
            
        if self.task == "MAPREPLACING":
            transformed_data = self.__map_replace(data)
            
        elif self.task == "CHARREPLACING":
            transformed_data = self.__replace_char(data)
            
        elif self.task == "IFCONTAINSREPLACNING":
            transformed_data = self.__replace_if_contains(data)
                
        else:
            raise NotImplemented("This method is not avaible \
                Try some of available methods: 'MAPREPLACING', 'CHARREPLACING' ")
            
        print("Data Replacement DONE !\n")
        return transformed_data
    
    def process_data(self, data):
         return self.transform_data(data)