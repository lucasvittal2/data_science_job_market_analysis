import os

os.chdir("C:/Users/lucas/Documents/Studying/Pos-graduacao - Ciencia de Dados e  Analytics/Sprints/sprint I - Analise de salarios cientista de dados/data_science_job_market_analysis/Code")

from WebScrapper.H1bdataWebScrapper import H1bdataWebScrapper
from Env.Constants import DATA_SCIENCE_JOBS

print("\nProcessing started!")
print("Retriving Jobs Data from H1bdata...")

scrapper = H1bdataWebScrapper()
 #carga full
dataset = scrapper.get_data(DATA_SCIENCE_JOBS)

print("Saving Data...")
dataset.to_csv("test_file.csv")
print("Data were saved!")
print("Processs Finished Successfully !")