#!/usr/bin/python

import json


class Word(object):

    def __init__(self, text = "", translation = "", word_class = ""):
        #Since its a german word its properties will be unicode strings (not byte strings).
        self.text = text
        self.translation = translation
        self.word_class = word_class


class WordRepository(object):
    """Initializes words stored in a json file."""

    # Json file metadata.
    file_name = "words.json"
    key_class = "class"
    key_translation = "translation"

    def __init__(self):
        # Char encoding is unicode.
        self.words = self.load_words()

    def load_words(self):
        try:
            with open(WordRepository.file_name, 'r') as file:
                raw_json = unicode(file.read(), 'utf8')
                return json.loads(raw_json)
        except IOError:
            # File does not exist, so we create it.
            with open(WordRepository.file_name, 'w') as file:
                file.write('{ }')
                return {}

    def words_count(self):
        if self.words:
            return len(self.words)
        else:
            return 0

    def get_words(self):
        words = []

        if self.words:
            for key, value in self.words.items():
                text = key
                translation = value[WordRepository.key_translation]
                word_class = value[WordRepository.key_class]
                words.append(Word(text, translation, word_class))

        return words

    def word_exists(self, word_text):
        # TODO: maybe it's better to accept a word object than the text.
        # TODO: maybe it's better to return the word instead of True or False
        if word_text in self.words:
            return True
        else:
            return False

    def get_word(self, word_text):
        if word_text in self.words:
            word_dict = self.words[word_text]
            translation = word_dict[WordRepository.key_translation]
            word_class = word_dict[WordRepository.key_class]

            return Word(word_text, translation, word_class)


    def insert_word(self, word):
        key = word.text

        if not key in self.words:
            self.words[key] = {
                WordRepository.key_translation: word.translation,
                WordRepository.key_class: word.word_class
            }

            self.save_words_to_file()

    def delete_word(self, word_text):
        if word_text in self.words:
            del self.words[word_text]
            self.save_words_to_file()
            return True
        else:
            return False

    def save_words_to_file(self):
        try:
            with open(WordRepository.file_name, 'w') as file:
                raw_json = json.dumps(self.words, ensure_ascii = False)
                file.write(raw_json.encode('utf8'))
        except IOError:
            raise IOError('WordRepository: error while saving words to file')
