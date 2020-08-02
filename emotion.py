from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
analyzer = SentimentIntensityAnalyzer()
import spacy
from spacymoji import Emoji

nlp = spacy.load('en')
emoji = Emoji(nlp)
nlp.add_pipe(emoji, first=True)

nlp1 = spacy.load('en')

def add_compound(set):
    emotion_set = []
    for index, row in set.iterrows():
        vs = analyzer.polarity_scores(row['twitters'])
        emotion_set.append(vs['compound'])
    set['emotion_score'] = emotion_set
    return set

def add_emojis(frame):
    
    emojisite = []
    for index, row in frame.iterrows():
        num_of_emoji = 0
        post = row['twitters']
        try:
            tokens = nlp(post)
            for token in tokens:
                if token._.is_emoji:
                    num_of_emoji=num_of_emoji+1
            emojisite.append(num_of_emoji)        
        except ValueError:
            emojisite.append(num_of_emoji)
        
    frame["emoji"] = emojisite 
    return frame
            
def add_hashtag(frame):
    hash_list = []
    for index, row in frame.iterrows():
        num_of_tag = 0
        post = row['twitters'] 
        tokens = nlp1(post)
        for token in tokens:
            if token.text.lower() == 'hashtag':
                num_of_tag=num_of_tag+1
        hash_list.append(num_of_tag)    
    frame["hash"] = hash_list
    return frame     

def add_RT(frame):
    RT_list = []
    for index, row in frame.iterrows():
        num_of_tag = 0
        post = row['twitters'] 
        tokens = nlp1(post)
        for token in tokens:
            if token.text.lower() == 'rt':
                num_of_tag=num_of_tag+1
        RT_list.append(num_of_tag)    
    frame["RT"] = RT_list
    return frame     

def add_URL(frame):
    RT_list = []
    for index, row in frame.iterrows():
        num_of_tag = 0
        post = row['twitters'] 
        tokens = nlp1(post)
        for token in tokens:
            if token.text.lower() == 'url':
                num_of_tag=num_of_tag+1
        RT_list.append(num_of_tag)    
    frame["url"] = RT_list
    return frame    

def add_trump(frame):
    RT_list = []
    for index, row in frame.iterrows():
        num_of_tag = 0
        post = row['twitters'] 
        tokens = nlp1(post)
        for token in tokens:
            if token.text.lower() == 'trump':
                num_of_tag=num_of_tag+1
        RT_list.append(num_of_tag)    
    frame["trump"] = RT_list
    return frame    
            
    
if __name__ == "__main__":
    # sentence = 'RT #USER#: Danny Ings levels against his former club‼️  1️⃣5️⃣ PREM GOALS FOR THE SEASON! ⚽️   #HASHTAG# I #HASHTAG# #HASHTAG#   #URL#…'
    # tokens =nlp1(sentence)
    # for token in tokens:
    #     if token.text.lower() == 'hashtag':
    #         print('find one')
    for i in range(0,10):
        path = "text_classification/data/emotionresults/"
        emoji_path = "text_classification/data/emotionresults/"
        filename =("%d.csv" %i)
        test_file = path +filename
        dataframe = pd.read_csv(test_file) 
        emotionframe = add_trump(dataframe)
        emotionframe.to_csv(emoji_path+filename, index =False)