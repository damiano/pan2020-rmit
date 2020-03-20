import spacy
nlp =spacy.load('en')
doc = nlp(u"the man reading the news is very tall lavish green grass")
#stupid software!!!!!

for token in doc.noun_chunks:
    print(token.root.text)
    print(token.root.head.text)

#very tall lavish green grass
#is reading  these are head