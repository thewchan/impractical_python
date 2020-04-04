"""
Decrypt a path through a Union Route Cipher.

Designed for a whole-word transposition ciphers with variable rows & columns.
Assumes encryption began at either top or bottom of a column.
Key indicates the orders to read columns and the direction to traverse.
Negative column numbers mean start at bottom and read up.
Positive column numbers mean start at top & read down.

Example below is for 4x4 matrix with key -1 2 -3 4.
Note "0" is not allowed.
Arrows show encryption route; for negative key values read UP.

  1   2   3   4
 ___ ___ ___ ___
| ^ | | | ^ | | | MESSAGE IS WRITTEN
|_|_|_v_|_|_|_v_|
| ^ | | | ^ | | | ACROSS EACH ROW
|_|_|_v_|_|_|_v_|
| ^ | | | ^ | | | IN THIS MANNER
|_|_|_v_|_|_|_v_|
| ^ | | | ^ | | | LAST ROW IS FILLED WITH DUMMY WORDS
|_|_|_v_|_|_|_v_|
START        END

Required inputs - a text message, # of columns, # of rows, key string

Prints translated plaintext
"""
import sys
from itertools import permutations

# =============================================================================
# User INPUT:

# the string to be decrypted (type or paste between triple - quotes):
ciphertext = """REST TRANSPORT YOU GODWIN VILLAGE ROANOKE WITH ARE YOUR IS
JUST SUPPLIES FREE SNOW HEADING TO GONE TO SOUTH FILLER"""

# number of columns in the transposition matrix:
COLS = 4

# number of rows in the transposition matrix:
ROWS = 5

# key with spaces between numbers; negative to read UP column (ex = -1 2 -3 4):
#key = """ -1 2 -3 4 """

# END OF USER INPUT - DO NOT EDIT BELOW THIS LINE!
# =============================================================================


def main():
    """Run program and print decrypted plaintext."""
    while True:
        key_len = input("Enter length of key: ")
        try:
            key_len = int(key_len)
        except ValueError:
            print("Please enter a number.")
            continue
        break
    print(f"\nCiphertext = {ciphertext}")
    print(f"Trying {COLS} columns")
    print(f"Trying {ROWS} rows")

    # split elements into words, not letters
    cipherlist = list(ciphertext.split())
    validate_col_row(cipherlist)
    keys = generate_keys(key_len)
    for key in keys:
        print(f"\nUsing key: {key}: ")
        translation_matrix = build_matrix(key, cipherlist)
        plaintext = decrypt(translation_matrix)

        print(f"Plaintext = {plaintext}\n")
    print(f"\nPossible numbers of decryption: {len(keys)}")


def generate_keys(key_len):
    """Generate possible key combinations given key length."""
    positive_integers = list(range(key_len + 1))
    positive_integers.pop(0)
    print(
        "Possible key values (not including direction): ",
        *positive_integers,
        )
    negative_integers = [-1 * x for x in positive_integers]
    all_integers = positive_integers + negative_integers
    raw_perms = list(permutations(all_integers, key_len))
    keys = []

    for perm in raw_perms:
        abs_perm = [abs(x) for x in perm]
        set_perm = set(abs_perm)
        if len(set_perm) == len(perm):
            keys.append(perm)

    return keys


def validate_col_row(cipherlist):
    """Check that input columns & rows are valid vs. message length."""
    factors = []
    len_cipher = len(cipherlist)
    for i in range(2, len_cipher):  # range excludes 1-column ciphers
        if len_cipher % i == 0:
            factors.append(i)
    print(f"\nLength of cipher = {len_cipher}")
    print(f"Acceptable column/row values include: {factors}")
    print()
    if ROWS * COLS != len_cipher:
        print(
            "\nError - Input columns & rows not factors of length of cipher."
            " Terminating program."
            )
        sys.exit(1)


def build_matrix(key_int, cipherlist):
    """Turn every n items in a list into a new item in a list of lists."""
    translation_matrix = [None] * COLS
    start = 0
    stop = ROWS
    for k in key_int:
        if k < 0:   # read bottom-to-top of column
            col_items = cipherlist[start:stop]
        elif k > 0:     # read top-to-bottom of colunn
            col_items = list((reversed(cipherlist[start:stop])))
        translation_matrix[abs(k) - 1] = col_items
        start += ROWS
        stop += ROWS
    return translation_matrix


def decrypt(translation_matrix):
    """Loop through nested list popping off last item to a string."""
    plaintext = ''
    for i in range(ROWS):
        for matrix_col in translation_matrix:
            word = str(matrix_col.pop())
            plaintext += word + ' '
    return plaintext


if __name__ == '__main__':
    main()
