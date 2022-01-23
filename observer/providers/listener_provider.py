from abc import ABC, abstractmethod


class ListenerProvider(ABC):
    @abstractmethod
    def handle(self, *args, **kwargs):
        pass
