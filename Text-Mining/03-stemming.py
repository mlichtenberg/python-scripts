# Stemming is the process of reducing words to their stem/base/root form.
# For example, the base form of both "fishing" and "fished" is "fish".  Note that 
# the base form may not be a valid word; a word such as "compared" might have
# a base form of "compar"

import pandas as pd
import numpy as np
import nltk
import os

# Get the 'punkt' sentence tokenizer from the Python Natural Language Toolkit.
nltk.download('punkt')

# Read the text to be analyzed.  Specify the encoding to avoid errors from unrecognized chars.
with open('data/StatusOfTheBarredOwlInAlberta.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Pass the text into word_tokenize to tokenize it into words
from nltk.tokenize import word_tokenize 
tokens = word_tokenize(text)

# Get an unordered list of each unique token
unique_tokens = list(set(tokens))

# Import Porterstemmer from the Python Natural Language Toolkit
from nltk.stem import PorterStemmer
pst = PorterStemmer()

# Importing LancasterStemmer from the Python Natural Language Toolkit.
# This strategy is more aggressive than Porterstemmer.
from nltk.stem import LancasterStemmer
lst = LancasterStemmer()

# Use the two stemmer strategies to determine the stem of each token in the list
print('\nTOKEN : PORTER-STEMMED TOKEN : LANCANSTER-STEMMED TOKEN\n')
print('----------------------------------------\n')
for word in unique_tokens :
   print(word + " : " + pst.stem(word) + " : " + lst.stem(word))
