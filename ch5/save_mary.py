from random import randint
from math import ceil
import load_dictionary

names = load_dictionary.load('supporters.txt')
names = set(names)
first_cipher_word = names.pop()
plain_text = 'Give your word and we rise'
plain_text = ''.join(plain_text.lower().split())

cipher_text = []
used_name = set()
phrase_len = len(plain_text)
counter = 0
encryption_pos = 0
stuart_position = randint(1, ceil(phrase_len / 2))
while True:
    jacob_position = randint(1, ceil(phrase_len / 2))
    if jacob_position != stuart_position:
        break
cipher_text.append(first_cipher_word.title())
used_name.add(first_cipher_word)

for letter in plain_text:
    if counter % 2 != 0:
        for name in names:
            if name[2] == plain_text[encryption_pos]:
                if name in used_name:
                    continue
                cipher_text.append(name.title())
                used_name.add(name)
                counter += 1
                encryption_pos += 1
                break

    elif counter % 2 == 0:
        for name in names:
            if name[1] == plain_text[encryption_pos]:
                if name in used_name:
                    continue
                cipher_text.append(name.title())
                used_name.add(name)
                counter += 1
                encryption_pos += 1
                break

cipher_text.insert(stuart_position, 'Stuart')
cipher_text.insert(jacob_position, 'Jacob')

print("Your majesty, below we humbly present a list of your loyal supporters' "
    "names:\n")
print(*cipher_text, sep='\n')
