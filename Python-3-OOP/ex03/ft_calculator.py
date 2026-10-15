class calculator:
    """Calculator class."""
    def __init__(self, vector) -> None:
        """Initialize the calculator class."""
        self.vector = vector

    def __add__(self, object) -> None:
        """Add x object to the vector"""
        self.vector[:] = [object + x for x in self.vector]
        print(self.vector)

    def __mul__(self, object) -> None:
        """Multiply x object to the vector"""
        self.vector[:] = [object * x for x in self.vector]
        print(self.vector)

    def __sub__(self, object) -> None:
        """Substract x object to the vector"""
        self.vector[:] = [x - object for x in self.vector]
        print(self.vector)

    def __truediv__(self, object) -> None:
        """Divide x object to the vector"""
        try:
            self.vector[:] = [x / object for x in self.vector]
            print(self.vector)

        except ZeroDivisionError as err:
            print(f"ZeroDivisionError : {err}")
