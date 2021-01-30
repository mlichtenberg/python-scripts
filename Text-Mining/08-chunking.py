# Chunking means picking up individual pieces of information and grouping them 
# into bigger pieces (or chunks).  For example, adjectives and nouns can be 
# combined to form a "chunk".

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

# Pass the text into word_tokenize to tokenize it into words
from nltk.tokenize import word_tokenize 
tokens = word_tokenize(text.lower())  # force everything to lowercase before tokenization

# Get the parts-of-speech for each token
tags = nltk.pos_tag(tokens)

# Use the Natural Language Toolkit  regular expression parser to examine the parts-of-speech output
# and find combinations of determiner, adjective, and noun.  These combinations will combined into
# "chunnks".
reg = "NP: {<DT>?<JJ>*<NN>}"
a = nltk.RegexpParser(reg)
result = a.parse(tags)

print('\nCHUNKING\n')
print('----------------------------------------\n')
for chunk in result:
    if hasattr(chunk, 'label'):
        print(' '.join(c[0] for c in chunk))
    else:
        print(chunk[0])
