from xml.etree.ElementTree import Element,ElementTree,tostring

def create_author(autor_id,language,author_type):
    author =Element('author', id =autor_id,lang =language, type= author_type)
    return author
    
    
def write_authors():
    author1=create_author("1","en","0")
    author2=create_author("2","en","0")

    with open('out.xml','a') as f:
        f.write(tostring(author2).decode("utf-8") + "\n")
        f.write(tostring(author1).decode("utf-8") +"\n" )
    
    
write_authors()    