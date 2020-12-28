from words import *

counter = 0

def read_word():
    global counter
    counter += 1
    print(f"Word {counter}:")
    text = input("\tenter text > ")
    translation = input("\tenter translation > ")
    word_class = input("\tenter class > ")
    return Word(text, translation, word_class)

db = Database()

while(True):
    word = read_word()
    word_inserted = db.insert_word(word)

    if word_inserted:
        print(f"Word {word.text} inserted successfully!")
    else:
        print(f"Word {word.text} already exists.")

    add_another_word = input("Add another word (y/n)?")
    if add_another_word.lower() != 'y':
        print("Goodbye!")
        break
