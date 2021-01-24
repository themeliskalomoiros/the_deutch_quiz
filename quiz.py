#!/usr/bin/python

import json
from random import shuffle
from words import WordRepository


class QuizRepository(object):

    def __init__(self):
        all_words = WordRepository().get_words()
        self.word_frequencies = self.get_sorted_frequencies(all_words)
        self.words = self.init_words(all_words)

    def get_sorted_frequencies(self, all_words):
        frequencies = self.load_frequencies('quiz.json')
        self.synchronize_frequencies(all_words, frequencies)
        return sorted(frequencies.items(), key = lambda s:s[1], reverse = True)

    def load_frequencies(self, file_name):
        with open(file_name, 'r') as file:
            raw_json = file.read().decode('utf8')
            return json.loads(raw_json)

    def synchronize_frequencies(self, words, stats):
        """Add zero frequencies for new words."""
        if len(words) > len(stats):
            for w in words:
                if not w.text in stats:
                    stats[w.text] = 0

    def init_words(self, all_words):
        words = []
        for i in range(0, 6):
            f = self.word_frequencies[i]
            for w in all_words:
                if w.text == f[0]:
                    words.append(w)
                    break
        return words


class Quiz(object):

    def __init__(self):
        self.repo = QuizRepository()
        self.words = self.repo.words

    def start(self):
        print "\n*********************************"
        print "* Welcome to 'The Deutsch Quiz' *"
        print "*********************************"

        shuffle(self.words)

        correct_answers = 0
        class_bonus = 0

        print "Debug: words length is", len(self.words)

        for i in range(0, 6):
            print "\n\nQuestion ", i + 1, "\n"

            text = self.words[i].text
            translation = self.words[i].translation
            w_class = self.words[i].word_class

            reply = raw_input("\tWhat does the word '{0}' means?$ ".format(text.encode('utf8')))

            if reply.lower().strip() == translation:
                print "\tThat's right!"
                correct_answers += 1

                reply = raw_input("\n\tAnd what's it's class (noun, verb, etc...)?$ ")

                if reply.lower().strip() == w_class:
                    print "\tCorrect!!"
                    class_bonus += 1
                else:
                    print "\tYou've missed that, it's", w_class

            else:
                print "\n\tWrong :(. The correct answer is '{0}'".format(translation)

        print "\n\nResults:"
        print "\tYou've answered", correct_answers, "out of 6 questions."
        print "\tYou've got", class_bonus, "class bonus points."
        print "Total score is ", correct_answers + class_bonus


if __name__ == '__main__':
    Quiz().start()
