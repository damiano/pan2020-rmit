import torch
import random
import numpy as np
from transformers import BertTokenizer
from torchtext import data
from text_classification.train_data import *
from transformers import BertTokenizer, BertModel
from model.BERTModel import BERTModel
from output.train_model import *
import torch.optim as optim
import torch.nn as nn
from collections import defaultdict
import pandas as pd

bert = BertModel.from_pretrained('bert-base-uncased')
BATCH_SIZE = 128
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')  
max_input_length = tokenizer.max_model_input_sizes['bert-base-uncased']
init_token_idx = tokenizer.cls_token_id
eos_token_idx = tokenizer.sep_token_id
pad_token_idx = tokenizer.pad_token_id
unk_token_idx = tokenizer.unk_token_id

#model need
HIDDEN_DIM = 256
OUTPUT_DIM = 1
N_LAYERS = 2
BIDIRECTIONAL = True
DROPOUT = 0.25
device = torch.device('cpu')


def tokenize_and_cut(sentence):
    tokens = tokenizer.tokenize(sentence) 
    tokens = tokens[:max_input_length-2]
    return tokens
    
class Model_trainer:
    SEED = 1234
    random.seed(SEED)
    np.random.seed(SEED)
    torch.manual_seed(SEED)
    torch.backends.cudnn.deterministic = True
    TEXT = data.Field(batch_first = True,
                    use_vocab = False,
                    tokenize = tokenize_and_cut,
                    preprocessing = tokenizer.convert_tokens_to_ids,
                    init_token = init_token_idx,
                    eos_token = eos_token_idx,
                    pad_token = pad_token_idx,
                    unk_token = unk_token_idx)

    LABEL = data.LabelField(dtype = torch.float)
    fields = [(None, None),('text', TEXT),('label', LABEL)]
    
    def __init__(self):
        self.owner = 'xinhuan'
    
    def get_data(self,index):
        train_data,test_data = get_traindata(self.fields,index)
        print(tokenizer.convert_ids_to_tokens(vars(train_data.examples[6])['text']))
        train_data, valid_data = train_data.split(random_state = random.seed(self.SEED))
        device = torch.device('cpu')
        train_iterator, valid_iterator, test_iterator = data.BucketIterator.splits(
            (train_data, valid_data, test_data), 
            sort = False,
            batch_size = BATCH_SIZE, 
            device = device
            )
        self.LABEL.build_vocab(train_data)
        self.LABEL.vocab.stoi =defaultdict(None, {'0': 0, '1': 1})
        print(self.LABEL.vocab.stoi)
        return  train_iterator, valid_iterator, test_iterator
    
    def get_final_data(self):
        train_data = final_data(self.fields)
        print(tokenizer.convert_ids_to_tokens(vars(train_data.examples[6])['text']))
        train_data, valid_data = train_data.split(random_state = random.seed(self.SEED))
        train_iterator, valid_iterator = data.BucketIterator.splits(
            (train_data, valid_data), 
            sort = False,
            batch_size = BATCH_SIZE, 
            device = device
            )
        self.LABEL.build_vocab(train_data)
        self.LABEL.vocab.stoi =defaultdict(None, {'0': 0, '1': 1})
        print(self.LABEL.vocab.stoi)
        return  train_iterator, valid_iterator
    
    
    def train_model(self, model,i):
        train_iterator, valid_iterator, test_iterator = self.get_data(i)
        N_EPOCHS = 5

        best_valid_loss = float('inf')

        for epoch in range(N_EPOCHS):

            start_time = time.time()

            train_loss, train_acc = train(model, train_iterator, optimizer, criterion)
            valid_loss, valid_acc = evaluate(model, valid_iterator, criterion)
                
            end_time = time.time()
                
            epoch_mins, epoch_secs = epoch_time(start_time, end_time)
                
            if valid_loss < best_valid_loss:
                best_valid_loss = valid_loss
                torch.save(model.state_dict(), 'tut6-model.pt')
            print(f'Epoch: {epoch+1:02} | Epoch Time: {epoch_mins}m {epoch_secs}s')
            print(f'\tTrain Loss: {train_loss:.3f} | Train Acc: {train_acc*100:.2f}%')
            print(f'\t Val. Loss: {valid_loss:.3f} |  Val. Acc: {valid_acc*100:.2f}%')
        
        model.load_state_dict(torch.load('tut6-model.pt'))
        test_loss, test_acc = evaluate(model, test_iterator, criterion)
        print(f'Test Loss: {test_loss:.3f} | Test Acc: {test_acc*100:.2f}%')
        
    def train_final_model(self, model):
        train_iterator, valid_iterator = self.get_final_data()
        N_EPOCHS = 5

        best_valid_loss = float('inf')

        for epoch in range(N_EPOCHS):

            start_time = time.time()

            train_loss, train_acc = train(model, train_iterator, optimizer, criterion)
            valid_loss, valid_acc = evaluate(model, valid_iterator, criterion)
                
            end_time = time.time()
                
            epoch_mins, epoch_secs = epoch_time(start_time, end_time)
                
            if valid_loss < best_valid_loss:
                best_valid_loss = valid_loss
                torch.save(model.state_dict(), 'final-model.pt')
            print(f'Epoch: {epoch+1:02} | Epoch Time: {epoch_mins}m {epoch_secs}s')
            print(f'\tTrain Loss: {train_loss:.3f} | Train Acc: {train_acc*100:.2f}%')
            print(f'\t Val. Loss: {valid_loss:.3f} |  Val. Acc: {valid_acc*100:.2f}%')
           
        
    def predict_sentiment(self,model, tokenizer, sentence):
        model.eval()
        tokens = tokenizer.tokenize(sentence)
        tokens = tokens[:max_input_length-2]
        indexed = [init_token_idx] + tokenizer.convert_tokens_to_ids(tokens) + [eos_token_idx]
        tensor = torch.LongTensor(indexed).to(device)
        tensor = tensor.unsqueeze(0)
        prediction = torch.sigmoid(model(tensor))
        return prediction.item()    
        
        
    
    
if __name__ == "__main__":
    
    
    model = BERTModel(bert,
            HIDDEN_DIM,
            OUTPUT_DIM,
            N_LAYERS,
            BIDIRECTIONAL,
            DROPOUT)
    optimizer = optim.Adam(model.parameters())
    criterion = nn.BCEWithLogitsLoss()
    
    model = model.to(device)
    
    criterion = criterion.to(device)
    #test_file = path +filename
    model_trainer=Model_trainer()
    model_trainer.train_final_model(model)
        # dataframe = pd.read_csv(test_file) 
        # data_list = dataframe['twitters'].values.tolist()
        # model.load_state_dict(torch.load('tut6-model.pt'))
        # fake_score_list = []
        # for sentence in data_list:
        #     fake_score = model_trainer.predict_sentiment(model,tokenizer,sentence)
        #     fake_score_list.append(fake_score)
        # dataframe["fake_score"] = fake_score_list
        # dataframe.to_csv("text_classification/data/results/%d.csv" %i, index = False)    
    
 
    
      
        
        
    



  
