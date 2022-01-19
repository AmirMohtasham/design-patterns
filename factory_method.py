"""
Factory Method design pattern (Creational)
Factory Method defines a method or class, which should be used for creating objects instead of direct constructor call.
Provide a high level and flexibility usage for your code.
constructor, we define factory that generate translations(TranslationFactory)

 When do we use it?
    1- Have classes  which from this class, many objects are made.
    2- Hide the complexities and dependencies needed to build an object.
    3- When we want to build an object we have to check different conditions

Example :
    In this example we want to get the translations of the word in another languages.
    instead call direct constructor

"""

from abc import ABC, abstractmethod


class AbstractTranslator(ABC):
    translations = None

    def __init__(self):
        self._set_translations()

    @classmethod
    @abstractmethod
    def _set_translations(cls):
        """Used to set the list of words in language"""
        pass

    def translate(self, word):
        """Get translation of the word in language"""
        return self.translations.get(word, word)


class FarsiTranslator(AbstractTranslator):

    @classmethod
    def _set_translations(cls):
        """Used to set the list of words in Farsi language"""
        cls.translations = {'book': 'کتاب', 'father': 'پدر', 'water': 'آب', 'day': 'روز'}


class SpanishTranslator(AbstractTranslator):

    @classmethod
    def _set_translations(cls):
        """Used to set the list of words in Spanish language"""
        cls.translations = {'book': 'libro', 'father': 'padre', 'water': 'agua', 'day': 'día'}


class JapaneseTranslator(AbstractTranslator):
    @classmethod
    def _set_translations(cls):
        """Used to set the list of words in Japanese language"""
        cls.translations = {'book': '本', 'father': '父親', 'water': '水', 'day': '日'}


class TranslationFactory:
    """Factory that generate translations objects"""

    @staticmethod
    def get_translator(lang):
        translators = {
            "f": FarsiTranslator,
            "s": SpanishTranslator,
            "j": JapaneseTranslator,
        }
        translator = translators.get(lang)
        if translator:
            return translator()


if __name__ == '__main__':
    word = 'book'
    translate_to = input('Enter translate to (f, s, j):')

    # Create instance without factory design pattern
    # result = ""
    # if translate_to == 'f':
    #     result = FarsiTranslator().translate(word)
    # elif translate_to == 's':
    #     result = SpanishTranslator().translate(word)
    # elif translate_to == 'j':
    #     result = JapaneseTranslator().translate(word)

    # Create instance with Factory design pattern
    result = TranslationFactory.get_translator(translate_to).translate(word)
    print(result)
