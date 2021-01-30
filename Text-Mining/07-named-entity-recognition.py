# Named-entity recognition is the process of locating and classifying named entities 
# in text into pre-defined categories such as person names, organizations, locations,
# quantities, monetary values, percentages, and so on.

import pandas as pd
import numpy as np
import nltk
import os

# Get the 'punkt' sentence tokenizer from the Python Natural Language Toolkit.
nltk.download('punkt')

# Get the English Part-Of-Speech (POS) tagger from the Python Natural Language Toolkit.
nltk.download('averaged_perceptron_tagger')

# Get the chunker used to perform the named entity recognition from the Python Natural Language Toolkit.
nltk.download('maxent_ne_chunker')

# Get a list of English words from the Python Natural Language Toolkit.
nltk.download('words')

# Read the text to be analyzed.  Specify the encoding to avoid errors from unrecognized chars.
with open('data/StatusOfTheBarredOwlInAlberta.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Pass the text into word_tokenize to tokenize it into words.
# DO NOT force the text to lowercase, or the entity recognition will not work correctly!
from nltk.tokenize import word_tokenize
tokens = word_tokenize(text)

# Get the parts-of-speech for each token
tags = nltk.pos_tag(tokens)

# Get the chunk library from nltk and perform the named entity recognition.
# Named Entity Recognition is also known as entity identification, entity
# chunking, and entity extraction.
from nltk import ne_chunk
chunks = ne_chunk(tags)

print('\nNAMED ENTITY RECOGNITION\n')
print('----------------------------------------\n')
for ne in chunks:
    if hasattr(ne, 'label'):
        print(ne.label(), ' '.join(c[0] for c in ne))
 