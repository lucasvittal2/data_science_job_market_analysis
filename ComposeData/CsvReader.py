import pandas as pd

class CsvReader():
    
    def __init__(self, file_path: str, file_name: str):
        
        self.file_path = file_path
        self.file_name = file_name
        
    def load_data(self) -> pd.DataFrame:
       
            return  pd.read_csv(self.file_path + self.file_name)