#!/usr/bin/python

import words

repo = words.WordRepository()
words = repo.get_words()

for w in words:
    print w.text, w.translation, w.word_class
