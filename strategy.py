"""
Strategy Design Pattern (Behavioral)

This allows us to specify how to execute the code at runtime.
Ability to select an algorithm at runtime.

If we can do a task in several ways and the desired method is selected at runtime,
 Strategy Pattern will be a good choice.

In this Example :
 We want to sort the data list, and we have several algorithms for
 sorting and according to the size of the data we have to choose one algorithm for sorting
"""

from abc import ABC, abstractmethod


class Sort:
    def __init__(self, data):
        self.data = data
        if len(data) > 100:
            self.sorter = QuickSortStrategy
        else:
            self.sorter = BubbleSortStrategy

    def start(self):
        self.sorter().sort(self.data)


class SortStrategy(ABC):

    @abstractmethod
    def sort(self, data):
        pass


class BubbleSortStrategy(SortStrategy):

    def sort(self, data):
        print('sort data by bubble sort strategy ')


class QuickSortStrategy(SortStrategy):

    def sort(self, data):
        print('sort data by quick sort strategy ')


if __name__ == '__main__':
    data1 = [i for i in range(1, 20)]
    Sort(data1).start()

    data2 = [i for i in range(1, 200)]
    Sort(data2).start()
