income = int(input('Enter Income->'))
tax = 0
charge = 0

if (income < 800000):
    tax = 0
    charge = 0
elif (800000 < income and income < 1000000):
    tax = (income * 15) / 100
    charge = 15
elif (1000000 < income and income < 2000000):
    tax = (income * 20) / 100
    charge = 20
else:
    tax = (income * 30) / 100
    charge = 30

income_after_tax = income - tax

print('\n\n\t Tax Slab:')
print('------------------------------------------------------')

print('\tIncome: \t\t\t\t', income)
print('\tTax on Income:\t[',charge,'%]\t\t * \t', charge)
print('_________________________________________________')
print('\t Total Income after Tax\t\t =\t', income_after_tax)

print('------------------------------------------------------')
