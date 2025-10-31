import sys


def main():
    """Make a program that takes a string as an argument and encodes it into
    Morse Code.
    • The program supports space and alphanumeric characters
    • An alphanumeric character is represented by dots . and dashes -
    • Complete morse characters are separated by a single space
    • A space character is represented by a slash /
    You must use a dictionary to store your morse code.
    If the number of arguments is different from 1, or if the type of any
    argument is wrong, the program prints an AssertionError."""

    NESTED_MORSE = {
        'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',
        'E': '.',     'F': '..-.',  'G': '--.',   'H': '....',
        'I': '..',    'J': '.---',  'K': '-.-',   'L': '.-..',
        'M': '--',    'N': '-.',    'O': '---', 'P': '.--.',
        'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
        'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',
        'Y': '-.--',  'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---', '3': '...--',
        '4': '....-', '5': '.....', '6': '-....', '7': '--...',
        '8': '---..', '9': '----.', ' ': '/'
    }

    try:
        err_msg = "the arguments are bad"

        assert len(sys.argv) == 2, err_msg

        text = sys.argv[1].upper()

        assert all(c.isalnum() or c == ' ' for c in text), err_msg

        morse_code = ' '.join(NESTED_MORSE[c] for c in text)
        print(morse_code)

    except AssertionError as err:
        print(f"AssertionError: {err}")


if __name__ == "__main__":
    main()
