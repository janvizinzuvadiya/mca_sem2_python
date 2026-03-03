mark = int( input('Enter Marks->'))
grade=''

if (mark > 90):
    grade = 'A1 Grade'
elif (mark > 80 and mark <= 90):
    grade = 'A Grade'
elif (mark > 70 and mark <=80):
    grade = 'B1 Grade'
elif (mark > 60 and mark <= 70):
    grade = 'B Grade'
elif (mark >50 and mark <= 60):
    grade = 'Can do Better!'
else:
    grade = 'Need to Work Hard!'

print('\n\n\t Result:')
print('------------------------------------------------------')

print('\tMarks you get: \t\t', mark)
print('\t\t\t\t____________________')
print('\tPerformance: \t\t', grade)

print('------------------------------------------------------')
