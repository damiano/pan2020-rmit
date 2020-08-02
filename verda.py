from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from data_generator import data_generator

analyzer = SentimentIntensityAnalyzer()

def add_compound(set):
    emotion_set = []
    for index, row in set.iterrows():
        vs = analyzer.polarity_scores(row['post'])
        emotion_set.append(vs['compound'])
    set['compound'] = emotion_set
    return set
        
if __name__ == "__main__":
    for i in range(0,10):
        data =data_generator(('datas/csvs/2nd/tweet%s.csv' %i))  
        set = data.get_set()
        set = add_compound(set)      
        set.to_csv(('datas/csvs/2nd/tweet%s.csv' %i), index = False)