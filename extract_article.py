import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
import os

def remove_all_files(files):
    for file in files:
        os.remove('URL_Content/' + file)


def extract_articles(URL_ID, URL):
    
    if os.path.exists('URL_Content'):
        remove_all_files(os.listdir('URL_Content'))
    else:
        os.mkdir('URL_Content')

    for i in range(len(URL)):
        r = requests.get(URL[i])
        soup = BeautifulSoup(r.content, features="lxml")
        
        if soup.find('h1') is not None:
            title = soup.find('h1').text
            
            text = soup.find('div', attrs={ 'class':'td-post-content' }).getText()
            text = re.sub('[^\w\n.]',' ', text)
            text = re.split('\n',text)
            text = "\n".join(text[0:len(text)-2])
            
            content = title+"\n\n"+text
            
            print(i+1)
            
            with open(f"URL_Content/{URL_ID[i]}.txt", 'w') as f:
                f.write(content)
                
if __name__ == "__main__":
    
    df = pd.read_excel('Input.xlsx')

    URL_ID = df['URL_ID']
    URL = df['URL']
    
    # Extracting articles from the URL
    extract_articles(URL_ID, URL)