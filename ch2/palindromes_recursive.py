"""Find palindromes (letter palingrams) in a dictionary file."""
from math import ceil

import load_dictionary


word_list = load_dictionary.load('words.txt')
pali_list = []

for word in word_list:
    if len(word) > 1:
        palindrome_flag = True
        half_length = ceil(len(word) / 2)
        temp_word = word
        for position in range(half_length):
            if temp_word[0] == temp_word[-1]:
                temp_word = temp_word[1:-1]
            else:
                palindrome_flag = False
                break
        if palindrome_flag is True:
            pali_list.append(word)


print(f"\nNumber of palindromes found = {len(pali_list)}")
print(*pali_list, sep='\n')
