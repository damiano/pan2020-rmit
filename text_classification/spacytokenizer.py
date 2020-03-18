import string
from spacy.lang.en import STOP_WORDS
from spacy.lang.en import English
import spacy

punctuations = string.punctuation

nlp = spacy.load('en')
stop_word = spacy.lang.en.stop_words.STOP_WORDS
parser = English()

def spacy_tokenizer(sentence):
    mytokens = parser(sentence)
    mytokens = [word.lemma_.lower().strip() if word.lemma_ != "-PRON-" else word.lower_ for word in mytokens]
    mytokens = [word for word in mytokens if word not in stop_word and word not in punctuations]
    return mytokens