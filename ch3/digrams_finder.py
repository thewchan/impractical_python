import load_dictionary
from collections import defaultdict
from pprint import pprint
import re
from itertools import permutations


name = 'tmvoordle'
word_list = load_dictionary.load('words.txt')
digrams = set()
length_name = len(name)

perms = {''.join(i) for i in permutations(name)}

for perm in perms:
    for count in range(length_name - 1):
        digram = perm[count] + perm[count + 1]
        digrams.add(digram)

digram_counts = defaultdict(int)

for word in word_list:
    for digram in digrams:
        for m in re.finditer(digram, word):
            digram_counts[digram] += 1


pprint(digram_counts)
