# “Stop words” are commonly used words in a language.  English exmaples are "the", "a",
# "at",  and "for".  In text mining, these words are often considered unimportant.
# The Python Natural Language Toolkit provides a way to remove stop words from text.

import pandas as pd
import numpy as np
import nltk
import os

# Get the 'punkt' sentence tokenizer from the Python Natural Language Toolkit.
nltk.download('punkt')

# Get the 'stopwords' resource from the Python Natural Language Toolkit.
nltk.download('stopwords')

# Read the text to be analyzed.  Specify the encoding to avoid errors from unrecognized chars.
with open('data/StatusOfTheBarredOwlInAlberta.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Pass the text into word_tokenize to tokenize it into words
from nltk.tokenize import word_tokenize 
tokens = word_tokenize(text.lower())  # force everything to lowercase before tokenization

print('\nORIGINAL LIST OF TOKENS\n')
print('----------------------------------------\n')
print(tokens)

# Load the stopwords
from nltk.corpus import stopwords
a = set(stopwords.words('english'))

# Compare the tokens to the stopwords, and build a list of tokens that omits the stopwords
tokens_without_stopwords = [x for x in tokens if x not in a]

print('\nTOKENS WITHOUT STOP WORDS\n')
print('----------------------------------------\n')
print(tokens_without_stopwords)

# Use string operations to remove punctuation/numbers from the original text
import string
translate_table = dict((ord(char), None) for char in string.punctuation)  # unicode
no_punctuation = text.lower().translate(translate_table)

translate_table = dict((ord(char), None) for char in string.digits)  # unicode
no_punctuation_or_digits = no_punctuation.translate(translate_table)

# Now tokenize and remove stopwords from the string without the punctuation/numbers
tokens = word_tokenize(no_punctuation_or_digits)
tokens_without_stopwords = [x for x in tokens if x not in a]

print('\nTOKENS WITH NO PUNCTUATION, NUMBERS, OR STOP WORDS\n')
print('----------------------------------------\n')
print(tokens_without_stopwords)
