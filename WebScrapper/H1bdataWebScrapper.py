from bs4 import BeautifulSoup
import requests
import pandas as pd




class H1bdataWebScrapper():
    def __get_dataWithExeceptionHandler(self, whole_data, index):
        tmp_lst=[]
        for i in whole_data:
                try:
                    tmp_lst.append(i[index])
                except IndexError:
                    tmp_lst.append("null")
        return tmp_lst
    
    def __replace_spaces(self, jobs):
        return [ job.replace(" ","+") for job in jobs]
 
  
    def get_data(self, jobs) -> pd.DataFrame():
        formated_jobs = self.__replace_spaces(jobs)
        links = [f'https://h1bdata.info/index.php?em=&job={job}&city=&year=All+Years' for job in formated_jobs]
        
        # Scrape table data from each of the above links and store in a list
        jobs_list = []
        for (job,link) in zip(jobs, links):
            print(f"Retriving data for {job} jobs from h1bdata...")
            page_link = link
            page_response = requests.get(page_link, timeout=1000)
            page_content = BeautifulSoup(page_response.content, 'lxml')
        
            for row in page_content.find_all('tr')[1:]:
                row_data = []
                for i in row:
                    row_data.append(i.text)
                jobs_list.append(row_data)
            print(f"all data for {job} jobs retrieved successfully from h1bdata!")
        # Put everything into dataframes for easier processing
        ds_jobs_df = pd.DataFrame()
        ds_jobs_df['company'] = [i[0] for i in jobs_list]
        
        
        
        
        ds_jobs_df['title'] = self.__get_dataWithExeceptionHandler(jobs_list,1)
        
        ds_jobs_df['salary'] = self.__get_dataWithExeceptionHandler(jobs_list,2)
        #ds_jobs_df['salary'] = ds_jobs_df['salary'].astype(float)
        
        ds_jobs_df['location'] = self.__get_dataWithExeceptionHandler(jobs_list,3)
        
        ds_jobs_df['date'] = self.__get_dataWithExeceptionHandler(jobs_list,4)
        ds_jobs_df['date'] =  ds_jobs_df['date'] 
        
        return ds_jobs_df