from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract base class representing a character"""
    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        """Initialize a character with a name and an alive state"""
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """Set the character's alive state to false"""
        self.is_alive = False


class Stark(Character):
    """Represent a Stark character"""
    def __init__(self, first_name, is_alive=True):
        """Initialize a stark character"""
        super().__init__(first_name, is_alive)
