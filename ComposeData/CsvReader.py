import pandas as pd

class CsvReader():
    
    def __init__(self, file_path: str, delimiter: str = ','):
        
        self.file_path = file_path
        self.delimiter = delimiter
        
    def load_data(self) -> pd.DataFrame:
       
            return  pd.read_csv( self.file_path, delimiter  = self.delimiter)