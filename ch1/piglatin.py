"""Transform a word into "Pig Latin"."""


def main():
    """
    Take user input word, check that it is a single word, and return
    a "Pig Latin"-ized word.
    """
    vowels = 'aeiouy'
    print("Welcome to the Pig Latin Transformer(tm)!!!!")
    while True:
        word = input("Enter a single word: ")
        if " " in word:
            print("Please only enter a SINGLE word.")
            continue

        if word[0].lower() in vowels:
            pig_latin_word = word + "way"
        else:
            pig_latin_word = word[1:] + word[0] + "ay"

        print(f"Pig Latin-ized word: {pig_latin_word.lower()}")

        try_again = input("\n\nTry again? (Press Enter else n to quit)\n")

        if try_again.lower() == "n":
            break

    input("\nThanks for playing. Press enter to exit.")


if __name__ == "__main__":
    main()
