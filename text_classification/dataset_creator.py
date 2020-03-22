from text_classification.xml_reader import read_twitters
import pandas as pd

def create_dataset():
    set =[]
    with open("text_classification/data/en/truth.txt") as file_in:
        for line in file_in:
            array = line.split(":::")
            user = array[0]
            posts= read_twitters(user+".xml")
            truth =int(array[1][0])
            set.append([user,posts,truth])     
    return set
    
def get_pandas():
    set = create_dataset()
    dataSet = pd.DataFrame(set)
    dataSet.columns=['user','twitters','truth']
    return dataSet
