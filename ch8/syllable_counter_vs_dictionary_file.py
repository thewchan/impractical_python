from collections import defaultdict
from random import sample
import count_syllables
import load_dictionary


word_list = load_dictionary.load('words.txt')
dictionary_sylls = defaultdict(int)

for word in word_list:
    try:
        num_syllables = count_syllables.count_syllables(word)
        dictionary_sylls[word] = num_syllables
    except KeyError:
        pass

while True:
    item_to_display = input("Enter the number of words to display: ")
    try:
        item_to_display = int(item_to_display)
    except ValueError:
        print("Please enter a number!")
        continue
    break

for item in range(item_to_display):
    word = sample(dictionary_sylls.items(), 1)
    print(word[0][0], word[0][1])
