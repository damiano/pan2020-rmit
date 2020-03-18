import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
from sklearn.base import TransformerMixin
from sklearn.pipeline import Pipeline

df_amazon = pd.read_csv("dataset/amazon_alexa.tsv",sep="\t")

#print(df_amazon.head())
#print(df_amazon.info())
print(df_amazon.feedback.value_counts())
