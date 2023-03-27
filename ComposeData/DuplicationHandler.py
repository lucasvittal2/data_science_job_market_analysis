import pandas as pd

class DuplicationHandler():

    def __init__(self):
        pass
    
    def eliminate_duplicates(self, df: pd.DataFrame) -> pd.DataFrame:
        
        duplicated_rows = df.duplicated(keep='first')
        return df[ ~duplicated_rows ]