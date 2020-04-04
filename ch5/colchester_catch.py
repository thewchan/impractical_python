import sys


with open('colchester_message.txt') as f:
    cipher_text = f.read()

print(cipher_text)
cipher_text = cipher_text.lower().split()
print(cipher_text)


while True:
    try_length = input("Enter cipher key to try (an integer): ")
    try:
        try_length = int(try_length)
    except ValueError:
        print("Please enter a number.")
        continue
    break

decrypted_text = ''
counter = 0

try:
    decrypted_text += cipher_text[0][try_length - 1]
except IndexError:
    print("Cipher key too high for length of words in cipher.")
    sys.exit(1)

for word in cipher_text:
    if counter == 0:
        counter += 1
        print(word)
    elif counter % try_length == 0:
        try:
            decrypted_text += word[try_length - 1]
            counter += 1
            print(word)
        except IndexError:
            print("Cipher key too high for length of words in cipher.")
            counter += 1
    else:
        counter += 1

print(decrypted_text)
