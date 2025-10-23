import sys


def char_count(string: str) -> dict:
    """
    Function that takes a single string argument and displays the sums of its
     upper-case characters, lower-case characters, punctuation characters,
     digits and spaces.
    """
    charTypes = {
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
            charTypes["upper"] += 1
        elif char.islower():
            charTypes["lower"] += 1
        elif char.isdigit():
            charTypes["digit"] += 1
        elif char.isspace():
            charTypes["space"] += 1
        elif char in punctuations:
            charTypes["punctuation"] += 1
        charTypes["char"] += 1
    return charTypes


def main():
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

        charTypes = char_count(string)
        print(f"The text contains {charTypes['char']} characters:")
        print(f"{charTypes['upper']} upper letters")
        print(f"{charTypes['lower']} lower letters")
        print(f"{charTypes['punctuation']} punctuation marks")
        print(f"{charTypes['space']} spaces")
        print(f"{charTypes['digit']} digits")

    except AssertionError as err:
        print(f"AssertionError: {err}")


if __name__ == "__main__":
    main()
