# Data science job market analysis


## Objetivo

This work aims to obtain insights through the data of how the Data Science market is doing and what it is requiring. The a priori idea was to obtain insights about wages and skills demanded around the world. With this preliminary aim, data was collected from the most diverse sources, such as kaagle, glassdoor, h1bdata and medley. The links from which the datasets were downloaded can be found below and categorized according to a preliminary inspection:


<br/>


- *Salaries Around World* : The dataset in this category involves datasets with the same schema. They have data on the year of data collection, the type of employment modality, wages in local currency, wages in dollars, proportion of time in remote regime, where the company is headquartered, the size of the company and finally the place of residence of the employee.


    - *AI/ML Salaries* : https://www.kaggle.com/datasets/cedricaubin/ai-ml-salaries 
    - *Data Science Jobs Analysis*: https://www.kaggle.com/datasets/niyalthakkar/data-science-jobs-analysis
    - *Data Jobs 2023*: https://www.kaggle.com/datasets/dinarkhan/data-jobs-2023 
    
    <br/>

 - Jobs Descriptions: This dataset was collected in order to analyze which skills appear most in job descriptions. The dataset have different schemes, but both were collected with the intention of only using the column equivalent to the job position and the description:

    - *Data Scientist Jobs* - GlassDoor: https://www.kaggle.com/datasets/andrewmvd/data-scientist-jobs?datasetId=778775&sortBy=voteCount : t has the job position offered in the vacancy, where the vacancy was posted, the company that posted the vacancy and the job description. 
    
    <br/>

    - *2023 Data Scientists Job Descriptions* : https://www.kaggle.com/datasets/diegosilvadefrana/2023-data-scientists-jobs-descriptions :  This dataset is much broader, in addition to having the title of the job and its description, it has the name of the company, its profit, its evaluation on the glassdoor platform and the sector in which that company operates. In fact, a richer analysis could be carried out with this dataset, but for reasons of the scope of the project, we only used the columns related to the job title, the description and the sector in which the company operates in order to obtain a insight into which industries are employing the most. 
    
    <br/>



- Jobs mapping Skills: In this category we have the mapping of skills by job, a total of 16 skills are listed where an employee. Each row in this dataset is equivalent to an employee in a given position, who answered their position in relation to that skill.

    - *IT Career Proficiency Dataset*: https://data.mendeley.com/datasets/kzt6h7pz97 
    
    <br/>
    

- H1Bdata: This dataset was obtained from an adaptation of a web scrapping script at "https://github.com/yiuhyuk/ds_salary_h1b/blob/master/h1b_salary.ipynb". The adapted code can be found in the `H1bdataWebScrapper.py` class and its implementation in the `h1bdata_web_scrapping.py` script, both present in this repository. In this dataset we have the name of the company where the job is located, the title of the job, the salary in dollars, the posting date, the city and the corresponding US state.

An analysis of the data was done in more detail in the `SprintI_counting_the_history.ipynb` file, where a preliminary analysis of the data, pre-processing and generation of insights was carried out,
in it we tell the story of how it all happened.


The complete project, with the databases and all the files used can be found at the link below, where you can access everything necessary to reproduce everything that was done in this project:

https://drive.google.com/drive/folders/1OIaWc-whIlm04W3WGfA9MUP4OAKg43EX?usp=share_link
