# 1. The Palindrome Checker
# The Task: Check if a string reads the same forward and backward (e.g., "radar").
# Logic Goal: Understand string slicing and comparison.

print('-' * 50)


str = input('Enter String->')
rev = str[::-1]
if(str == rev):
    print('The String is Palindrome')
else:
    print('XXXXXXXX')

print('-' * 50)
