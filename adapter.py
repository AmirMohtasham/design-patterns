"""
Adapter Design Pattern (Structural)
The Adapter acts as a wrapper between two objects.
It catches calls for one object and transforms them to format and interface recognizable by the second object.
In simpler terms:
   Allows communication with incompatible objects.

It is usually used for the purpose of making it possible
to use the current class without changing the original code.

Example :
    Suppose we receive news from several external services and need to save it in a file.
    The type of data that is returned is as follows:
        FOXNews => Json
        BBCNews => Json
        CNNNews => xml

 """

from abc import ABC, abstractmethod


class SourceNews(ABC):
    @abstractmethod
    def get_data(self):
        """ Get data from source news """
        pass

    def save_data_to_file(self):
        """ store json data to file """
        print("Store json data to file")

    def start(self):
        self.get_data()
        self.save_data_to_file()


class FoxNews(SourceNews):
    """ FoxNews data is json """

    def get_data(self):
        print("get data(json) from fox news")


class BBCNews(SourceNews):
    """ BBCNews data is json """

    def get_data(self):
        print("get data(json) from bbc news")


class CNNNews(SourceNews):
    """ CNNNews data is xml """

    def get_data(self):
        print("get data(xml) from cnn news")


class JsonAdapter:
    """
    write json adapter that convert xml to json that compatible to SourceNews class
    If we not use adapter pattern, we should change the SourceNews class for support xml
    and if we change the SourceClass, We are broken the Open/Close Principle
    """

    def __init__(self, obj):
        self.obj = obj

    def convert_xml_to_json(self):
        print('Convert XML to JSON')
        return self.obj


def main():
    # Json
    FoxNews().start()
    BBCNews().start()

    # XML
    JsonAdapter(CNNNews()).convert_xml_to_json().start()


if __name__ == '__main__':
    main()
