#!/usr/bin/python

from words import *


def add_words():
    repo = WordRepository()

    while True:
        print "\nWord", repo.words_count()
        text = unicode(raw_input('\tenter text> ').strip(), 'utf-8')

        if text:
            if repo.word_exists(text):
                print '\n', text, 'exists.'
                continue
            else:
                translation = unicode(raw_input('\tenter translation> ').strip(), 'utf-8')
                word_class = unicode(raw_input('\tenter class> ').strip(), 'utf-8')
                word = Word(text, translation, word_class)

                repo.insert_word(word)
                print '\n', word.text, 'inserted.'
        else:
            print '\nGoodbye!'
            return

if __name__ == '__main__':
    add_words()
