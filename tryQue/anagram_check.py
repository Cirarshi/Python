## Anagram check

from collections import Counter
s1 = 'silent'
s2 = 'listen'

print(Counter(s1))
print(Counter(s2))
print(Counter(s1) == Counter(s2))

if sorted(s1) == sorted(s2):
    print("Anaragm")
else:
    print("Not Anaragm")