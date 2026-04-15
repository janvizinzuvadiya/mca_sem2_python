# 3. Remove Duplicate Characters
# The Task: Remove all duplicate characters from a string so that every character appears only once 
# (e.g., "programming" becomes "progamin").
# Logic Goal: Learn to use auxiliary data structures like Sets or temporary lists to track seen items.


print('-' * 50)


str = "Programming"

result = ""
 
for i in str:
    if i in result:
        pass
    else:
        result += i

print(result)




print('-' * 50)
