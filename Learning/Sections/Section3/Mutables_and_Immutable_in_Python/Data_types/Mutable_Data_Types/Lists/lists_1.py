#Lists

ingrredients = ['water', 'milk', 'black tea']
print(f'Ingredients: {ingrredients}') # the output will print, water, milk and milk tea
#in the given list, lets say if we forgot to add some elements like, sugar, we can add it, but it was tuple, we can not add

#for example
#append
ingrredients.append ('sugar')# append is used to add new items
#append always add the elements at the last

print(f'Ingredients: {ingrredients}')# after appeneding , it will print sugar as well

#remove
ingrredients.remove('water')# used to remove the items from the list
print(f'Ingredients: {ingrredients}')# the output will be, milk, blcak tea and sugar, it will reomve water


#extend
spice_options = ['ginger', 'cardamom']#list named spice_options has ginger and cardmom
chai_ingredinets = ['water', 'milk']#list named chai_ingrediets has water and milk
chai_ingredinets.extend(spice_options)# now in chai_ingredients list, spice_options has been exteneded, this means, all the items from spice_options will be added to chai_ingredients
#extend always add the elements at the last

print(f'Chai ingredients: {chai_ingredinets}')#output will be water, milk, ginger and cardomom

#insert
chai_ingredinets.insert(2, 'black tea')
#so here black tea will be inserted at index 2, but from the previous print statement, we have water, milk, ginger and cardamom
#that means , ginger is at index 2, so now at index 2 black tea will be added, and ginger will move to the next index
#so the final output will be like, water, milk, black tea, ginger and cardamom
print(f'Chai indredients: {chai_ingredinets}') #output Chai indredients: ['water', 'milk', 'black tea', 'ginger', 'cardamom']


#pop :it will remoeve the last added element from the list
#ginger and cardamom were added in chai ingredints by meging it with spice_options, so pop() will remove the last element which is cardamom
last_added = chai_ingredinets.pop()# cardamom will be removed
print(f'{last_added}')# output :Chai indredients: ['water', 'milk', 'black tea', 'ginger', 'cardamom'] cardamom

print(f'Chai ingredients: {chai_ingredinets}')#output Chai ingredients: ['water', 'milk', 'black tea', 'ginger'], because caraamom was removed

#reverse
chai_ingredinets.reverse()# reverse , will print all the elments in reverse order, it will reverse words only, not characters in reverse order
print(f'chai ingredients: {chai_ingredinets}')# output will be :chai ingredients: ['ginger', 'black tea', 'milk', 'water']

#sorting
chai_ingredinets.sort()# it will sort the items in order with alphabet of every element
print(f'chai ingredients: {chai_ingredinets}')# the output will be : chai ingredients: ['black tea', 'ginger', 'milk', 'water']


sugar_levels = [1, 2, 3, 4, 5]# new list named sugar_levels with values upto 5 starging from 1
print(f'Maximum sugar level: {max(sugar_levels)}')# this will print the maximum value present in the list:output: Maximum sugar level: 5

print(f'Minimum sugar level: {min(sugar_levels)}')# this will print the min8imum value present in the list:output: Minimum sugar level: 1

#operator overloading
base_liquid = ['water', 'milk']# new list
extra_flavor = ['ginger']# new list

full_liquid_mix = base_liquid + extra_flavor# base liquid and extra flavour will be added together in the new variable full_liquid mix
print(f'full liquid mix : {full_liquid_mix}')# output will be : full liquid mix : ['water', 'milk', 'ginger']


strong_brew = ['black tea'] * 3# new list created with name strong brew and element as black tea but multiplied by 3
print(f'Strong brew: {strong_brew}')# the output will be : Strong brew: ['black tea', 'black tea', 'black tea']
#so the black tea will be printed thrice in the list

strong_bew1 = ['black tea', 'water'] * 3
print(f'Strong brew1: {strong_bew1}') # both the elements will be printed twice but one after anohter 
#output: Strong brew1: ['black tea', 'water', 'black tea', 'water', 'black tea', 'water']


#bytearray
raw_spice_data = bytearray(b'CINAMON')# bytearray is a method
raw_spice_data = raw_spice_data.replace(b'CINA', b'CARD')
print(f'raw spice data ; {raw_spice_data}')

'''
Let's go through the code step by step.

raw_spice_data = bytearray(b'CINAMON')  # bytearray is a method
1. b'CINAMON'

The b before the string means it is a bytes literal rather than a normal string.

b'CINAMON'

represents the sequence of bytes:

67 73 78 65 77 79 78

which correspond to the characters:

C I N A M O N
2. bytearray()

bytearray() creates a mutable sequence of bytes.

Unlike bytes, which cannot be changed, a bytearray can be modified.

raw_spice_data = bytearray(b'CINAMON')

Now raw_spice_data contains:

bytearray(b'CINAMON')
3. replace()
raw_spice_data = raw_spice_data.replace(b'CINA', b'CARD')

The replace() method searches for the byte sequence:

b'CINA'

and replaces it with:

b'CARD'

Original:

C I N A M O N
^^^^

Replace:

C A R D

Result:

CARDMON

So now:

raw_spice_data

becomes

bytearray(b'CARDMON')

Notice that:

CINA → CARD
MON remains unchanged.
4. Printing
print(f'raw spice data : {raw_spice_data}')

Output:

raw spice data : bytearray(b'CARDMON')
Why use bytearray?

bytearray is commonly used when working with:

Binary files
Images
Audio/video data
Network packets
Data that needs to be modified efficiently

For example:

data = bytearray(b'hello')

data[0] = ord('H')

print(data)

Output:

bytearray(b'Hello')
Difference between bytes and bytearray
bytes	bytearray
Immutable (cannot change)	Mutable (can change)
Faster for read-only data	Useful when modifying binary data
Example: b'ABC'	Example: bytearray(b'ABC')
Complete example
raw_spice_data = bytearray(b'CINAMON')

print(raw_spice_data)
# bytearray(b'CINAMON')

raw_spice_data = raw_spice_data.replace(b'CINA', b'CARD')

print(raw_spice_data)
# bytearray(b'CARDMON')

This code creates a mutable byte sequence containing CINAMON, replaces the byte sequence CINA with CARD, and prints the updated byte sequence bytearray(b'CARDMON').

'''
