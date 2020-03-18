from sklearn.base import TransformerMixin

class predictors(TransformerMixin):
    def transform(self,X,**transform_params):
        return(clean_text(text) for text in X)

    def fit(self, X, y=None, **fit_params):
        return self    
    
    def get_params(self, deep=True):
        return {}    

def clean_text(text):
    # Removing spaces and converting text into lowercase
    return text.strip().lower()         

#Classifying text in positive and negative labels is called sentiment analysis.    