# Análise do mercado de trabalho de data science


## Objetivo

Este trabalho visa obter insights através dos dados de como está o mercado de Data Science e o que ele esta requerendo. A ideia a priori era obter insights a cerca de salários e skills demandadas ao redor do mundo. Com esse intuito preilimar coletou-se os dados das mais diversas fontes, tais como kaagle, glassdoor, h1bdata e medley. Os links de onde foram baixados os dataset podem ser encontrados abaixo e categorizados segundo uma inspeção preliminar:


<br/>


- *Salaries Around World* : O conjunto de dados nessa categoria envolve datasets com mesmo esquema. Eles possuem dados sobre o ano de coleta do dado, o tipo a modalidade empregatícia, salários na moeda local, salarios em dolar, proporção de tempo em regime remoto, onde fica sede da compania ,o tamanho da compania e finalmente o local de residência do empregado.


    - *AI/ML Salaries* : https://www.kaggle.com/datasets/cedricaubin/ai-ml-salaries 
    - *Data Science Jobs Analysis*: https://www.kaggle.com/datasets/niyalthakkar/data-science-jobs-analysis
    - *Data Jobs 2023*: https://www.kaggle.com/datasets/dinarkhan/data-jobs-2023 
    
    <br/>

 - Jobs Descriptions: Esse conjunto de dados foi coletado visando analisar quais são as skills que mais aparecem nas descrições de vagas de trabalho. Os dataset possuem squemas diferentes, mas ambos foram coletados com o intuito de  somente utilizar a coluna equivalente ao cargo de trabalho e a descrição:

    - *Data Scientist Jobs* - GlassDoor: https://www.kaggle.com/datasets/andrewmvd/data-scientist-jobs?datasetId=778775&sortBy=voteCount : Possui o cargo de trabalho ofertado na vaga, aonde a vaga foi postada, a compania que postou a vaga e a descrição do job. 
    
    <br/>

    - *2023 Data Scientists Job Descriptions* : https://www.kaggle.com/datasets/diegosilvadefrana/2023-data-scientists-jobs-descriptions :  Esse dataset é bem mais amplo, além de possuir o título do job e sua descrição ele possui o nome da companhia, seu lucro, sua avalição na plataforma glassdoor e o setor de atuação daquela companhia.  De fato poderia-se fazer fazer uma análise mais rica com esse dataset, mas por questões de escopo de projeto apenas utilizou-se as columnas relativas ao título do job, a descrição e o setor em que a companhia atua com a finalidade de obter um insight de qual setores estão mais empregando. 
    
    <br/>



- Jobs mapping Skills: Nessa categoria temos o mapeamento de habilidades por job, são listados ao todo  16 habilidades onde um empregado. Cada linha desse dataset equivale a um empregado num determinado posto, que respondeu sua posição em relação a aquela habilidade.

    - *IT Career Proficiency Dataset*: https://data.mendeley.com/datasets/kzt6h7pz97 
    
    <br/>
    

- H1Bdata: Esses dataset foi obtido a partir de uma adpatação de um script de  web scrapping em  "https://github.com/yiuhyuk/ds_salary_h1b/blob/master/h1b_salary.ipynb". O código adpatado pode ser encontrando na classe       ```H1bdataWebScrapper.py``` e sua implementação no script  ```h1bdata_web_scrapping.py``` ambos presensente nesse repositório. Nesse datasset temos  o nome da compania em que está o job, o título do job, o salário em dolar, a data de postagem, a cidade e o estado americano correspondente.

Uma análise dos dados fora feita com mais detalhes no arquivo `SprintI_counting_the_history.ipynb`, onde fora feita uma analise preliminar dos dados, o pré-processamento e a geração de insights,
nele contamos a história de como tudo ocorreu.


O projeto completo, com os bancos de dados e todos os arquivos utilizados pode ser encontrado no link abaixo, nele pode-se ter acesso tudo quanto for necessário para se reproduzir tudo que fora feito nesse projeto:

https://drive.google.com/drive/folders/1OIaWc-whIlm04W3WGfA9MUP4OAKg43EX?usp=share_link
