# This script combines several text-mining and machine-learning methods to
# analyze sets of scholarly article titles and predict which of the articles
# are about "owls".
# The methods used include the text-mining methods of Tokenization, Word 
# Frequency, Stemming, Lemmatization, Stop-word Removal, and Vectorization.
# In addition, Linear Regression (machine learning) is used to analyze the 
# text.

# Import the necessary libraries
import pandas as pd
import numpy as np
import nltk
import os
import string
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer

###############################

def remove_stopwords(sentence):
    from nltk.corpus import stopwords
    a = set(stopwords.words('english')) # Load the English stopwords

    # Tokenize the sentence
    tokens = word_tokenize(sentence)

    # Remove stopwords from the list of tokens
    tokens_clean = [x for x in tokens if x not in a]

    # Recreate the sentence without the stopwords
    return ' '.join(tokens_clean)

def show_top_20_words_in_set(articles, setname):
    from nltk.probability import FreqDist
    tokens = word_tokenize(' '.join(articles)) # tokenize the entire set into words
    fdist = FreqDist(tokens) # Get the frequency of each word
    fdisttop20 = fdist.most_common(20) # Show the frequency of the top 20 words in the set
    print('\n----------------------------------------\n')
    print('TOP 20 WORDS in {0}\n'.format(setname))
    print(pd.DataFrame(fdisttop20, columns = ["Word","Frequency"]))
    print()

def get_stemmed_sentence(sentence):
    # Use a stemmer to get the base form for each word
    from nltk.stem import PorterStemmer
    stemmer = PorterStemmer()
    bases = [stemmer.stem(word) for word in sentence.split()]

    # Recreate the sentence with the word base forms
    return ' '.join(bases)

def get_lemmatized_sentence(sentence):
    # Importing Lemmatizer library from nltk
    from nltk.stem import WordNetLemmatizer
    lemmatizer = WordNetLemmatizer() 

    # Use the Lemmatizer to get the base form of each word in the list
    bases = [lemmatizer.lemmatize(word) for word in sentence.split()]

    # Recreate the sentence with the word base forms
    return ' '.join(bases)

def get_predictions(training_bow, scores, predict_bow):
    from sklearn.linear_model import LinearRegression
    lr = LinearRegression()
    lr.fit(training_bow, scores)
    return lr.predict(predict_bow)

###############################

# Set up the pandas print options for printing dataframes
pd.set_option("display.max_rows", None, "display.max_columns", None) # print entire dataframe
pd.options.display.float_format = '{:,.2f}'.format # set the format for float values
pd.options.display.max_colwidth = 75 # set length of string values
pd.options.display.colheader_justify = 'left'
pd.options.display.width = 100

# Make sure the necessary resources are available
nltk.download('punkt') # Get the 'punkt' sentence tokenizer
nltk.download('stopwords') # Get the 'stopwords' resource

###############################

# Get three lists: the training set of article titles, their associated scores,
# and the validation set that will be used to verify the model.
#
# In the list scores, 1 indicates that the article is about owls and 0 indicates
# it is not.  The first 25 articles in the validation set are about owls, and the
# last 25 are not.
with open('data/Scores.txt', 'r', encoding='utf-8') as file:
    scores = file.read().splitlines()
with open('data/Training.txt', 'r', encoding='utf-8') as file:
    training_articles = file.read().splitlines()
with open('data/Validation.txt', 'r', encoding='utf-8') as file:
    validation_articles = file.read().splitlines()

# Get three additional lists of articles.  These are the test sets.  A linear 
# regression model will be used to try to predict which of the articles in these
# lists are about owls.
#   1st list = articles with "owl" in the title
#   2nd list = articles about owls that do not have "owl" in the title
#   3rd list = articles that are not about owls
with open('data/Predict-1-Owl-Articles.txt', 'r', encoding='utf-8') as file:
    test_articles_1 = file.read().splitlines()
with open('data/Predict-2-Owl-Articles.txt', 'r', encoding='utf-8') as file:
    test_articles_2 = file.read().splitlines()
with open('data/Predict-3-Non-Owl-Articles.txt', 'r', encoding='utf-8') as file:
    test_articles_3 = file.read().splitlines()

# Remove punctuation, digits, and stop words from the training set
translate_table_punctuation = dict((ord(char), None) for char in string.punctuation)
translate_table_digits = dict((ord(char), None) for char in string.digits)
training_articles = [article.translate(translate_table_punctuation).translate(translate_table_digits) for article in training_articles]
training_articles = [remove_stopwords(article) for article in training_articles]

