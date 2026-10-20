def square(x: int | float) -> int | float:
    """Return the square of a number."""
    return (x * x)


def pow(x: int | float) -> int | float:
    """Return the pow of a number."""
    return (x ** x)


def outer(x: int | float, function) -> object:
    """Return an inner function that applies function iteratively."""
    count = 0

    try:
        if not isinstance(x, (int, float)):
            raise AssertionError("x is not int or float")

        def inner() -> float:
            """Apply the function and return the updated value."""
            nonlocal count, x
            count += 1
            x = function(x)
            return x

    except AssertionError as err:
        print(f"Error : {err}")
        return None

    return inner
