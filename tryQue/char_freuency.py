# count frequency of characters in a string

def char_frequency(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

print(char_frequency("hello"))

from collections import Counter
result = Counter("hello")
print(result)