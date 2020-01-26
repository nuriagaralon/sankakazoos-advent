#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Grab random words from the british dictionary
For Sankakazoos's Christmas project

@author: Sankakyumu
"""
import re
import random

n = int(input('How many words do you want? '))
numbers = set()

# Add random numbers to the list numbers.
# The range does not include numbers 1-10108 because these
# lines contain proper nouns.
for i in range(n):
    x = random.randrange(19109, 101825)
    numbers.add(x)

print()
with open("british-english") as words: # English dictionary
    for i, word in enumerate(words):
        if i in numbers:
            word = re.sub(r'\'s', '', word) #Removes possessive 's
            word = word.strip()  # Removes extraneous whitespace
            print(word)
