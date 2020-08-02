import pandas as pd
class data_generator:
    def __init__(self,file_name):
        self.file_name=file_name
    
    def get_set(self):
        set = pd.read_csv(self.file_name ,delimiter = ',')
        return set
       
        
if __name__ == "__main__": 
    
    for i in range(0,10):
        data =data_generator(('G:/semester3/research/rm/pan/pan2020-rmit/text_classification/data/emotionresults/%s.csv' %i))  
        set = data.get_set()  
    
        new_set=set.groupby('user').agg(
            median_score = pd.NamedAgg(column = 'fake_score', aggfunc='median'),
            mean_score = pd.NamedAgg(column = 'fake_score', aggfunc='mean'),
            score_std = pd.NamedAgg(column = 'fake_score', aggfunc='std'),
            label = pd.NamedAgg(column = 'truth', aggfunc='mean'),
            median_compound = pd.NamedAgg(column = 'emotion_score', aggfunc='median'),
            mean_compound = pd.NamedAgg(column = 'emotion_score', aggfunc='mean'),
            compound_std = pd.NamedAgg(column = 'emotion_score', aggfunc='std'),
            emoji = pd.NamedAgg(column = 'emoji', aggfunc='mean'),
            hash = pd.NamedAgg(column = 'hash',aggfunc = 'mean'),
            hash_median = pd.NamedAgg(column = 'hash',aggfunc = 'median'),
            hash_std = pd.NamedAgg(column = 'hash',aggfunc = 'std'),
            url = pd.NamedAgg(column = 'url',aggfunc = 'mean'),
            url_median = pd.NamedAgg(column = 'url',aggfunc = 'median'),
            url_std = pd.NamedAgg(column = 'url',aggfunc = 'std'),
            trump = pd.NamedAgg(column = 'trump',aggfunc = 'mean'),
            trump_median = pd.NamedAgg(column = 'trump',aggfunc = 'median'),
            trump_std = pd.NamedAgg(column = 'trump',aggfunc = 'std')
        ).reset_index()
        print(new_set)

        # new_set['emoji'] = new_set['emoji'].map(lambda x: 0 if (x < 0.1) else 1)
        new_set.to_csv(('csvs/3rd/user%s.csv' %i), index=False)