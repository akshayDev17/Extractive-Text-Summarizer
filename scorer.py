""" Module to award score to tokenized sentences """

from collections import defaultdict
from nltk.tokenize import word_tokenize
from nltk import FreqDist


def give_score(word_list, sentence_list):

    """ we first calculate the frequency distribution of each word in
    our data(word tokenize list), and based on the words occuring in a sentence,
    we assign a score value to that sentence.
    if most-occuring words are found in a sentence, that sentence is
    awarded a higher score."""

    word_count = FreqDist(word_list)
    len_sent = len(sentence_list)
    top_dict = defaultdict(int)
    for i in range(len_sent):
        for word in word_tokenize(sentence_list[i].lower()):
            if word in word_count:
                top_dict[i] += word_count[word]

    return top_dict
