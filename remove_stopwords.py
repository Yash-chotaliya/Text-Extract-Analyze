import os

def remove_all_files(files):
    for file in files:
        os.remove('Cleaned_URL_Content/' + file)

def remove_stopwords(files):
    
    if os.path.exists('Cleaned_URL_Content'):
        remove_all_files(files=os.listdir('Cleaned_URL_Content'))
    else:
        os.mkdir('Cleaned_URL_Content')
    
    for file in files:
        with open('URL_Content/' + file, 'r') as f:
            lines = f.readlines()[1:]
            text = ' '.join(lines)
            text = text.lower().strip()

        stopword_dir_ls = os.listdir('StopWords')

        stopWords = []

        for i in stopword_dir_ls:
            with open('StopWords/' + i, 'r') as f:
                stopWords.extend(f.read().splitlines())

        for i in range(len(stopWords)):
            stopWords[i] = stopWords[i].split('|')[0].lower().strip()

        for word in stopWords:
            text = text.replace(f" {word} ", ' ')
            
        with open(f"Cleaned_URL_Content/{file}", 'w') as f:
            f.write(text)
                            
if __name__ == "__main__":
    
    files = os.listdir('URL_Content')
    
    # Removing stopwords from the articles
    remove_stopwords(files=files)