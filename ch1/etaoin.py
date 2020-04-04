"""
This program break down user input text and display letter usage frequency as
a bar chart.
"""

import string


from pprint import pprint
from collections import defaultdict


def main():
    """Main function of the program."""
    print(
        "This program will count alphabet used in your input and display them"
        "in a bar chart."
        )
    paragraph = input("Enter sentence(s): ")
    paragraph = paragraph.lower().replace(" ", "")
    bar_chart = defaultdict(list)

    for letter in paragraph:
        if letter in string.punctuation:
            continue
        bar_chart[letter].append(letter)

    pprint(bar_chart, width=110)


if __name__ == '__main__':
    main()
