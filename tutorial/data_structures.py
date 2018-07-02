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

# Tuples:

# Tuples are used to hold together multiple objects. Unlike lists they cannot
# be changed (are immutable).
#
# Example:

# Parenthesis are optional with tuples, but use them anyway to better specify
# when you are using a tuple
zoo = ('python', 'elephant', 'penguin')
print('The number of animals in the zoo is', len(zoo))

new_zoo = ('monkey', 'camel', zoo)
print('The amount of cages in the zoo is', len(new_zoo))
print('The animals in the zoo are', new_zoo)
print('The animals brought in from the old zoo are', new_zoo[2])
print('The last animal brought into the new zoo is', new_zoo[2][2])
print('The number of animals in the new zoo is', len(new_zoo)-1+len(new_zoo[2]))

# Dictionary:
#
# A dictionary stores pairs of keys and values. You can call on the values by
# using the key. Keys should be unique and using an immutable data type (i.e. a
# string) while values can use whatever data type you want.

# Example:

ab = {
    'Swaroop': 'swaroops@swaroopch.com',
    'Larry': 'larry@wall.org',
    'Matsumoto': 'matz@ruby-lang.org',
    'Spammer': 'spammer@hotmail.com'
}

print("Swaroop's address is", ab['Swaroop'])

del ab['Spammer']
print('\nThere are {} contacts in the address-book\n'.format(len(ab)))

for name, address in ab.items():
  print('Contact {} at {}'.format(name, address))

ab['Guido'] = 'guido@python.org'

if 'Guido' in ab:
  print("\n Guido's address is", ab['Guido'])

# Sequences:
#
# Lists, tuples and dictionaries are all types of sequences. What defines a
# sequence is the ability to 'slice' it, or fetch one specific item in the
# sequence. This requires the sequence to have an index starting at 0 (as is
# true with every other programming language I've learned). Use negative
# numbers to start from the end of the sequence.






































