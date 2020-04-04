import count_syllables


with open('train.txt') as in_file:
    words = set(in_file.read().split())

missing = []

for word in words:
    try:
        num_syllables = count_syllables.count_syllables(word)
        print(word, num_syllables, end='\n')
    except KeyError:
        missing.sppend(word)

print("Missing words:", missing)
