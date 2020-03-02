import os.path
import re

def count_words(fn,):
    """
    Count words in a file. 

    Known issue: don't deal with apostrophe.
    """
    if os.path.isfile(fn):
        with open(fn, 'r') as fh:
            total = 0
            pattern = re.compile('^[a-zA-Z]+[,.]?$')
            for line in fh:
                words = line.strip().split(' ')
                words = list(filter(pattern.match, words))
                total += len(words)
            return total

print("Total words: {}".format(count_words('./readme.md')))

