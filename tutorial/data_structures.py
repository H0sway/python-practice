# Data Structures Notes

# There are four data structures in Python: lists, tuples, dictionaries, and
# sets.

# Lists are a collection of data values, or a sequence of items. Think shopping
# list, or arrays in other languages. Used brackets [] and commas between each
# data point.

# Objects are instances of class types. I.e. if you have x = 5 then x is an
# object with class int (for integer). To take another example, lists are a
# class, but an individual list is an object. Objects are categorized in
# classes.

# Use list methods the same way as other languages:
# list_name.method()

# Shopping list example:

shoplist = ['apple', 'mango', 'carrot', 'banana']

print('I have', len(shoplist), 'items to purchase.')

print('These items are:', end=' ')
for item in shoplist:
    print(item, end=' ')

print('\nI also have to buy rice.')
shoplist.append('rice')
print('My shopping list is now', shoplist)

print('I will now sort my shopping list.')
shoplist.sort()
print('After sorting my shopping list is', shoplist)

print('The first item I will buy is the', shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('I bought the', olditem, 'and now my shopping list is', shoplist)
