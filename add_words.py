from words import *

repo = WordRepository()

def read_word():
    text = raw_input("\tenter text> ")
    translation = raw_input("\tenter translation> ")
    word_class = raw_input("\tenter class> ")
    return Word(text, translation, word_class)


while(True):
    print "Word {0}:".format(repo.words_count())
    word = read_word()
    word_inserted = repo.insert_word(word)

    if word_inserted:
        print "Word {0} inserted successfully!".format(word.text)
    else:
        print "Word {0} already exists.".format(word.text)

    add_another_word = raw_input("Add another word (y/n)?> ")
    if add_another_word.lower() != 'y':
        print("\nGoodbye!")
        break
