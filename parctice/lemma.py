#limma can change the word into the simplest form
from spacy.lang.en import English
from spacy.lemmatizer import Lemmatizer
from spacy.lookups import Lookups

nlp = English()
lookups = Lookups()
lookups.add_table("lemma_rules", {"noun": [["s", ""]]})
lemmatizer = Lemmatizer(lookups)

lem = nlp("run ruins computed runner")

for word in lem:
    print(word.text,lemmatizer(word.text,"NOUN"))
    print(word.lemma_)