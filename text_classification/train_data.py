from torchtext import data,datasets
import pandas as pd 


def final_data(fields):
    train_data= data.TabularDataset(
        path ='text_classification/data/train-test/en/final_train.csv',
        format='csv',
        fields =fields,
        skip_header = True
    ) 
    return train_data 

    

def create_all_csv():
    path = "text_classification/data/train-test/en/"
    
    indexs=[0,1,2,3,4,5,6,7,8,9]   
    frames=[]
    for i in indexs:
        filename =("fold%d.csv" %i)
        full_path = path+filename
        data = pd.read_csv(full_path) 
        frames.append(data)
    train = pd.concat(frames, ignore_index=True)    
    train.to_csv('text_classification/data/train-test/en/final_train.csv',index=False)

def get_traindata(fields,i):
    
    test_path = create_csv(i)
    train_data= data.TabularDataset(
        path ='text_classification/data/train-test/en/train.csv',
        format='csv',
        fields =fields,
        skip_header = True
    ) 
    
    test_data= data.TabularDataset(
        path =test_path,
        format='csv',
        fields =fields,
        skip_header = True
    )  
    return train_data,test_data

def create_csv(i):
    path = "text_classification/data/train-test/en/"
    
    indexs=[0,1,2,3,4,5,6,7,8,9]   
    index =indexs.pop(i)
    frames=[]
    for i in indexs:
        filename =("fold%d.csv" %i)
        full_path = path+filename
        data = pd.read_csv(full_path) 
        frames.append(data)
        
    filename = ("fold%d.csv" %index) 
    train = pd.concat(frames, ignore_index=True)
    test_path = path+filename
    train.to_csv('text_classification/data/train-test/en/train.csv',index=False)
    return test_path
  

create_all_csv()  
