import spacy
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from text_classification.predictors import predictors
from text_classification.spacytokenizer import spacy_tokenizer
from text_classification.dataset_creator import get_pandas
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.metrics import confusion_matrix

df_amazon = get_pandas()
#bow_vector = CountVectorizer(tokenizer = spacy_tokenizer, ngram_range=(1,1))  
tfid_vector = TfidfVectorizer(tokenizer = spacy_tokenizer)  
#tokenizer
#tf_id

X = df_amazon['twitters']
ylabels =df_amazon['truth']

kf = KFold(n_splits=10, random_state=None, shuffle=False)

#X_train, X_test, y_train, y_test = train_test_split(X, ylabels, test_size=0.1,shuffle=False)

classifier = LogisticRegression()
#
pipe = Pipeline([("cleaner", predictors()),
                ('vectorizer',tfid_vector),
                ('classifier', classifier)])

for train_index, test_index in kf.split(X):
    X_train,X_test = X[train_index],X[test_index]
    y_train,y_test= ylabels[train_index],ylabels[test_index]
    pipe.fit(X_train,y_train)
    predicted = pipe.predict(X_test)
    print(confusion_matrix(y_test, predicted))
    print(metrics.accuracy_score(y_test,predicted))
    print(metrics.precision_score(y_test,predicted))
    print(metrics.recall_score(y_test,predicted))

# pipe.fit(X_train,y_train)

# predicted = pipe.predict(X_test)



# print(metrics.accuracy_score(y_test,predicted))
# print(metrics.precision_score(y_test,predicted))
# print(metrics.recall_score(y_test,predicted))


#what is ngram_range

# talking area user
# basic things 
# bert
# diversity of people and totic
#classification

#add other features
#refine the vectorizer
#repeat 10 times 10 fold validation

# basic analysis(how many twitters of 0,1)
# avaernumber of words in 

#output confusion matrix(how many each class is predicted)
#how many instaces, how many errors

#shuffle
#cross validation 
#ten fold validation 10pieces each of the loop 
#300 instaces 
#10-fold cross validation: 10 times 270 training, 30 test
#leave-one-out: 300 times, 299 training, 1 test
#extract the features

#function much more complicated
#try classifier

# exrat 
# weight the word
# a couple of the slides


#1.bert
#2.cross validation
#3.confusion matrix
#4.analysis
#5.vectorization, try tf-idf
#6.tf-idf combine with svm
#7.special features(find features)
#8.number of emojis