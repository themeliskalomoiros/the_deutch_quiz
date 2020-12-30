#!/usr/bin/env python
# coding=utf-8

import words

repo = words.WordRepository()

words = repo.get_words()

for w in words:
    print w.text, w.translation, w.word_class
