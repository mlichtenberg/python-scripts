# Vectorization or vectorizing is the process of converting text data to numerical 
# data which can be used for machine learning.

import pandas as pd
import numpy as np
import nltk
import os

# Get the 'punkt' sentence tokenizer from the Python Natural Language Toolkit.
nltk.download('punkt')

# Read the text to be analyzed.  Specify the encoding to avoid errors from unrecognized chars.
with open('data/StatusOfTheBarredOwlInAlberta.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Pass the text into the sentence tokenzier to get a list of sentences.
sentences = nltk.tokenize.sent_tokenize(text)

# Use a stemmer to get the base form for each word
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
bases = [[stemmer.stem(word) for word in sentence.split()] for sentence in sentences]

# Recreate the sentences with the base forms of the tokens
sentences = [' '.join(base) for base in bases]

# Use CountVecorizer from the SciKit-Learn machine learning toolkit to apply Bag Of Word 
# (basically a word count) for vectorizing.  The resulting numeric array can be used for
# machine learning.
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()
bag_of_words = cv.fit_transform(sentences)

# Print the bag of words array
import numpy as np
np.set_printoptions(threshold=np.inf) # print entire bag_of_words array
print('\nVECTORIZED TEXT\n')
print('----------------------------------------\n')
print(bag_of_words.todense())
np.set_printoptions(threshold=False)
