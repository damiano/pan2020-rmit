import spacy
from spacy import displacy
import en_core_web_sm
from IPython.display import display, HTML

nlp = en_core_web_sm.load()



post = nlp(u"""Wall Street braced for more carnage Monday, with the Dow Jones industrial average projected to shed more than 1,000 points at the open as investors were spooked by the Federal Reserve’s move to slash interest rates to nearly to zero to protect the economy against a coronavirus-fueled recession.""")

entities=[(i,i.label_,i.label) for i in post.ents]
print(entities)
displacy.serve(post,style="ent")
# sudo lsof -i:5000
#kill number
#html=displacy.render(post,style='ent',page=True)