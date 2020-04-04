"""
Pseudo-code

ask for length of key
initiate possible integers
get sum of positive integers
get negative integers
merge into 1 string
get permutation
loop through permutation and sum up abs values
eliminate those with sum not equal to sum of positive integers
print out list of tuples
"""
from itertools import permutations
while True:
    key_len = input("Enter length of key: ")
    try:
        key_len = int(key_len)
    except ValueError:
        print("Please enter a number.")
        continue
    break

positive_integers = list(range(key_len + 1))
positive_integers.pop(0)
print(
    "Possible key values (not including direction): ",
    *positive_integers,
    )
negative_integers = [-1 * x for x in positive_integers]
all_integers = positive_integers + negative_integers
raw_perms = list(permutations(all_integers, key_len))
filtered_perms = []

for perm in raw_perms:
    abs_perm = [abs(x) for x in perm]
    set_perm = set(abs_perm)
    if len(set_perm) == len(perm):
        filtered_perms.append(perm)

print("Valid key combinations:\n", *filtered_perms, sep='\n')
print(f"Number of valid key combinations: {len(filtered_perms)}")
