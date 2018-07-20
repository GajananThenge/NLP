# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 10:40:29 2018

@author: hp-pc
"""

'''Name entity relational '''


import nltk

para = '''The Taj Mahal was built by Emperor Shah Jahan'''

words = nltk.word_tokenize(para)
tagged_word = nltk.pos_tag(words)

namedEnt = nltk.ne_chunk(tagged_word)

namedEnt.draw()

namedEnt.ORGANIZATION