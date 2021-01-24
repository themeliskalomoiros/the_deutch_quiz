#!/usr/bin/python

import time
import json
from random import shuffle
from words import WordRepository


class QuizRepository(object):

    file_name = 'quiz.json'

    def __init__(self):
        all_words = WordRepository().get_words()
        self.timestamps = self.load_timestamps()
        self.synchronize_timestamps(all_words)
        self.sorted_timestamps = self.get_sorted_timestamps()
        self.words = self.init_words(all_words)

    def load_timestamps(self):
        with open(QuizRepository.file_name, 'r') as file:
            raw_json = file.read().decode('utf8')
            return json.loads(raw_json)

    def synchronize_timestamps(self, words):
        """Add timestamps for new words."""
        new_words = len(words) > len(self.timestamps)
        if new_words:
            for w in words:
                new_word = not w.text in self.timestamps
                if new_word:
                    self.timestamps[w.text] = 0

    def get_sorted_timestamps(self):
        return sorted(
            self.timestamps.items(),
            key = lambda ts : ts[1])

    def init_words(self, all_words):
        words = []
        for i in range(0, 6):
            ts = self.sorted_timestamps[i]
            for w in all_words:
                if w.text == ts[0]:
                    words.append(w)
                    break
        return words


    def update_word(self, word):
        self.timestamps[word.text] = time.time()

    def save_changes_to_disk(self):
        """Saves all the changes into the disk"""
        with open(QuizRepository.file_name, 'w') as file:
            raw_json = json.dumps(self.timestamps, ensure_ascii = False)
            file.write(raw_json.encode('utf8'))

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

        for i in range(0, 6):
            print "\n\nQuestion ", i + 1, "\n"

            text = self.words[i].text
            translation = self.words[i].translation
            w_class = self.words[i].word_class

            self.repo.update_word(self.words[i])

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

        self.repo.save_changes_to_disk()

        print "\n\nResults:"
        print "\tYou've answered", correct_answers, "out of 6 questions."
        print "\tYou've got", class_bonus, "class bonus points."
        print "Total score is ", correct_answers + class_bonus


if __name__ == '__main__':
    Quiz().start()
