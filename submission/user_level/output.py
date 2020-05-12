from xml.etree.ElementTree import Element,ElementTree,tostring

def write_author(author_id,language,author_type,path):
    author =Element('author', id =author_id,lang =language, type= author_type)
    
    with open(('%s/%s.xml' %(path,author_id)),'a') as f:
        f.write(tostring(author).decode("utf-8"))
    
    

    
