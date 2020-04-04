"""
pseudo-code:

etaoin_freq = 0.50

read cipher file to string

use counter to count occurrence

find occurrence of e, t, a, o, i, and n

sum

compare to etaoin_freq, if >, transposition cipher, if < substitution cipher

"""
from collections import Counter

ETAOIN_FREQ = 0.50
ETAOIN = 'ETAOIN'

file = input("Enter cipher file name/path: ")
with open(file) as f:
    cipher_text = f.read()

cipher_len = len(cipher_text)
cipher_counts = Counter(cipher_text)
etaoin_counts = 0
print(cipher_text)

for letter in ETAOIN:
    try:
        etaoin_counts += cipher_counts[letter]
        print(f"{letter}: {cipher_counts[letter]}")
    except KeyError:
        continue

cipher_etaoin_freq = etaoin_counts / cipher_len

print(f"Cipher length: {cipher_len}")
print(f"Frequency of ETAOIN in cipher = {cipher_etaoin_freq}%")
if cipher_etaoin_freq >= ETAOIN_FREQ:
    print("Cipher mostly likely a transposition cipher.")
else:
    print("Cipher most likely a substitution cipher.")
