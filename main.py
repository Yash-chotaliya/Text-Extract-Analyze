from extract_article import extract_articles
from remove_stopwords import remove_stopwords
from create_dictionary import create_dictionary
from analyze_variables import analyze_variables
import pandas as pd
import json
import os

if __name__ == '__main__':
    
    df = pd.read_excel('Input.xlsx')

    URL_ID = df['URL_ID']
    URL = df['URL']
    
    # Extracting articles from the URL
    extract_articles(URL_ID, URL)
    print("Articles extracted\n")
    
    files = os.listdir('URL_Content')

    # Removing stopwords from the articles
    remove_stopwords(files=files)
    print("Stopwords removed\n")
    
    pos_words = []
    neg_words = []

    with open('MasterDictionary/positive-words.txt', 'r') as f:
        pos_words.extend(f.readlines())

    with open('MasterDictionary/negative-words.txt', 'r') as f:
        neg_words.extend(f.readlines())
    
    # create dictionary for positive and negative words
    create_dictionary(pos_words=pos_words, neg_words=neg_words)
    print("Dictionary created\n")
    
    dict = json.load(open('Dictionary.json','r'))

    cleaned_files = os.listdir('Cleaned_URL_Content/')
    
    # analyze variables from the cleaned files
    analyze_variables(cleaned_files=cleaned_files, dict=dict)
    print("Variables analyzed\n")
    
    print("Program completed")