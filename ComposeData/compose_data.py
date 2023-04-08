#Even it works I doesn't looks weel, I would like to replace that for something more elegant.
import sys
sys.path.append("../")

from CsvReader import CsvReader
from Concatenator import Concatenator
from Env.ProjectPaths import DATASET_PATH


#Instantiate Classes

#Readers

csv_reader1 = CsvReader(file_path= DATASET_PATH + "Salaries_around_world/data_science jobs_salaries_world.csv")
csv_reader2 = CsvReader(file_path= DATASET_PATH + "Salaries_around_world/data_science_salaries_around_world.csv")
csv_reader3 = CsvReader(file_path= DATASET_PATH + "Salaries_around_world/ds.salaries.csv")
csv_reader4 = CsvReader(file_path= DATASET_PATH + "Salaries_around_world/salaries.csv")

#Concatenator

Concatenator = Concatenator()


#Load data

df_salaries_around_world1 = csv_reader1.load_data()
df_salaries_around_world2 = csv_reader2.load_data()
df_salaries_around_world3 = csv_reader3.load_data()
df_salaries_around_world4 = csv_reader4.load_data()


#Cocatenate

dfs_salaries_around_world = [df_salaries_around_world1, df_salaries_around_world2, df_salaries_around_world3, df_salaries_around_world4]
salaries_around_world = Concatenator.process_data(data=dfs_salaries_around_world)

#Save on to analyse Output

salaries_around_world.to_csv(DATASET_PATH + "Output_analyse/salaries_around_world.csv")
