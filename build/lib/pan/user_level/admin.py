from .User import user
from .userLoader import loader
from .user_predictor import user_predictor
from .output import write_author
import os
from os import walk
class admin:
    def __init__(self,input_folder,output):
        self.input= input_folder
        self.output= output
        f = []
        for (dirpath, dirnames, filenames) in walk(input_folder):
            f.extend(filenames)
            break
        self.files =f
        self.user = user()
        self.predictor = user_predictor()
        self.l =loader()
        
    def write_file(self,filename):
        
        user_id=filename.split(".")[0]
        self.user.set_name(user_id, self.l.read_single(self.input + '/' +filename))
        arr = self.user.tweet_sentiment()
        result = self.predictor.pridict_user(arr)
        write_author(self.user.name, 'en', str(result[0]), self.output + '/' + 'en')
        
    def create_folder(self):
        directories = ['en', 'es']
        parent_dir = self.output  
        for directory in directories:
            path = os.path.join(parent_dir, directory) 
            os.mkdir(path) 
            print("Directory '% s' created" % directory) 
            
    def start(self):
        self.create_folder()
        i = 0
        for file in self.files:
            print('%d/300' %i)
            self.write_file(file)  
            i = i+1      
            