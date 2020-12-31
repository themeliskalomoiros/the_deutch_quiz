#!/usr/bin/python


def print_words():
    import words
    repo = words.WordRepository()
    words = repo.get_words()

    for w in words:
        print w.text, w.translation, w.word_class


if __name__ == '__main__':
    print_words()
