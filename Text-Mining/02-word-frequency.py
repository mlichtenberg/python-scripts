# Word Frequency is the number of times a word (or token) appears in a text.

import pandas as pd
import numpy as np
import nltk
import os

# Get the 'punkt' sentence tokenizer from the Python Natural Language Toolkit.
nltk.download('punkt')

# Set up pandas to print entire dataframes.  This ensure that this script will
# output all of the results.  By default, pandas truncates dataframes when they
# are printed.
pd.set_option("display.max_rows", None, "display.max_columns", None)

# Read the text to be analyzed.  Specify the encoding to avoid errors from unrecognized chars.
with open('data/StatusOfTheBarredOwlInAlberta.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Pass the text into word_tokenize to tokenize it into words
from nltk.tokenize import word_tokenize 
token = word_tokenize(text)

# Find the frequency of each token
from nltk.probability import FreqDist
fdist = FreqDist(token)
print('\nWORD FREQUENCE FOR EACH TOKEN\n')
print('----------------------------------------\n')
print(pd.DataFrame(list(fdist.items()), columns = ["Word","Frequency"]))
print()

# Find the frequency of the top 20 tokens
print('\nTOP 20 TOKENS\n')
print('----------------------------------------\n')
print('Top 20 Tokens')
fdisttop20 = fdist.most_common(20)
print(pd.DataFrame(fdisttop20, columns = ["Word","Frequency"]))

