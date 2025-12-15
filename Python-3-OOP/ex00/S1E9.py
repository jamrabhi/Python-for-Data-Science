from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract base class"""
    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        """Docstring for Constructor"""
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """Docstring for Method"""
        self.is_alive = False


class Stark(Character):
    """Stark class based on Character ABC"""
    def __init__(self, first_name, is_alive=True):
        """Docstring for Constructor"""
        super().__init__(first_name, is_alive)
