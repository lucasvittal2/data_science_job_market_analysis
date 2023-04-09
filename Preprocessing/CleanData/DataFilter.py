from AbstractionClasses.Preprocessing.DataCleaner import DataCleaner
from pandas import DataFrame, concat
from scipy import stats
import numpy as np

class DataFilter(DataCleaner):
    
    
    
    def __init__(self, filter_by: str, col: str, category_col:str = "", by_value=None):
        self.by_value = by_value
        self.col = col
        self.filter_by = filter_by
        self.category_col = category_col
    
    
    def __filter_data_by_z_score(self, data: DataFrame):
        Z_THRESHOLD = 3 ## holds 99.78% of data regarding a normal distribution.
        col = self.col
        tmp_df = data.copy()
        z_score = np.abs( stats.zscore( tmp_df[col] ) )
        outlier_free = tmp_df[ (z_score.lt(Z_THRESHOLD) )]
        return outlier_free
    
    def __filter_data_by_value_list(self, data: DataFrame):
        
        col = self.col
        values = self.by_value
        filtered_data = data[ data[col].isin(values)]
        return  filtered_data
        
    
    def __filter_data_by_IQR(self, data: DataFrame):
        #filter by IRQ
        
        tmp_df = data.copy()
        col= self.col
        
        Q1 = tmp_df.quantile(0.25)
        Q3 = tmp_df.quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5*IQR
        upper_bound = Q3 + 1.5*IQR
        
        outlier_free = tmp_df[~( ( tmp_df.lt( lower_bound ) ) |( tmp_df.gt( upper_bound ) ) ).any(axis=1) ]
        
        return outlier_free
    
    def __eliminate_outliers(self, data: DataFrame):
        
        if self.filter_by == "FILTER_OUTLIERS_BY_Z_SCORE" or self.filter_by == "FILTER_OUTLIERS_CATEGORICALLY_Z_SCORE":
            filtered_data = self.__filter_data_by_z_score(data)
            
        elif self.filter_by == "FILTER_OUTLIERS_BY_IQR"  or self.filter_by == "FILTER_OUTLIERS_CATEGORICALLY_BY_IRQ":
            filtered_data = self.__filter_data_by_IQR(data)
        else:
            print("You have tryed to implent a non-available outilier elimination method")
            raise NotImplementedError("Outrilier Elimination Methoid not available !\n  \
                                       try to impleement one of following available methods : 'FILTER_OUTLIERS_BY_Z_SCORE' ,'FILTER_OUTLIERS_BY_IQR', 'FILTER_OUTLIERS_CATEGORICALLY_BY_IRQ' or 'FILTER_OUTLIERS_CATEGORICALLY_Z_SCORE'")
        return filtered_data
         
    def __eliminate_outliers_categorically(self, data: DataFrame):
        
        category_col = self.category_col
        filtered_df = DataFrame({}, columns = data.columns)

        for category in  data[category_col].unique():
            
            tmp_df =  data[  data[category_col] == category ] 
            tmp_df = self.__eliminate_outliers(tmp_df)
            filtered_df = concat([filtered_df, tmp_df], axis=0)
            
        
        return filtered_df

         
    def __filter_by_freq(self, data:  DataFrame):
        
        col = self.col
        by_value = self.by_value
        filter_by = self.filter_by
        tmp_df = data.copy()
        
        value_counts = DataFrame(tmp_df[col].value_counts()).reset_index()
        value_counts.columns = ['title', 'freq']
        
          
        options ={
            "FREQ_GREATER_THAN_VALUE" : value_counts[ value_counts['freq'] >  by_value]['title'],
            "FREQ_GREATER_OR_EQUAL_THAN_VALUE" :    value_counts[ value_counts['freq'] >=  by_value]['title'],
            "FREQ_EQUAL_VALUE" :  value_counts[ value_counts['freq'] ==  by_value]['title'],
            "FREQ_LOWER_THAN_VALUE" : value_counts[ value_counts['freq'] <  by_value]['title'],
            "FREQ_LOWER_OR_EQUAL_THAN_VALUE" : value_counts[ value_counts['freq'] <=  by_value]['title']
        }
        to_remove = options[filter_by]
        tmp_df = tmp_df[  ~tmp_df[col].isin(to_remove)  ]
        
        
        return tmp_df
        
    def __filter_by_value(self,data : DataFrame):
        col = self.col
        value= self.by_value
        
        tmp_data = data.copy()
        tmp_data[col] = tmp_data[col].str.strip()
        
        if value == None and "FILTER_OUTLIERS" not in self.filter_by:
            raise ValueError("Value used in filtration not Defined! Define some value !")
        
        
        if self.filter_by == "FILTER_NOT_EQUAL_VALUE":
            filtered_data =  tmp_data[ tmp_data[col] ==  value ]
        
        elif self.filter_by == "FILTER_EQUAL_VALUE":
            filtered_data =  tmp_data[ tmp_data[col] !=  value ]
            
        elif self.filter_by == "FILTER_GREATER_THAN_VALUE":
            filtered_data =  tmp_data[ tmp_data[col] <  value ]
            
        elif self.filter_by == "FILTER_GREATER_OR_EQUAL_THAN_VALUE":
            filtered_data =  tmp_data[ tmp_data[col] <=  value ]
            
        elif self.filter_by == "FILTER_LOWER_THAN_VALUE":
                filtered_data =  tmp_data[ tmp_data[col] >  value ]
            
        elif self.filter_by == "FILTER_LOWER_OR_EQUAL_THAN_VALUE":
            filtered_data =  tmp_data[ tmp_data[col] >=  value ]
            
        else:
            print("ERROR NOT IMPLEMENTED!")
            raise NotImplementedError("Value Filtration Method not implemented!\n \
                try the available methods : 'FILTER_NOT_EQUAL_VALUE', 'FILTER_EQUAL_VALUE' ,'FILTER_GREATER_THAN_VALUE', 'FILTER_GREATER_OR_EQUAL_THAN_VALUE', 'FILTER_LOWER_THAN_VALUE', 'FILTER_LOWER_OR_EQUAL_THAN_VALUE' ")

        
        return filtered_data
    def clean_data(self, data):
        
        print("Performing Data Filtering... ")
        
        if "FILTER_OUTLIERS_CATEGORICALLY" in self.filter_by:
            filtered_data = self.__eliminate_outliers_categorically(data)
        
        elif "FILTER_OUTLIERS" in self.filter_by:
            filtered_data = self.__eliminate_outliers(data)
            
        elif "FREQ" in self.filter_by:
            filtered_data = self.__filter_by_freq(data)
            
        elif  self.filter_by in ["FILTER_NOT_EQUAL_VALUE", "FILTER_EQUAL_VALUE", "FILTER_GREATER_THAN_VALUE","FILTER_GREATER_OR_EQUAL_THAN_VALUE","FILTER_LOWER_THAN_VALUE", "FILTER_LOWER_OR_EQUAL_THAN_VALUE"]:
            
            filtered_data = self.__filter_by_value(data)
        elif self.filter_by == "FILTER_BY_VALUES":
            filtered_data = self.__filter_data_by_value_list(data)
        
        print("Data Filtering DONE ! \n")    
            
        return filtered_data

    def process_data(self, data):
         return self.clean_data(data)