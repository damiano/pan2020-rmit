import spacy
import pandas as pd

nlp =spacy.load('en')

doc1 = nlp("tired")
doc2 = nlp("bored")

print(doc1.similarity(doc2))


ex1 = nlp("wolf dog cat bird fish")

mylist = [(token1.text,token2.text,token1.similarity(token2)) for token1 in ex1 for token2 in ex1]

df = pd.DataFrame(mylist)

print(df)