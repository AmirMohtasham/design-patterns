"""
Abstract Factory Design pattern (Creational)
Solves the problem of creating entire product families
Provide a high level and flexibility usage for your code.

 When do we use it?
    1- The system consists of multiple families of objects, and these families are designed to be used together
    2- Hide the complexities and how we create and compose the objects in the system


Example :
    In this example, we assume that we have an online store,
    and we have to make objects of
    Currency, Language, TaxRate and ShippingRate according to the country of the user
"""

from abc import ABC, abstractmethod


class Language(ABC):
    """ Language Abstract class """

    @abstractmethod
    def set_evnironment_language(self):
        """set environment language according to user country"""
        pass


class Currency(ABC):
    """ Currency Abstract class """

    @abstractmethod
    def update_user_currency_config(self):
        """ set user config currency according to user country"""
        pass


class FarsiLanguage(Language):

    def set_evnironment_language(self):
        print('set environment language to persian')


class EnglishLanguage(Language):

    def set_evnironment_language(self):
        print('set environment language to english')


class RialCurrency(Currency):

    def update_user_currency_config(self):
        print('set user currency config to rial')


class DollarCurrency(Currency):

    def update_user_currency_config(self):
        print('set user currency config to dollar')


class FarsiFactory:
    """ Factory Class for create all object relation to farsi . """
    """ Use Abstract Factory Design pattern for generate objects that are families """

    def get_currency(self):
        return RialCurrency()

    def get_language(self):
        return FarsiLanguage()


class EnglishFactory:
    """ Factory Class for create all object relation to english . """
    """ Use Abstract Factory Design pattern for generate objects that are families """

    def get_currency(self):
        return DollarCurrency()

    def get_language(self):
        return EnglishLanguage()


class LocalizeFactory:
    """ LocalizeFactory is used for get factory instance (Factory Design pattern) """

    def __init__(self, country):
        self.country = country

    def get_factory(self):
        factories = {
            'iran': FarsiFactory,
            'england': EnglishFactory,
        }
        return factories[self.country]()


def get_user_country():
    """Get user country from user"""
    countries = ('iran', 'england')
    user_country = input(f"Enter your country {str(countries)} :")
    if user_country not in countries:
        get_user_country()
    return user_country


if __name__ == '__main__':
    user_country_name = get_user_country()
    factory = LocalizeFactory(user_country_name).get_factory()
    currency = factory.get_currency()
    language = factory.get_language()
    print(f"Currency: {currency}")
    print(f"Language: {language}")
    currency.update_user_currency_config()
    language.set_evnironment_language()
