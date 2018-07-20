# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 12:19:11 2018

@author: hp-pc
"""

from nltk.corpus import wordnet

syno=[]
anto=[]

for syn in wordnet.synsets("good"):
    for s in syn.lemmas():
        syno.append(s.name)
        for a in s.antonyms():
            anto.append(a.name)