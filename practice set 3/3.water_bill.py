lit = int(input('Enter Water amount in Litters->'))
charge = 0

if(lit < 90):
    charge = 0
elif(lit > 90 and lit < 150):
    charge = 2
elif(lit > 150 and lit < 250 ):
    charge = 5
else:
    charge = 10

bill = lit * charge

print('\n\n\t Total Bill:')
print('------------------------------------------------------')

print('\tUsage of Water in Litres: \t\t', lit)
print('\tCharges Applied per litre: \t * \t', charge)
print('_________________________________________________')
print('\t Total bill\t\t\t =\t', bill)

print('------------------------------------------------------')
