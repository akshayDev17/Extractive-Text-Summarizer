""" Create a summary of the text in a given text file """

import sys

from file_read import read_file
from filter_space import clean_up
from tokenizer import new_tokenize
from scorer import give_score
from summary import select_sentence

if __name__ == "__main__":

    CONTENTS = read_file()
    if CONTENTS:
        LIMIT = int(sys.argv[2])
        CONTENTS = clean_up(CONTENTS)
        TEMP = new_tokenize(CONTENTS)
        WORDS, SENTENCES = TEMP[0], TEMP[1]
        SCORE = give_score(WORDS, SENTENCES)
        print(select_sentence(SCORE, SENTENCES, LIMIT))
