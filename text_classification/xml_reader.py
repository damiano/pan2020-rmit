from xml.dom.minidom import parse
import xml.dom.minidom

#read from xml and combine all the tweets together, then return a string

def read_twitters(x):
    s=""""""
    DOMTree = parse("data/en/%s" % x)
    collection =DOMTree.documentElement
    documents = DOMTree.getElementsByTagName("document")
    for document in documents:
        s+=document.firstChild.wholeText
    return s    

