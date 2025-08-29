def reverse_string(s):
    return s[::-1]
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

print(count_vowels("Hello World"))  # Output: 3

print(reverse_string("hello"))  # Output: olleh
def are_anagrams(s1, s2):
    return sorted(s1.lower()) == sorted(s2.lower())

print(are_anagrams("listen", "silent"))  # Output: True
def word_count(sentence):
    words = sentence.lower().split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts

print(word_count("This is a test. This test is simple."))
# Output: {'this': 2, 'is': 2, 'a': 1, 'test.': 2, 'simple.': 1}
def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

print(caesar_cipher("abc", 2))  # Output: cde
import re

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))

print(validate_email("example@test.com"))  # Output: True
print(validate_email("invalid-email"))  # Output: False

