import json

def create_dictionary(pos_words, neg_words):
    
    for i in range(len(pos_words)):
        pos_words[i] = pos_words[i].strip().lower()

    for i in range(len(neg_words)):
        neg_words[i] = neg_words[i].strip().lower()
        
    dict = {
        'pos_words':pos_words,
        'neg_words':neg_words
    }
        
    json.dump(dict, open('Dictionary.json','w'), indent=4)

if __name__=="__main__":
    
    pos_words = []
    neg_words = []

    with open('MasterDictionary/positive-words.txt', 'r') as f:
        pos_words.extend(f.readlines())

    with open('MasterDictionary/negative-words.txt', 'r') as f:
        neg_words.extend(f.readlines())
    
    # create dictionary for positive and negative words 
    create_dictionary(pos_words=pos_words, neg_words=neg_words)
    