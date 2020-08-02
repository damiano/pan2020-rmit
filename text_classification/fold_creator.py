from text_classification.dataset_creator import get_users
import os

    
def create_folds():
    folds = []
    users = get_users();
    start = 0
    
    while(start<=270):
        temp_users = []
        for i in range(start,start+30):
            temp_users.append(users[i])
        folds.append(temp_users)
        start +=30
        
    return folds    

def create_folder():
    path = "data/train_test"    
    for i in range (0,10):
        folder = ("/fold%d" %i)
        fold_path = path+folder
        os.mkdir(fold_path)    
        
def test_folds():
    fold_name = "fold%s" 
    folds = create_folds()
    i = 0 
    for fold in folds:
        print((fold_name %i))       
        for user in fold:
            print(user[0],user[1])
        i+=1   
        
if __name__ == "__main__":
    create_folder()        