from typing import Any


def callLimit(limit: int):
    """Decorator to limit the number of times a function can be called."""
    count = 0

    def callLimiter(function):
        """Takes the function to be decorated and returns the wrapper."""
        def limit_function(*args: Any, **kwds: Any):
            """Wrapper that checks the call limit before executing."""
            nonlocal count

            if count < limit:
                count += 1
                return function(*args, **kwds)
            else:
                print(f"Error: {function} call too many times")

        return limit_function

    return callLimiter
