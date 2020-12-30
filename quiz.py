
from random import shuffle
from words import WordRepository

print "Welcome to 'The Deutsch Quiz'"

words = WordRepository().get_words()
shuffle(words)

correct_answers = 0
class_bonus = 0

for i in range(0, 6):
    print "\n\nQuestion ", i + 1, "\n"
    
    text = words[i].text
    translation = words[i].translation
    w_class = words[i].word_class
    
    reply = raw_input("\tWhat does the word '{0}' means?$ ".format(text))

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
        print "\n\tWrong :(. The correct answer '{0}'".format(translation)

print "You've answered", correct_answers, "out of 6 questions."
print "You've got", class_bonus, "class bonus points."
