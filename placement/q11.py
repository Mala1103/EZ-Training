'happy fathers day'
'''extract the vowel which has max count'''

text = "happy fathers day"
vowel_counts = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

for char in text:
    if char in vowel_counts:
        vowel_counts[char] += 1

max_vowel = max(vowel_counts, key=vowel_counts.get)

print(f"The vowel with the maximum count is '{max_vowel}' with a count of {vowel_counts[max_vowel]}.")

        