# Show the top 20 words in the training set and in each test set
show_top_20_words_in_set(training_articles, "training set")
show_top_20_words_in_set(test_articles_1, "test set 1 (owl articles)")
show_top_20_words_in_set(test_articles_2, "test set 2 (owl articles)")
show_top_20_words_in_set(test_articles_3, "test set 3 (non-owl articles)")

# stem the titles in each list of articles
training_articles_stemmed = [get_stemmed_sentence(article) for article in training_articles]
validation_articles_stemmed = [get_stemmed_sentence(article) for article in validation_articles]
test_articles_1_stemmed = [get_stemmed_sentence(article) for article in test_articles_1]
test_articles_2_stemmed = [get_stemmed_sentence(article) for article in test_articles_2]
test_articles_3_stemmed = [get_stemmed_sentence(article) for article in test_articles_3]

# Vectorize the stemmed sets into numeric values (bags of words)
cv = CountVectorizer()
training_stem_bow = cv.fit_transform(training_articles_stemmed)
validation_stem_bow = cv.transform(validation_articles_stemmed)
test1_stem_bow = cv.transform(test_articles_1_stemmed)
test2_stem_bow = cv.transform(test_articles_2_stemmed)
test3_stem_bow = cv.transform(test_articles_3_stemmed)

# Use a Linear Regression model to predict whether each article in the validation and 
# test sets are about owls.  The closer the score is to 1, the more likely the article
# is about owls.
print('\n----------------------------------------\n')
print('PREDICTION OUTPUT: STEMMED WORDS')
print('\nVALIDATION SET (25 owl articles and 25 non-owl articles)\n')
print(pd.DataFrame({'article': validation_articles, 
                    'predicted score': get_predictions(training_stem_bow, scores, validation_stem_bow)}))
print('\nTEST SET 1 (Owl articles with \'owl\' in title)\n')
print(pd.DataFrame({'article': test_articles_1, 
                    'predicted score': get_predictions(training_stem_bow, scores, test1_stem_bow)}))
print('\nTEST SET 2 (Owl articles without \'owl\' in title)\n')
print(pd.DataFrame({'article': test_articles_2, 
                    'predicted score': get_predictions(training_stem_bow, scores, test2_stem_bow)}))
print('\nTEST SET 3 (Non-owl articles)\n')
print(pd.DataFrame({'article': test_articles_3, 
                    'predicted score': get_predictions(training_stem_bow, scores, test3_stem_bow)}))

# lemmatize the titles in each list of articles
training_articles_lemm = [get_lemmatized_sentence(article) for article in training_articles]
validation_articles_lemm = [get_lemmatized_sentence(article) for article in validation_articles]
test_articles_1_lemm = [get_lemmatized_sentence(article) for article in test_articles_1]
test_articles_2_lemm = [get_lemmatized_sentence(article) for article in test_articles_2]
test_articles_3_lemm = [get_lemmatized_sentence(article) for article in test_articles_3]

# Vectorize the lemmatized sets into numeric values (bags of words)
cv = CountVectorizer()
training_lemm_bow = cv.fit_transform(training_articles_lemm)
validation_lemm_bow = cv.transform(validation_articles_lemm)
test1_lemm_bow = cv.transform(test_articles_1_lemm)
test2_lemm_bow = cv.transform(test_articles_2_lemm)
test3_lemm_bow = cv.transform(test_articles_3_lemm)

# Use a Linear Regression model to predict whether each article in the validation and 
# test sets are about owls.  The closer the score is to 1, the more likely the article
# is about owls.
print('\n----------------------------------------\n')
print('PREDICTION OUTPUT: LEMMATIZED WORDS')
print('\nVALIDATION SET (25 owl articles and 25 non-owl articles)\n')
print(pd.DataFrame({'article': validation_articles, 
                    'predicted score': get_predictions(training_lemm_bow, scores, validation_lemm_bow)}))
print('\nTEST SET 1 (Owl articles with \'owl\' in title)\n')
print(pd.DataFrame({'article': test_articles_1, 
                    'predicted score': get_predictions(training_lemm_bow, scores, test1_lemm_bow)}))
print('\nTEST SET 2 (Owl articles without \'owl\' in title)\n')
print(pd.DataFrame({'article': test_articles_2, 
                    'predicted score': get_predictions(training_lemm_bow, scores, test2_lemm_bow)}))
print('\nTEST SET 3 (Non-owl articles)\n')
print(pd.DataFrame({'article': test_articles_3, 
                    'predicted score': get_predictions(training_lemm_bow, scores, test3_lemm_bow)}))
