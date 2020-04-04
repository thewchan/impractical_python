import load_dictionary
from itertools import permutations


word_list = load_dictionary.load('words.txt')

starting_words = input("Enter phrase: ")
starting_words = ''.join(starting_words.lower().split())
length = len(starting_words)
perms = {''.join(i) for i in permutations(starting_words)}

filtered_word_list = []
for word in word_list:
    if len(word) <= length:
        filtered_word_list.append(word)

for perm in perms:
    temp = perm
    anagram_phrase_flag = True
    while len(temp) > 0:
        for word in filtered_word_list:
            if temp.startswith(word):


