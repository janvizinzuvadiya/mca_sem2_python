dict = {

    'program' : 'MCA',
    'Department' : 'CS & IT',
    'Semester' : 2,
    'Roll no' : 64,
    'Division' : 'Y1',
    'Batch' : 'Y',
    'Enrollment_no' : 34323221,
    'Registration_no' : 46278366453 ,
    'Course' : 'Python',
    'Date' : '20-2-2026'
}
print('-----------------------------------------------------------')
print('Here are the Details of the student:')
for i in dict:
    print(i,"\t: \t ",dict[i])
print('-----------------------------------------------------------')
print('\n\nType of The Holder:')
print(type(dict))

print('\nEnrollment no:  ',end=" ")
print(dict["Enrollment_no"])

print('\nUpdated Enrollment no:  ',end=" ")
dict['Enrollment_no'] = 34232
print(dict["Enrollment_no"])

print('\nOnly Values: ')
print(dict.values())



