import json

class Word(object):

    def __init__(self, text = "", translation = "", structure = ""):
        self.text = text
        self.translation = translation
        self.structure = structure


class Database(object):
    """ Initializes quiz data stored in json format."""

    # Json metadata
    json_file_name = "data.json"
    key_words = "words"
    key_structure = "structure"
    key_text = "text"
    key_translation = "translation"

    def __init__(self):
        self.raw_json = self.get_raw_json(json_file_name)

    def get_raw_json(self, file_name):
        try:
            file = open(file_name, "r")
            json_str = file.read()
            return json.loads(json_str)
        except FileNotFoundError as e:
            print "Database: ", e
            raise FileNotFoundError()
        finally:
            file.close()

    def load_words(self):
        words = []
        words_data = self.raw_json[key_words]
        structures_data = self.raw_json[key_structure]

        for word_data in words_data:
            text = word_data[key_word_text]
            translation = word_data[key_translation]
            structure_index = word_data[key_structure]
            structure = structures_data[structure_index]

            words.append(text, translation, structure)

        return words
