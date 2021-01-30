# Similar to stemming, Lemmatization is the process of converting a word to its canonical/
# dictionary/citation form.  It differs from stemming in that lemmatization considers the 
# context and meaning of the words and converts it to its meaningful base form.  Stemming 
# simply reduces a word to a base form, often leading to results that are not valid words.

import pandas as pd
import numpy as np
import nltk
import os

# Get the 'punkt' sentence tokenizer from the Python Natural Language Toolkit.
nltk.download('punkt')

# Get 'wordnet', a lexical database for the English language, from from the Python Natural 
# Language Toolkit.  It helps to identify the meanings of words..
nltk.download('wordnet')

# Read the text to be analyzed.  Specify the encoding to avoid errors from unrecognized chars.
with open('data/StatusOfTheBarredOwlInAlberta.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Pass the text into word_tokenize to tokenize it into words
from nltk.tokenize import word_tokenize 
tokens = word_tokenize(text)

# Get an unordered list of each unique token
unique_tokens = list(set(tokens))

# Import the Lemmatizer library from the Python Natural Language Toolkit
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer() 

# Use the Lemmatizer to get the base form of each word in the list
print('\nTOKEN : LEMMATIZED TOKEN\n')
print('----------------------------------------\n')
for word in unique_tokens :
   print(word + " : " + lemmatizer.lemmatize(word))
