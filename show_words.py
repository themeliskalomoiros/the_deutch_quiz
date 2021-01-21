#!/usr/bin/python


def print_words():
    import words
    repo = words.WordRepository()
    words = repo.get_words()

    for w in words:
        print w.text.encode('utf8'), w.translation.encode('utf8'), w.word_class.encode('utf8')


if __name__ == '__main__':
    print_words()
