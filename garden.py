import spacy
nlp = spacy.load('en_core_web_sm')

# List of garden path sentences
gardenpathSentences = ['The pineapple pizza from the ocean', 'John drinks car in red', 'Mary gave the child a Band-Aid.', 'That Jill is never here hurts.', 'The cotton clothing is made of grows in Mississippi.']

# Tokenize and NER
for sentence in gardenpathSentences:
    doc = nlp(sentence)
    # Tokenize each sentence
    print([token.orth_ for token in doc])
    # Perform Named Entity Recognition
    print([(i, i.label_, i.label) for i in doc.ents])

# COMMENT ON HOW spaCy has categorised each sentence:
# We can see that spacy has tokenized each word
# and punctuation. However, we note that spacy recognize
# entities, but not object.

# Look up and print the meaning of entities that you don't understand
print(spacy.explain('PERSON'))
print(spacy.explain('GPE'))

# I looked up for PERSON and GPE, respectively for 'Jill' and 'Mississippi'
# It does make sense in terms of the word associated with it