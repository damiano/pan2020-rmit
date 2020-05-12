import pickle
import numpy as np
from pan.tweet_level.tweetPredictor import tweet_predictor as t_predictor

class user_predictor:
    def __init__(self):
        self.classifier = pickle.load(open('Data/classifier.txt','rb'))

    def pridict_user(self,set):
        
    
        result = self.classifier.predict(set)
        return result
    
