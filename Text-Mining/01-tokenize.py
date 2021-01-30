# Tokenization is the the process of breaking text into smaller pieces (tokens).
# For example, paragraphs might be broken into sentences, or sentences into words.

import pandas as pd
import numpy as np
import nltk
import os

# Get the 'punkt' sentence tokenizer from the Python Natural Language Toolkit.
nltk.download('punkt')

# Read the text to be tokenized.  Specify the encoding to avoid errors from unrecognized chars.
with open('data/StatusOfTheBarredOwlInAlberta.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Pass the text into word_tokenize to tokenize it into words
from nltk.tokenize import word_tokenize
tokens = word_tokenize(text)
print('\nWORDS\n')
print('----------------------------------------\n')
print(tokens)

# Pass the text into the sentence tokenzier to get a list of sentences
sentences = nltk.tokenize.sent_tokenize(text)
print('\nSENTENCES\n')
print('----------------------------------------\n')
print (sentences)
