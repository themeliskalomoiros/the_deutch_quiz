import json

class Word(object):

    def __init__(self, text = "", translation = "", word_class = ""):
        self.text = text
        self.translation = translation
        self.word_class = word_class

    def to_json(self):
        data = {}
        data[Database.key_text] = self.text
        data[Database.key_translation] = self.translation
        data[Database.key_class] = self.word_class

        return data


class Database(object):
    """ Initializes quiz data stored in json format."""

    # Json metadata
    file_name = "data.json"
    key_words = "words"
    key_class = "class"
    key_text = "text"
    key_translation = "translation"

    def __init__(self):
        self.raw_json = self.get_raw_json()

    def get_raw_json(self):
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

    def load_words(self):
        words = []
        data = self.raw_json[Database.key_words]

        for word_data in data:
            word = self.load_word(word_data)
            words.append(word)

        return words

    def load_word(self, json_data):
        text = json_data[Database.key_text]
        translation = json_data[Database.key_translation]
        word_class = json_data[Database.key_class]

        return Word(text, translation, word_class)

    def insert_word(self, word):
        """ Returns true for a successfull insert, false otherwise."""
        if self.word_exist(word):
            return False
        else:
            try:
                file = open(Database.file_name, "w")
                words = self.raw_json[Database.key_words]
                words.append(word.to_json())

                self.raw_json = {Database.key_words: words}
                file.write(json.dumps(self.raw_json))

                return True
            except Exception as e:
                print(f"Database: Error in word insertion.\n{e}")
                return False
            finally:
                if file:
                    file.close()

    def word_exist(self, word):
        word_data = self.raw_json[Database.key_words]
        for wd in word_data:
            if word.text == wd[Database.key_text]:
                return True
            else:
                return False
