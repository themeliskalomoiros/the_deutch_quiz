import words

db = words.Database()

words = db.get_words()

for w in words:
    print(w.text, w.translation, w.word_class)
