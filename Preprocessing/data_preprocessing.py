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

h1bdata_pre_preprocessors = [ 
                     blank_lines_cleaner, comma_replacer, convert_salaries_to_float,filter_ds_jobs,\
                    covert_date_to_datetime, get_out_outliers_IQR, \
                    splitt_location_column, map_replace_states,filtering_unknown_state
    ]

preprocessing = PreProcessing( pre_processors= h1bdata_pre_preprocessors)
h1bdata_df = pd.read_csv(DATASET_PATH + 'H1bdata_Salaries_EUA/USA_data_science_jobs_h1bdata.csv')
h1bdata_preprocessed =  preprocessing.process_data(h1bdata_df)


print("H1BdataDB Preprocessing Completed Sucessfully.")
"""

"""#Simplifying job roles on kaggle dataset

map = dict(pd.read_csv(DATASET_PATH + "Jobs_descriptions_EUA/job_role_mapping/mapa_job_roles_kaggle.csv" , delimiter=';')[['Original','Simplyfied']].values)
map = {k.upper(): v.upper() for k,v in  map.items()}


simplify_job_role_on_glassdorr_db = DataReplacer(task="MAPREPLACING", on_col="title", map=map)


# Eliminate useless titles

useless_title_eliminator = DataFilter(filter_by="FREQ_LOWER_THAN_VALUE", col='title', by_value= 2)


#preprocessing kaggle dataset

print("Iniciating Pre-Processing on job_description_kaggle\n")
job_description_kaggle_df = pd.read_csv(DATASET_PATH + 'Jobs_descriptions_EUA/2023-data-scientists-jobs-descriptions.csv')
job_description_kaggle_preprocessors = [ simplify_job_role_on_glassdorr_db, useless_title_eliminator ]
job_description_kaggle_preprocessing =  PreProcessing( pre_processors= job_description_kaggle_preprocessors)
job_description_kaggle_preprocessed =  job_description_kaggle_preprocessing.process_data(job_description_kaggle_df)
print("job_description_kaggle Preprocessing Completed Sucessfully.")


# Replace if contains
jobs =  ["DATA SCIENTIST","DATA ENGINEER","DATA ANALYST","DATA ARCHITECT","BI ANALYST","BUSINESS ANALYST","STATISTICIAN", "DATA ANALYTICS","DATA SPECIALIST", "DATA SCIENCE","DATA ANALYSIS","ANALYST", "ANALYTICS","DATA MANAGEMENT SPECIALIST","BUSINESS ANALYSIS", "MACHINE LEARNING ENGINEER", "RESEARCH","SOFTWARE ENGINEER","MACHINE LEARNING SCIENTIST","ASSOCIATE SCIENTIST", "DATA MODELER"]
glassdoor_job_replace_if_contains = DataReplacer(task="IFCONTAINSREPLACNING", on_col= 'Job Title', values= jobs)


#Simplifying titles on glassdoor database
map = {
    "BUSINESS ANALYSIS": "DATA ANALYST",
     "DATA ANALYTICS": "DATA ANALYST",
     "DATA ANALYSIS": "DATA ANALYST",
     "DATA SCIENCE" : "DATA SCIENTIST",
     "ANALYST": "DATA ANALYST",
     "DATA MANAGEMENT SPECIALIST": "DATA SPECIALIST",
     "ANALYTICS":"DATA ANALYST",
     "RESEARCH": "RESEARCHER",
     "MACHINE LEARNING SCIENTIST": "RESEARCHER",
     "DATA ENGINEER I": "DATA ENGINEER",
     "DATA ENGINEER II": "DATA ENGINEER",
     "DATA ENGINEER III": "DATA ENGINEER",
     "DATA ANALYST I":"DATA ANALYST",
     "DATA ANALYST II":"DATA ANALYST",
     "DATA ANALYST III":"DATA ANALYST",
     "DATA ANALYST JUNIOR":"DATA ANALYST",
     "DATA ARCHITECT II": "DATA ARCHITECT",
     "DATA ARCHITECT I": "DATA ARCHITECT",
     "DATA ARCHITECT III": "DATA ARCHITECT",
     "MARKETING DATA ANALYST": "DATA ANALYST",
     "DATA ENGINEER (REMOTE)": "DATA ENGINEER",
     "CLOUD DATA ENGINEER": "DATA ENGINEER",
     "SR. DATA ENGINEER": "DATA ENGINEER",
     "BUSINESS DATA ANALYST	": "DATA ANALYST",
     "SR. DATA ANALYST": "DATA ANALYST",
     "SENIOR MACHINE LEARNING ENGINEER": "MACHINE LEARNING ENGINEER",
     "DATA SCIENTIST (REMOTE)": "DATA SCIENTIST",
     "DATA SCIENTIST I": "DATA SCIENTIST",
     "DATA SCIENTIST II": "DATA SCIENTIST",
     "DATA SCIENTIST III": "DATA SCIENTIST",
     "AWS DATA ENGINEER":"DATA ENGINEER",
     "AZURE DATA ENGINEER":"DATA ENGINEER",
     "DATA SCIENCE ENGINEER":"DATA SCIENTIST",
     "MACHINE LEARNING ENGINEER (IMAGING)": "MACHINE LEARNING ENGINEER",
     "MACHINE LEARNING SCIENTIST":"RESEARCHER"

}


glassdoor_job_title_simplifier = DataReplacer(task='MAPREPLACING', on_col = 'Job Title', map=map)


#eliminate unfrequent values

glassdoor_unfrequent_title_elimination = DataFilter(filter_by = "FREQ_LOWER_THAN_VALUE", col='Job Title', by_value= 108)




#glassdoor preprocessing
print("Iniciating Pre-Processing on job_description_kaggle\n")
job_description_glassdoor_df = pd.read_csv(DATASET_PATH + "Jobs_descriptions_EUA/DataScientist_glassdoor.csv")
job_description_glassdoor_preprocessors = [ glassdoor_job_replace_if_contains, glassdoor_job_title_simplifier, glassdoor_unfrequent_title_elimination ]
job_description_kaggle_preprocessing =  PreProcessing( pre_processors= job_description_glassdoor_preprocessors)
job_description_kaggle_preprocessed =  job_description_kaggle_preprocessing.process_data(job_description_glassdoor_df)
print("job_description_kaggle Preprocessing Completed Sucessfully.")



#save files
print("Saving Files on test folder...")
#h1bdata_preprocessed.to_csv(TEST_PATH + "H1BDATA_preprocessed_data.csv")
job_description_kaggle_preprocessed.replace(-1, 'unknown', inplace=True)
job_description_kaggle_preprocessed.replace('-1', 'unknown', inplace=True)
job_description_kaggle_preprocessed.to_csv(TEST_PATH + "job_description_glassdoor_preprocessed.csv")
print("Files Saved !")

