import sys

m1 = int(sys.argv[1])
m2 = int(sys.argv[2])
m3 = int(sys.argv[3])
m4 = int(sys.argv[4])
m5 = int(sys.argv[5])

total = m1 + m2 + m3 + m4 + m5
per = (total * 100) / 500

print('\n\n\tResult:')
print('------------------------------------------------------')

print('\tMarks of subject 1: \t \t', m1)
print('\tMarks of subject 2:\t +\t', m2)
print('\tMarks of subject 3:\t +\t', m3)
print('\tMarks of subject 4:\t +\t', m4)
print('\tMarks of subject 5:\t +\t', m5)

print('_____________________________________________')
print('\t Total\t\t\t =\t', total,"/500")
print('\t Percentage\t\t =\t', per,"%")

print('------------------------------------------------------')

