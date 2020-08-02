import spacy

import spacy
nlp = spacy.load('/emotion')



tokens = nlp("I am a rat")
for token in tokens:
    print(token.text, token.has_vector, token.vector_norm, token.is_oov)