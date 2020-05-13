from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer as analyzer
from pan.tweet_level.tweetPredictor import tweet_predictor as predictor
import pandas as pd

class user:
    def __init__(self):
        self.name = None
        self.tweets= None
        self.emotion=None
        self.ana = analyzer()
        self.sentiment = None
        self.predict = predictor()
    
    def set_name(self, name,tweet_list):
        self.name =name
        self.tweets=tweet_list
        
    def add_emotion(self):
        emotion_list = []
        for tweet in self.tweets:
            vs = self.ana.polarity_scores(tweet)['compound']
            emotion_list.append(vs)  
        self.emotion = emotion_list
        
    
    def tweet_sentiment(self):
        self.add_emotion()
        sentiment_list=[]
        for tweet in self.tweets:
           tweet_level = self.predict.predict_sentiment(tweet)
           sentiment_list.append(tweet_level)
          
        print(sentiment_list)  
        print(self.emotion)
        
           
        sentiments = {'compound': sentiment_list,
                      'score': self.emotion,}
        
        df = pd.DataFrame(sentiments, columns = ['score','compound'], index=None)
        print(df)
        arr = [[df['score'].median(),df['score'].mean(),df['score'].std(),df['compound'].median(),df['compound'].mean(),df['compound'].std()]]
        return arr
         
        
       
        
        
        