from AbstractionClasses.Preprocessing.DataTransformation import DataTransformation

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re
import string
import nltk


class TextProcessor(DataTransformation):
    
    def __init__(self, col):
        self.col = col
    
    def __remove_patterns(self, input_txt, pattern):
        r = re.findall(pattern, input_txt)
        for word in r:
            input_txt = re.sub(word, "", input_txt)
        return input_txt
    
    def __remove_especial_characters(self, data):
        
        tmp_df = data.copy()
        col = self.col
        tmp_df[col] = tmp_df[col].str.replace("0\t", " ")
        tmp_df[col] = tmp_df[col].str.replace("\n", " ")
        tmp_df[col] = tmp_df[col].replace('[^\w\s]', " ", regex=True)
        tmp_df[col] = tmp_df[col].replace('[^a-zA-Z0-9]', ' ', regex=True)
        tmp_df[col] = tmp_df[col].str.replace("[^a-zA-Z#]", " ", regex=True)
        
        return tmp_df
        

    def __remove_stop_words(self, data):
        
        col = self.col
        
        tmp_df = data.copy()
        tmp_df[col] = tmp_df[col].apply(lambda x:' '.join([w for w in str(x).split() if len(w)>3]))
        return tmp_df
    
    def __tokenize_data(self,data):
        
        col = self.col
        tmp_df = data.copy()
        
        tokenized_description = tmp_df[col].apply(lambda x: x.split())
        tmp_df[col] =  tokenized_description
        return  tmp_df

    def __stem_words(self, tmp_df):
        stemmer = nltk.PorterStemmer()
        col = self.col
        
        tmp_df[col]  = tmp_df[col].apply(lambda sentence: [stemmer.stem(word) for word in sentence])
        return tmp_df

    
    def __convert_to_a_single_sentence(self, data ):
        
        col = self.col
        tmp_df  = data.copy()
        
        tokenized_description = tmp_df[col]
        
        
        
        for i in range( len( tokenized_description ) ) :
            tokenized_description[i] = " ".join( tokenized_description[i])
        
        tmp_df[col]  = tokenized_description          
        return tmp_df[col]
    

    
    def transform_data(self, data: pd.DataFrame):
        #remove patterns maybe
        col= self.col
        tmp_df = data.copy()
        print('Removing Especial Characters... ')
        especial_characters_free = self.__remove_especial_characters(tmp_df)
        print('Removing Stop Words... ')
        stop_words_free  = self.__remove_stop_words(especial_characters_free)
        print('Tokenizing Descriptions... ')
        tokenized_descriptions  = self.__tokenize_data(stop_words_free)
        print('Stemming Descriptions... ')
        stemmed_descriptions  = self.__stem_words(tokenized_descriptions)
        print('Converting all to a single setence')
        tmp_df[col]  = self.__convert_to_a_single_sentence(stemmed_descriptions)
        print('Processing is done!')
  
        
        return tmp_df
    
    def process_data(self, data):
         return self.transform_data(data)
    