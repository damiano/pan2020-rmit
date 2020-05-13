from xml.dom.minidom import parse


class loader:
   
        
    def get_documents(self,x):
        DOMTree = parse(x)
        collection =DOMTree.documentElement
        documents = DOMTree.getElementsByTagName("document")
        return documents

    def read_single(self,x):
        set=[]
        documents =self.get_documents(x)
        for document in documents:
            set.append(document.firstChild.wholeText)
        return set;    
    
    
