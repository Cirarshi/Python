# String Compression

def compress_string(s):
    compressed = []  # To store compressed parts
    count = 1  # Count of consecutive characters
    
    for i in range(1, len(s)):
        if s[i] == s[i-1]:  # If current character matches previous
            count += 1
        else:
            compressed.append(s[i-1] + str(count))  # Append character and count
            count = 1  # Reset the count
    compressed.append(s[-1] + str(count))  # Append the last character and count
    
    compressed_string = ''.join(compressed)
    return compressed_string if len(compressed_string) < len(s) else s

# Testing the function
print(compress_string("aaabbcccaaaaaddddddddda"))  # Output: 'a3b2c3'
