import spacy
import torch
import pickle
class tweet_predictor:
    def __init__(self):
        self.cuda = torch.device('cuda' if torch.cuda.is_available() else 'cpu')  
      
        self.model = torch.load('Data/final_model.pt', map_location=self.cuda)
        self.model.eval()
        self.vocab = pickle.load(open('Data/file.txt','rb'))
    def predict_sentiment(self,sentence):    
        nlp = spacy.load('en')
        tokenized = [tok.text for tok in nlp.tokenizer(sentence)]
        #tokenized = spacy_tokenizer(sentence)
        indexed = [self.vocab.stoi[t] for t in tokenized]
        length = [len(indexed)]
        tensor = torch.LongTensor(indexed).to(self.cuda)
        tensor = tensor.unsqueeze(1)
        length_tensor = torch.LongTensor(length)
        prediction = torch.sigmoid(self.model(tensor, length_tensor))
        return prediction.item()
