"""
State Design Pattern (Behavioral)

Allows an object to change the behavior when its internal state changes.

"""

from abc import ABC, abstractmethod


class IState(ABC):

    @property
    @abstractmethod
    def allowed(self):
        pass


class Archive(IState):
    allowed = []


class Done(IState):
    allowed = [Archive]


class InProgress(IState):
    allowed = [Done]


class New(IState):
    allowed = [InProgress]


class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.to_state = None
        self.current = New

    def change_state(self, to_state):
        if to_state.__class__ in self.current.allowed:
            self.to_state = to_state
            self.current = to_state
            print(f'Successfully moved from {self.current.__class__} to {to_state.__class__}')
        else:
            print(f'Not Allow move direct from {self.current.__class__} to {to_state.__class__}')

    def __str__(self):
        return f"{self.title} - {self.to_state.__class__}"


if __name__ == '__main__':
    task = Task('Task#1', 'Fix Bug')
    task.change_state(InProgress())
    task.change_state(Done())
