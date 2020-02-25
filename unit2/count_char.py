# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 09:39:33 2020

@author: 85726
"""

import os.path

def count_word(file):
    with open(file, 'r') as f:
        words = 0
        for line in f:
            for char in ('#', '\n'):
                line = line.replace(char," ")
            word = line.split()
            words += len(word)
        return words
        
file = './test.md'

if os.path.isfile(file):
    words = count_word(file)
    print('{} words in file'.format(words))
else:
    print('it is not a file')
