#Not elegant !!
import sys
sys.path.append("../")
import warnings

# Disable DeprecationWarning
warnings.filterwarnings("ignore", category=DeprecationWarning)


from TransformData.DataSplitter import DataSplitter
from TransformData.DataTypeConversor import DataTypeConversor
from TransformData.DataReplacer import DataReplacer


from CleanData.DataFilter import DataFilter
from CleanData.MissingDataHandler import MissingDataHandler

from PreProcessing import PreProcessing
from Env.Constants import DS_JOBS
from Env.ProjectPaths import *

import pandas as pd




#instantiating entities

print("Instantiating Preprocessor...\n")


blank_lines_cleaner = MissingDataHandler(handling_by = "CLEAN_BLANK_LINES")

#tretement on salaries
comma_replacer = DataReplacer(task = "CHARREPLACING", on_col = "salary", this_char = ",", by_char = "")
convert_salaries_to_float = DataTypeConversor(to_type='TO_FLOAT', col='salary')

#Filter the interesting jobs

filter_ds_jobs = DataFilter(filter_by="FILTER_BY_VALUES", col='title', by_value = DS_JOBS)

#Tretment on date
covert_date_to_datetime = DataTypeConversor(to_type='TO_DATETIME', col = 'date',actual_date_format="%m/%d/%Y", to_date_format = "%d/%m/%Y")




#get out outliers by IRQ
get_out_outliers_IQR =   DataFilter(filter_by = "FILTER_OUTLIERS_BY_IQR",col ='salary')

# Spliting  location column on city and state column
splitt_location_column = DataSplitter(delimiter = ',' , old_col = 'location', new_col1='city', new_col2='state')

#map Replace
map = {
    "DC 20006": "WA",
    "CA 95134": "CA",
    "WASHINGTON": "WA",
    "VT.": "VT"	,
    "TX 77002": "TX",
    "NJ 07642": "NJ",
    "IL 60654": "IL",
    "SHOREVIEW":"MN",
    "MINNEAPOLIS": "MN",
    "MO 63105":"MO",
    "SAN RAMON,":	"CA",
    "SAN RAMON": "CA",
    "5TH FL": "FL",
    "NEW YORK": "NY",
    'NY,': "NY",
    "ETS DRIVE": "unknown",
    '': "unknown",
    "D.C.":"WA",
    "D.C":"WA",
    "ATLANTA":"GA",
    "LONG ISLAND CITY": "NY"

}

map_replace_states = DataReplacer(task="MAPREPLACING", on_col='state', map = map)


#filtering unknow states 

filtering_unknown_state  = DataFilter(filter_by="FILTER_NOT_EQUAL_VALUE", by_value='unknown', col='state')

# let's go

print("Iniciating Pre-Processing on H1BdataDB\n")

pre_preprocessors = [ 
                     blank_lines_cleaner, comma_replacer, convert_salaries_to_float,filter_ds_jobs,\
                    covert_date_to_datetime, get_out_outliers_IQR, \
                    splitt_location_column, map_replace_states,filtering_unknown_state
    ]

preprocessing = PreProcessing( pre_processors= pre_preprocessors)
data = pd.read_csv(DATASET_PATH + 'H1bdata_Salaries_EUA/USA_data_science_jobs_h1bdata.csv')
h1bdata_preprocessed =  preprocessing.process_data(data)


print("H1BdataDB Preprocessing Completed Sucessfully.")

h1bdata_preprocessed.to_csv(TEST_PATH + "H1BDATA_preprocessed_data.csv")