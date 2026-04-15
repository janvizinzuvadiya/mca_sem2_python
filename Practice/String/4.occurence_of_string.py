# 4. Word Frequency Tracker
# The Task: Count how many times each word appears in a sentence.
# Logic Goal: Understand the .split() method and how to use Dictionaries (essential for LLM tokenization).



print('-' * 50)


str = "New Delhi in New India"

a = list(str.split())
s = set(a)

print(a)

count = 0
for i in s:
    for j in a:
        if i == j:
            count += 1
    print(i,"=",count)
    count = 0
    
# print(a)


print('-' * 50)