sal = int(input('Enter Basic Salary->'))

TA = (sal * 4) / 100
DA = (sal * 30) / 100
HRA = (sal * 15) / 100

if(sal>10000):
    grsal = (sal + TA + DA + HRA) - 2000
else:
    grsal = sal + TA + DA + HRA

TAX = (grsal * 3) / 100
PF = (grsal * 12) / 100

netsal = grsal - (TAX + PF)

print('\n\n\tNet Salary:')
print('------------------------------------------------------')

print('\t Basic Salary: \t\t\t\t', sal)
print('\t Travel Allowance [4%]:\t\t +\t', TA)
print('\t Dearness Allowance [30%]:\t +\t', DA)
print('\t House rent allowance [15%]:\t +\t', HRA)
print('\t Gross Salary: \t\t\t = \t', grsal)
print('\t\t\t\t_____________________')
print('\t TAX [3%]:\t\t\t -\t', TAX)
print('\t Providant Fund [12%]:\t\t -\t', PF)
print('______________________________________________________')
print('\t Net Salary \t\t\t =\t', netsal)

print('------------------------------------------------------')
