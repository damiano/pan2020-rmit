from xml.dom.minidom import parse
import xml.dom.minidom



def read_twitters(x):
    s=""""""
    DOMTree = parse("data/en/%s" % x)
    collection =DOMTree.documentElement
    documents = DOMTree.getElementsByTagName("document")
    for document in documents:
        s+=document.firstChild.wholeText
    return s    

s = read_twitters("0dwovd7nj6yg9m795ng2c629me0ccmrh.xml")  
print(s)      