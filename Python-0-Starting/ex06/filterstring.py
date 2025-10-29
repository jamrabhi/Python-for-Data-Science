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


def main():
    try:
        assert len(sys.argv) == 3, "the arguments are bad"

        S = sys.argv[1]
        words = S.split()

        try:
            N = int(sys.argv[2])
        except ValueError:
            raise AssertionError("the arguments are bad")

        filteredstring = ft_filter(lambda word: len(word) > N, words)

        result = [word for word in filteredstring]
        print(result)

    except AssertionError as err:
        print(f"AssertionError: {err}")


if __name__ == "__main__":
    main()
