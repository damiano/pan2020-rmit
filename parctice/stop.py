from spacy.lang.en import English
import spacy

spacy_stopwords = spacy.lang.en.stop_words.STOP_WORDS
filtered_sent = []
nlp = English()
text = "The easiest way is to just interrupt it with the usual"

doc = nlp(text)

for word in doc:
    if word.is_stop==False:
        filtered_sent.append(word)
print(filtered_sent) 

print(list(spacy_stopwords)[:20])

