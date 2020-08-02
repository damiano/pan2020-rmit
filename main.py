from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.pipeline import Pipeline
from data_generator import data_generator
from sklearn.metrics import confusion_matrix
from sklearn import metrics
import numpy as np 
import matplotlib.pyplot as pl
import pandas as pd
import pickle
from sklearn.svm import LinearSVC
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_classification


clf = make_pipeline(StandardScaler(),
                   LinearSVC(random_state=0, tol=1e-5,max_iter=4000)
                  )
#classifier = RandomForestClassifier(n_estimators=100)
# clf =LogisticRegression()

def get_train_and_test(j):
    sets = []
    for i in range(0,10):
        data =data_generator(('csvs/3rd/user%s.csv' %i))  
        data_set = data.get_set()
        sets.append(data_set)
    test = sets.pop(j)
        
    train = pd.concat(sets)
    return train,test

def get_all():
    sets = []
    for i in range(0,10):
        data =data_generator(('csvs/3rd/user%s.csv' %i))  
        data_set = data.get_set()
        sets.append(data_set)     
        train = pd.concat(sets)
    return train

def assemble(columns,s):
    c = s
    media = c+'_median'
    std = c+'_std'
    columns.append(c)
    columns.append(media)
    columns.append(std)
    return columns
        
def classification():
    columns = ['median_score','mean_score','score_std','median_compound','mean_compound','compound_std','emoji','hash',
               'hash_median','hash_std','url','url_median','url_std']
    columns =assemble(columns,'trump')
    print(columns)
    accuracy = 0
    precision =0
    recall = 0 
    predict_set = []
    test_set = []
    for i in range(0,10):
        train_data,test_data = get_train_and_test(i)
        x_train = pd.DataFrame(train_data, columns=columns).values
        y_train = train_data['label']
        x_test = pd.DataFrame(test_data, columns=columns).values
        y_test = test_data['label']
        clf.fit(x_train,y_train)
        predicted = clf.predict(x_test)  
        predict_set.extend(predicted)
        test_set.extend(y_test)
        
        accuracy+=metrics.accuracy_score(y_test,predicted)
        precision+=metrics.precision_score(y_test,predicted)
        recall+=metrics.recall_score(y_test,predicted)
    print(accuracy*10,precision*10,recall*10) 
    print(predict_set) 
    print(test_set) 
    matrix = confusion_matrix(test_set, predict_set)
    print(matrix)
    return matrix 

def make_model():
    sets = []
    columns = ['median_score','mean_score','score_std','median_compound','mean_compound','compound_std','emoji','hash',
            'hash_median','hash_std','url','url_median','url_std']
    columns =assemble(columns,'trump')
    print(columns)
    accuracy = 0
    precision =0
    recall = 0 
    predict_set = []
    test_set = []
    
    train_data = get_all()
    x_train = pd.DataFrame(train_data, columns=columns).values
    y_train = train_data['label']
  
    clf.fit(x_train,y_train)
    
    pickle.dump(clf,open('classifier.txt', 'wb'))   
        
def classify(name):
    df_tweet = data_generator(name).get_set()
    x = df_tweet['score'].tolist()
    X = np.array(x).reshape(-1,1)
    ylabels =df_tweet['Label']
    print(X)
    kf = KFold(n_splits=10, random_state=None, shuffle=False)
    accuracy = 0
    precision =0
    recall = 0 
    predict_set = []
    test_set = []
    for train_index, test_index in kf.split(X):
        X_train,X_test = X[train_index],X[test_index]
        y_train,y_test= ylabels[train_index],ylabels[test_index]
        classifier.fit(X_train,y_train)
        predicted = classifier.predict(X_test)  
        predict_set.extend(predicted)
        test_set.extend(y_test)
        
        accuracy+=metrics.accuracy_score(y_test,predicted)
        precision+=metrics.precision_score(y_test,predicted)
        recall+=metrics.recall_score(y_test,predicted)
    print(accuracy,precision,recall) 
    print(predict_set) 
    print(test_set) 
    matrix = confusion_matrix(test_set, predict_set)
    return matrix 
if __name__ == "__main__":
    #make_model()
    # matrixs = classify("datas/mean.csv")
    # print(matrixs)
    # pl.matshow(matrixs)
    # pl.title('Confusion matrix of the classifier')
    # pl.colorbar()
    # pl.xlabel('Predicted')
    # pl.ylabel('True')
    # pl.savefig('confusion.jpg')
    classification()