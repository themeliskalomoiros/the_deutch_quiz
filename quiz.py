#!/usr/bin/python

import json
from random import shuffle
from words import WordRepository


class Quiz(object):

    def __init__(self):
        # that is a list of Word objects.
        all_words = WordRepository().get_words()
        # that is a dictionary with word.text: times_shown
        word_stats = self.get_word_stats()
        self.synchronize_stats(all_words, word_stats)
        # sorted list of tupples in the form (Word.text, times_shown)
        word_stats_list = sorted(word_stats.items(), key = lambda x:x[1], reverse = True)
        self.words = []
        for i in range(0, 6):
            word_stat = word_stats_list[i]
            for w in all_words:
                if w.text == word_stat[0]:
                    self.words.append(w)
                    break

    def get_word_stats(self):
        with open('quiz.json', 'r') as file:
            raw_json = file.read().decode('utf8')
            return json.loads(raw_json)

    def synchronize_stats(self, words, stats):
        if len(words) > len(stats):
            for w in words:
                if not w.text in stats:
                    # set a default value for every word that does not exist in quiz.json
                    stats[w.text] = 0

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
