from AbstractionClasses.Preprocessing.DataCleaner import DataCleaner

class DataFilter(DataCleaner):
    
    by_value: any = None
    
    def __init__(self, filter_by, col, by_value):
        self.filter_by = filter_by
        self.col = col
    
    
    def __filter_data_by_z_score(self, data):
        Z_THRESHOLD = 3
        #filter by z-score
        pass
    
    def __filter_data_by_IQR(self, data):
        #filter by IRQ
        pass
    
    def __eliminate_outliers(self,data):
        
        if self.filter_by == "FILTER_OUTLIERS_BY_Z_SCORE":
            filtered_data = self.__filter_data_by_z_score(data)
        elif self.filter_by == "FILTER_OUTLIERS_BY_IQR":
            filtered_data = self.__filter_data_by_IQR(data)
        else:
            print("You have tryed to implent a non-available outilier elimination method")
            raise NotImplementedError("Outrilier Elimination Methoid not available !\n  \
                                       try to impleement one of following available methods : 'FILTER_OUTLIERS_BY_Z_SCORE' or 'FILTER_OUTLIERS_BY_IQR' ")
        return filtered_data
         
    def __filter_by_value(self,data):
        col = self.col
        value= self.by_value
        
        if value == None:
            raise ValueError("Value used in filtration not Defined! Define some value !")
        if self.filter_by == "FILTER_NOT_EQUAL_VALUE":
            filtered_data =  data[data[col] !=  value ]
        
        if self.filter_by == "FILTER_EQUAL_VALUE":
            filtered_data =  data[data[col] ==  value ]
            
        elif self.filter_by == "FILTER_GREATER_THAN_VALUE":
            filtered_data =  data[data[col] >  value ]
            
        elif self.filter_by == "FILTER_GREATER_OR_EQUAL_THAN_VALUE":
            filtered_data =  data[data[col] >=  value ]
            
        elif self.filter_by == "FILTER_LOWER_THAN_VALUE":
                filtered_data =  data[data[col] <  value ]
            
        elif self.filter_by == "FILTER_LOWER_OR_EQUAL_THAN_VALUE":
            filtered_data =  data[data[col] <=  value ]
        
        else:
            raise NotImplementedError("Value Filtration Method not implemented!\n \
                try the available methods : 'FILTER_NOT_EQUAL_VALUE', 'FILTER_EQUAL_VALUE' ,'FILTER_GREATER_THAN_VALUE', 'FILTER_GREATER_OR_EQUAL_THAN_VALUE', 'FILTER_LOWER_THAN_VALUE', 'FILTER_LOWER_OR_EQUAL_THAN_VALUE' ")
        
        return filtered_data
    def clean_data(self, data):
        
        if "FILTER_OUTLIERS" in self.filter_by:
            filtered_data = self.__eliminate_outliers(data)
        else:
            filtered_data = self.__filter_by_value(data)
            
        return filtered_data