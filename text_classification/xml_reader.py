from xml.dom.minidom import parse
import xml.dom.minidom
import pandas as pd
import csv

#read from xml and combine all the tweets together, then return a string

def get_documents(x):
    DOMTree = parse("text_classification/data/en/%s" % x)
    collection =DOMTree.documentElement
    documents = DOMTree.getElementsByTagName("document")
    return documents

def read_twitters(x):
    s=""""""
    documents = get_documents(x)
    for document in documents:
        s+=document.firstChild.wholeText
    return s    

def read_all(set,x,y):
    documents = get_documents(x)
    # with open('BERT_lib/tsv/twitter.tsv',"a",encoding="utf-8",newline='') as out_file:
    for document in documents:
        name = x.split('.')[0]
        set.append([name,document.firstChild.wholeText,y])
            
def read_single(x):
    set=[]
    documents =get_documents(x)
    for document in documents:
        set.append(document.firstChild.wholeText)
    return set;    
         
def clear_all():            
    open('BERT_lib/tsv/twitter.tsv', 'w').close()    