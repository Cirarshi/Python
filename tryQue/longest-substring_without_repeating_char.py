##  Longest Substring Without Repeating Characters

def longest_substring_without_repeating(s):
    char_set = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        print(char_set)
        max_length = max(max_length, right - left + 1)  
        print(f"right - {right}")
        print(f"left - {left}")

    return max_length

print(longest_substring_without_repeating("abcabcbb"))