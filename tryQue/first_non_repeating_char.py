# first non repeating character

def first_non_repeating_char(s):
    count = {}
    for char in s:
        count[char] = count.get(char,0)+1
    for char in s:
        if count[char] == 1:
            return char
    return None

print(first_non_repeating_char("kiss"))