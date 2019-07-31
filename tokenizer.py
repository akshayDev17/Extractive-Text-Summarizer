""" Module which tokenizes the given data, i.e. filters out
stopwords(prepositions, conjunctions and so on), punctuation marks,
and gives us sentence and word arrays"""

import string
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

def new_tokenize(input_string):

    """ Returns a list containing a list of words and a list of sentences
    given by nltk tokenize function and cleans up the punctuation marks
    and common stop words like 'or' and 'and' """

    stop_words = set(stopwords.words('english') + list(string.punctuation))
    unfiltered_words = word_tokenize(input_string)
    words = [word for word in unfiltered_words if word not in stop_words]
    sentences = sent_tokenize(input_string)
    return [words, sentences]
