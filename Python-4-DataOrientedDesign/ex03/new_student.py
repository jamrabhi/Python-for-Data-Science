import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Generate a random 15-character string of lowercase letters."""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """Student dataclass containing student information."""
    name: str
    surname: str
    active: bool = True
    id: str = field(init=False, default_factory=generate_id)
    login: str = field(init=False)

    def __post_init__(self):
        """Initialize the login attribute based on name and surname."""
        self.login = self.name[0].upper() + self.surname.lower()
