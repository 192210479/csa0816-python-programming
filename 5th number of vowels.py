def count_vowels(string):
    vowels = 'aeiouAEIOU'
    vowel_count = 0
    for char in string: 
        if char in vowels:
            vowel_count += 1
    return vowel_count
string = "krishna"
print("number of vowels in the string:", count_vowels(string))
