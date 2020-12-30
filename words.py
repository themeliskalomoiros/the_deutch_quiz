#!/usr/bin/env python
# coding=utf-8

import json

class Word(object):

    def __init__(self, text = "", translation = "", word_class = ""):
        self.text = text
        self.translation = translation
        self.word_class = word_class


class WordRepository(object):
    """ Initializes words stored in a json file."""

    # Json metadata
    file_name = "words.json"
    key_class = "class"
    key_translation = "translation"

    def __init__(self):
        self.words = self.load_words()

    def words_count(self):
        if self.words:
            return len(self.words)
        else:
            return 0

    def load_words(self):
        try:
            with open(WordRepository.file_name, "r") as file:
                return json.loads(file.read())
        except IOError:
            msg = "WordRepository: error in load_words, does the file exists?"
            raise IOError(msg)

    def get_words(self):
        words = []

        if self.words:
            for key, value in self.words.items():
                text = key
                translation = value[WordRepository.key_translation]
                word_class = value[WordRepository.key_class]
                word = Word(text, translation, word_class)
                words.append(word)

        return words

    def insert_word(self, word):
        """ Returns true for a successfull insert, false otherwise."""
        if self.words:
            if self.word_exist(word):
                return False
            else:
                key = word.text
                self.words[key] = {
                    WordRepository.key_translation: word.translation,
                    WordRepository.key_class: word.word_class
                }

                try:
                    with open(WordRepository.file_name, "w") as file:
                        raw_json = json.dumps(self.words, ensure_ascii=False)
                        file.write(raw_json)
                        return True
                except IOError:
                    msg = "WordRepository: error in '{0}'s insertion.".format(word.text)
                    raise IOError(msg)

    def word_exist(self, word):
        key = word.text

        if key in self.words:
            return True
        else:
            return False
