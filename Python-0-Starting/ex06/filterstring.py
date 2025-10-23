"""Program accepts two arguments: a string(S), and an integer(N).
The program should output a list of words from S that have a length greater
than N.
• Words are separated from each other by space characters.
• Strings do not contain any special characters. (Punctuation or invisible)
• The program must contain at least one list comprehension expression and one
lambda.
• If the number of argument is different from 2, or if the type of any argument
is wrong, the program prints an AssertionError."""

import sys
from ft_filter import ft_filter


def filterstring(S: str, N: int):
    if (len(S) > N):
        return S


def main():
    try:
        assert len(sys.argv) == 3, "the arguments are bad"
        value = int(sys.argv[2])
        filtered = ft_filter(filterstring(sys.argv[1], value), sys.argv[1])

        print(list(filtered))

    except AssertionError as err:
        print(f"Assertion error: {err}")


if __name__ == "__main__":
    main()
