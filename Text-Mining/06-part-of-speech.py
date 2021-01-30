# Part of Speech tagging (or PoS tagging) is the process of determining the part of speech
# of every token in a document, and then tagging it as such. For example, PoS tagging will
# determine whether a given token represents a noun, verb, adjective, or something else.

# Here is a list of parts-of-speech tags that may be identified:
#  CC | Coordinating conjunction
#  CD | Cardinal number
#  DT | Determiner
#  EX | Existential there
#  FW | Foreign word
#  IN | Preposition or subordinating conjunction
#  JJ | Adjective
#  JJR | Adjective, comparative
#  JJS | Adjective, superlative
#  LS | List item marker
#  MD | Modal
#  NN | Noun, singular or mass
#  NNS | Noun, plural
#  NNP | Proper noun, singular
#  NNPS | Proper noun, plural
#  PDT | Predeterminer
#  POS | Possessive ending
#  PRP | Personal pronoun
#  PRP$ | Possessive pronoun
#  RB | Adverb
#  RBR | Adverb, comparative
#  RBS | Adverb, superlative
#  RP | Particle
#  SYM | Symbol
#  TO | to
#  UH | Interjection
#  VB | Verb, base form
#  VBD | Verb, past tense
#  VBG | Verb, gerund or present participle
#  VBN | Verb, past participle
#  VBP | Verb, non-3rd person singular present
#  VBZ | Verb, 3rd person singular present
#  WDT | Wh-determiner
#  WP | Wh-pronoun
#  WP$ | Possessive wh-pronoun
#  WRB | Wh-adverb

import pandas as pd
import numpy as np
import nltk
import os

# Get the 'punkt' sentence tokenizer from the Python Natural Language Toolkit.
nltk.download('punkt')

# Get the English Part-Of-Speech (POS) tagger from the Python Natural Language Toolkit.
nltk.download('averaged_perceptron_tagger')

# Read the text to be analyzed.  Specify the encoding to avoid errors from unrecognized chars.
with open('data/StatusOfTheBarredOwlInAlberta.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Remove punctuation and numbers
import string
translate_table = dict((ord(char), None) for char in string.punctuation)
text = text.translate(translate_table)

translate_table = dict((ord(char), None) for char in string.digits)
text = text.translate(translate_table)

# Pass the string text into word_tokenize to tokenize it into words
from nltk.tokenize import word_tokenize 
tokens = word_tokenize(text.lower())  # force everything to lowercase before tokenization
unique_tokens = list(set(tokens))

# Print each word and it's part-of-speech tag
print('\nPARTS OF SPEECH\n')
print('----------------------------------------\n')
for token in unique_tokens:
    print(nltk.pos_tag([token]))
