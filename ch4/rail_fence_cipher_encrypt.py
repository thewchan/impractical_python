r"""Encrypt a Civi War 'rail fence' type cipher.

This is for a "2-rail" fence cipher for short messags.

Example text to encrypt:    'Buy more Maine potatoes'

Rail fence style:   B Y O E A N P T T E
                     U M R M I E O A O S

Read zigzag:        \/\/\/\/\/\/\/\/\/\/

Encrypted:  BYOEA NPTTE UMRMI EOSOS

"""
# ----------------------------------------------------------------------------
# User INPUT:

# the string to be encrypted (paste between quotes):
plaintext = """Let us corss over the river and rest uder the shade of the trees
"""


# END OF USER INPUT - DO NOT EDIT BELOW THIS LINE!
# ----------------------------------------------------------------------------


def main():
    """Run program to encrypt message using 2-rail rail fence cipher."""
    message = prep_plaintext(plaintext)
    rails = build_rails(message)
    encrypt(rails)


def prep_plaintext(plaintext):
    """Remove spaces & leading/trailing white space."""
    message = "".join(plaintext.split())
    message = message.upper()   # convention for ciphertext is uppercase
    print(f"\nplaintext = {plaintext}")
    return message


def build_rails(message):
    """Build strings with every other letter in a message."""
    evens = message[::2]
    odds = message[1::2]
    rails = evens + odds
    return rails


def encrypt(rails):
    """Split letters in ciphertext into chunks of 5 & join to make strings."""
    ciphertext = ' '.join([rails[i:i+5] for i in range(0, len(rails), 5)])
    print(f"ciphertext = {ciphertext}")


if __name__ == '__main__':
    main()
