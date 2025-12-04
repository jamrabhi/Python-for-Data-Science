"""
Program, which takes a single string argument and displays the sums of :
- upper-case characters,
- lower-case characters,
- punctuation characters,
- digits,
- and spaces."""
import sys


def char_count(string: str) -> dict:
    """
    Count different types of characters in a string.
    Args:
        string (str): The input string to analyze.
    Returns:
        dict: A dictionary with counts of different character types.
    """
    char_types = {
        "char": 0,
        "upper": 0,
        "lower": 0,
        "punctuation": 0,
        "digit": 0,
        "space": 0,
    }
    punctuations = '''!"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~'''
    for char in string:
        if char.isupper():
            char_types["upper"] += 1
        elif char.islower():
            char_types["lower"] += 1
        elif char.isdigit():
            char_types["digit"] += 1
        elif char.isspace():
            char_types["space"] += 1
        elif char in punctuations:
            char_types["punctuation"] += 1
        char_types["char"] += 1
    return char_types


def main():
    """
    Main function to execute the character counting program.
    It handles command-line arguments and user input.
    """
    try:
        assert len(sys.argv) <= 2, "more than one argument is provided"

        if len(sys.argv) == 1:
            print("What is the text to count?")
            try:
                string = sys.stdin.readline()
            except KeyboardInterrupt:
                sys.exit(0)
        else:
            string = sys.argv[1]

        char_types = char_count(string)
        print(f"The text contains {char_types['char']} characters:")
        print(f"{char_types['upper']} upper letters")
        print(f"{char_types['lower']} lower letters")
        print(f"{char_types['punctuation']} punctuation marks")
        print(f"{char_types['space']} spaces")
        print(f"{char_types['digit']} digits")

    except AssertionError as err:
        print(f"AssertionError: {err}")


if __name__ == "__main__":
    main()
