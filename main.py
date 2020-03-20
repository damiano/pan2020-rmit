import pandas as pd
import spacy
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from text_classification.predictors import predictors
from text_classification.spacytokenizer import spacy_tokenizer
from sklearn.linear_model import LogisticRegression
from sklearn import metrics

df_amazon = pd.read_csv("dataset/amazon_alexa.tsv",sep="\t")
bow_vector = CountVectorizer(tokenizer = spacy_tokenizer, ngram_range=(1,1))  
tfid_vector = TfidfVectorizer(tokenizer = spacy_tokenizer)  

X = df_amazon['verified_reviews']
ylabels =df_amazon['feedback']

X_train, X_test, y_train, y_test = train_test_split(X, ylabels, test_size=0.3)
#read the data
#cross validation 
#ten fold validation 10pieces each of the loop 
#300 instaces 
#10-fold cross validation: 10 times 270 training, 30 test
#leave-one-out: 300 times, 299 training, 1 test

classifier = LogisticRegression()

pipe = Pipeline([("cleaner", predictors()),
                ('vectorizer',bow_vector),
                ('classifier', classifier)])

pipe.fit(X_train,y_train)

predicted = pipe.predict(X_test)
print(metrics.accuracy_score(y_test,predicted))
print(metrics.precision_score(y_test,predicted))
print(metrics.recall_score(y_test,predicted))


#what is ngram_range

#a set of twitters
#put all the text together

#task
#read everything
#combine all the xml file

