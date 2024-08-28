import nltk
nltk.download('stopwords')
from nltk.tokenize import sent_tokenize,word_tokenize
import json
from nltk.corpus import stopwords
import os
import pandas as pd


def count_word(tokens):
    stop_words = stopwords.words('english')
    filtered_sentence = [w for w in tokens if ((not w.lower() in stop_words) and (w not in [',','?','.','!']))]
    return len(filtered_sentence)
    
def count_syllables(tokens):
    count = 0
    vowels = 'aeiou'
    
    for word in tokens:
        for char in word:
            if char in vowels:
                count += 1
        
        if word.endswith('es') or word.endswith('ed'):
            count -= 1
        
    return count

def personal_pronouns(tokens):
    count = 0
    for word in tokens:
        if word in ['i', 'we', 'my', 'ours', 'us']:
            count += 1
    return count

def count_char(tokens):
    count = 0
    for word in tokens:
        count += len(word)
    return count

def complex_word_count(tokens):
    count = 0
    vowels = 'aeiou'
    for word in tokens:
        x=0
        for char in word:
            if char in vowels:
                x += 1
        if x > 2:
            count += 1
            
    return count

def store_in_excel(file, file_analysis):
    df = pd.read_excel('Output Data Structure.xlsx')
    
    for key in file_analysis.keys():
        df.loc[int(file.split('.')[0][-3:])-1, key] = file_analysis[key]
    
    df.to_excel('Output Data Structure.xlsx', index=False)
    
def analyze_variables(cleaned_files, dict):
    
    for file in cleaned_files:

        with open('Cleaned_URL_Content/' + file,'r') as f:
            file_analysis = {}
            text = f.read()
            tokens = word_tokenize(text)
            sents = sent_tokenize(text)
            
            file_pos_words = []
            file_neg_words = []
            
            for token in tokens:
                if token in dict['pos_words']:
                    file_pos_words.append(token)
                if token in dict['neg_words']:
                    file_neg_words.append(token)
                    
            file_analysis['POSITIVE SCORE'] = len(file_pos_words)
            file_analysis['NEGATIVE SCORE'] = len(file_neg_words)
            file_analysis['POLARITY SCORE'] = (file_analysis['POSITIVE SCORE'] - file_analysis['NEGATIVE SCORE']) / ((file_analysis['POSITIVE SCORE'] + file_analysis['NEGATIVE SCORE']) + 0.000001)
            file_analysis['SUBJECTIVITY SCORE'] = (file_analysis['POSITIVE SCORE'] + file_analysis['NEGATIVE SCORE']) / ((len(tokens)) + 0.000001)
            file_analysis['AVG SENTENCE LENGTH'] = len(tokens) / (len(sents))
            file_analysis['WORD COUNT'] = count_word(tokens)
            file_analysis['SYLLABLE PER WORD'] = count_syllables(tokens) / len(tokens)
            
            file_analysis['PERSONAL PRONOUNS'] = personal_pronouns(tokens)
            
            file_analysis['AVG WORD LENGTH'] = count_char(tokens)/len(tokens)
            file_analysis['AVG NUMBER OF WORDS PER SENTENCE'] = file_analysis['AVG SENTENCE LENGTH']
            file_analysis['COMPLEX WORD COUNT'] = complex_word_count(tokens)
            file_analysis['PERCENTAGE OF COMPLEX WORDS'] = (file_analysis['COMPLEX WORD COUNT']*100) / len(tokens)
            file_analysis['FOG INDEX'] = 0.4 * (file_analysis['AVG SENTENCE LENGTH'] + file_analysis['PERCENTAGE OF COMPLEX WORDS'])
                        
            store_in_excel(file, file_analysis)

if __name__ == '__main__':
    
    dict = json.load(open('Dictionary.json','r'))

    cleaned_files = os.listdir('Cleaned_URL_Content/')
    
    # analyze variables from the cleaned files 
    analyze_variables(cleaned_files=cleaned_files, dict=dict)