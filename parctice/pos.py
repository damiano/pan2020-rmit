import en_core_web_sm

nlp=en_core_web_sm.load()

doc =nlp("All is well that ends well.")

for word in doc:
    print(word.text,word.pos_)