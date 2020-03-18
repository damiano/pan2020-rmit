import spacy
from spacy import displacy
import en_core_web_sm
from IPython.display import display, HTML

nlp = en_core_web_sm.load()

docp = nlp (" In pursuit of a wall, President Trump ran into one.")


for chunk in docp.noun_chunks:
   print(chunk.text, chunk.root.text, chunk.root.dep_,
          chunk.root.head.text)

displacy.serve(docp,style="dep",port = 4999)          