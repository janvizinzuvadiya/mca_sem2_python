# 2. Vowel & Consonant Counter
# The Task: Given a string, count how many vowels (a, e, i, o, u) and consonants are present.
# Logic Goal: Practice looping and membership testing (if char in "aeiou").

print('-' * 50)

str = input('Enter String->')

temp = str.lower()

vowel = 0
constant = 0

for i in temp:
    if(i in 'aeiou'):
        vowel += 1
    else:
        constant += 1


print("count of Vowel : ",vowel)
print("count of Constant : ",constant)

print('-' * 50)
