from xml_reader import read_twitters,read_all
import pandas as pd

def get_users():
    users=[]
    with open("text_classification/data/en/truth.txt") as file_in:
        for line in file_in:
            array = line.split(":::")
            user = array[0]
            truth =int(array[1][0])
            users.append([user,truth])
    return users     

def create_seprate_set():
    set = []    
    users = get_users()
    for user in users:
        read_all(set,user[0]+'.xml',user[1])
    return set

def assemble_pandas(dataset,column):
    dataSet = pd.DataFrame(dataset)
    dataSet.columns = column
    return dataSet

def get_combined_twitters():
    set = create_combined_set()
    columns = ['user','twitters','truth']
    dataSet = assemble_pandas(set,columns)
    return dataSet

def get_seprate():
    set = create_seprate_set()
    columns = ['user','twitters','truth']
    dataSet = assemble_pandas(set,columns)
    return dataSet

def create_combined_set(users):
    set=[]
    for user in users:
        posts= read_twitters(user[0]+".xml")           
        set.append([user[0],posts,user[1]])     
    return set