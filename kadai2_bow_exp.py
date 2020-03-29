from gensim import corpora,matutils
from gensim import models
import pandas as pd
import os

def bow(df):

    all_texts = []
    for line in df['description']:
        text = line.split(' ')
        all_texts.append(text)

    dictionary = corpora.Dictionary(all_texts)

    f = open('companies_bow1.csv', mode='w')
    f.write("index,company,category,training/test"+","*len(dictionary) + '\n')

    for index, company, category, traintest ,description in zip(df['index'],df['company'],df['category'],df['training/test'],all_texts):
        dense = list(matutils.corpus2dense([dictionary.doc2bow(description)], num_terms=len(dictionary)).T[0])
        f.write("{},{},{},{},".format(str(index),company,category,traintest))

        tmp = ""
        for i in dense:
            tmp += (str(i)+',')
        
        f.write(str(tmp[:-1])+'\n')
    f.close()
    
def main():
        df = pd.read_csv("companies_tokenized1.csv")
        bow(df)
if __name__ == "__main__":
    main()