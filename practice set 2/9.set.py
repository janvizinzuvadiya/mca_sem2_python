fruits = {'apple','banana','cherry','dragon-fuit','fig','fig'}

print('\n\n---------------------------------------------------------------------')
print('\nSet of Fruit Juice We Have:')
for i in fruits:
    print('->',i)

print('\nAdded 2 New Flavours:')
fruits.update(['grapes','hibiscus'])
print(fruits)

print('\nSeasonal Flavours:[removed apple]')
fruits.remove('apple')
print(fruits)

print('\n[also removed banana, fig]')
fruits.difference_update('banana','fig')
print(fruits)


print('----------------------------------------------------------------------')

