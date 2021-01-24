#!/usr/bin/python

from words import *


def update_words():
    repo = WordRepository()

    while True:
        reply = unicode(raw_input('\nWord to update:> '), 'utf8')

        if reply:
            original_word = repo.get_word(reply)

            if original_word:
                prompt_msg = '\nFound \'{0}\' ({1}, {2}).\n'.format(reply.encode('utf8'), original_word.translation.encode('utf8'), original_word.word_class.encode('utf8'))
                print prompt_msg

                prompt_msg = 'Set new value for \'{0}\' - leave empty for default.> '.format(original_word.text.encode('utf8'))
                text = unicode(raw_input(prompt_msg), 'utf8')

                prompt_msg = 'Set new value for translation (current \'{0}\') - leave empty for default.> '.format(original_word.translation.encode('utf8'))
                translation = unicode(raw_input(prompt_msg), 'utf8')

                prompt_msg = 'Set new value for class (current \'{0}\') - leave empty for default.> '.format(original_word.word_class.encode('utf8'))
                word_class = unicode(raw_input(prompt_msg), 'utf8')

                if text or translation or word_class:
                    word_deleted = repo.delete_word(reply)

                    # Set new values to the original word and insert it again to the database.
                    if word_deleted:
                        if text:
                            original_word.text = text
                        if translation:
                            original_word.translation = translation
                        if word_class:
                            original_word.word_class = word_class

                        repo.insert_word(original_word)

                        prompt_msg = "\n'{0}' updated to ({1}, {2}, {3}).".format(reply.encode('utf8'), original_word.text.encode('utf8'), original_word.translation.encode('utf8'), original_word.word_class.encode('utf8'))
                        print prompt_msg
                else:
                    print "\nYou haven't defined any values, aborting..."

            else:
                print reply.encode('utf8'), 'not exist.'
        else:
            print 'Goodbye!'
            break


if __name__ == '__main__':
    update_words()
