from abc import ABC, abstractmethod

class AbstractFormatter(ABC):
    @abstractmethod
    def format(self, obj) -> str:
        pass

    @abstractmethod
    def format_all(self, objs) -> str:
        pass

