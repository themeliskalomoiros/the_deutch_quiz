import json

class Word(object):

    def __init__(self, text = "", translation = "", word_class = ""):
        self.text = text
        self.translation = translation
        self.word_class = word_class


class Database(object):
    """ Initializes quiz data stored in json format."""

    # Json metadata
    file_name = "data.json"
    key_class = "class"
    key_translation = "translation"

    def __init__(self):
        self.data = self.load_data()

    def load_data(self):
        try:
            file = open(Database.file_name, "r")
            file_data = file.read()
            return json.loads(file_data)
        except FileNotFoundError as e:
            print("Database: ", e)
            raise FileNotFoundError()
        finally:
            if file:
                file.close()

    def get_words(self):
        words = []
        print(type(self.data))
        for key, value in self.data.items():
            text = key
            translation = value[Database.key_translation]
            word_class = value[Database.key_class]
            word = Word(text, translation, word_class)

            words.append(word)

        return words

    def insert_word(self, word):
        """ Returns true for a successfull insert, false otherwise."""
        if self.word_exist(word):
            return False
        else:
            key = word.text
            self.data[key] = {
                Database.key_translation: word.translation,
                Database.key_class: word.word_class
            }

            try:
                file = open(Database.file_name, "w")
                raw_json = json.dumps(self.data)
                file.write(raw_json)

                return True
            except Exception as e:
                raise Exception(f"Database: {e}")
            finally:
                if file:
                    file.close()

    def word_exist(self, word):
        key = word.text

        if key in self.data:
            return True
        else:
            return False
