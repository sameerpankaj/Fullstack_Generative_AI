#Tuples

# Create a tuple containing three masala spices
# Tuples are ordered collections and are immutable (cannot be changed after creation)
masala_spices = ('cardamom', 'cloves', 'cinamon')

# Unpack the tuple values into three separate variables
# spice1 gets the first value ('cardamom')
# spice2 gets the second value ('cloves')
# spice3 gets the third value ('cinamon')
(spice1, spice2, spice3) = masala_spices

# Print the individual spices using an f-string
print(f'Main masala spices: {spice1}, {spice2}, {spice3}')

# Create two variables and assign values at the same time
# ginger_ratio = 2
# cardmom_ratio = 1
ginger_ratio, cardmom_ratio = 2, 1


# Print the original ratio values
print(f'Ratio is G {ginger_ratio} and C {cardmom_ratio}')


# Swap the values of two variables without using a temporary variable
# Before:
# ginger_ratio = 2
# cardmom_ratio = 1
#
# After:
# ginger_ratio = 1
# cardmom_ratio = 2
ginger_ratio, cardmom_ratio = cardmom_ratio, ginger_ratio


# Print the swapped values
print(f'Ratio is G {ginger_ratio} and C {cardmom_ratio}')


# Membership testing using the "in" operator
# Checks whether a value exists inside the tuple
#
# 'ginger' is not present in masala_spices, so output will be False
print(f"Is ginger in masala spices? {'ginger' in masala_spices}")


# 'cinamon' exists in the tuple, so output will be True
print(f"Is cinamon in masala spices? {'cinamon' in masala_spices}")


# Python is case-sensitive
# 'Cinamon' with capital C is different from 'cinamon'
# Therefore, output will be False
print(f"Is Cinamon in masala spices? {'Cinamon' in masala_spices}")

'''

Step-by-step explanation:
1. Creating a tuple
masala_spices = ('cardamom', 'cloves', 'cinamon')

Python stores the values in a tuple:

Index:     0           1          2
Value:  cardamom    cloves    cinamon

Tuples are immutable, meaning you cannot modify them:

masala_spices[0] = 'ginger'

will give an error:

TypeError: 'tuple' object does not support item assignment
2. Tuple unpacking
(spice1, spice2, spice3) = masala_spices

Python automatically assigns values:

spice1 = 'cardamom'
spice2 = 'cloves'
spice3 = 'cinamon'

This is called tuple unpacking.

3. Printing the values
print(f'Main masala spices: {spice1}, {spice2}, {spice3}')

The f before the string creates an f-string, allowing variables to be inserted inside {}.

Output:

Main masala spices: cardamom, cloves, cinamon
Additional example:

You can also unpack without brackets:

spice1, spice2, spice3 = masala_spices

The parentheses are optional.

Important rule for tuple unpacking:

The number of variables must match the number of items:

(a, b) = (10, 20)       # ✅ Works

(a, b, c) = (10, 20)    # ❌ Error

Error:

ValueError: not enough values to unpack

Tuple unpacking is commonly used in Python to return multiple values from functions and to swap variables.
'''

'''
# Create a tuple containing three masala spices
# A tuple is an ordered collection of elements
# Tuples are immutable, meaning their values cannot be changed after creation
masala_spices = ('cardamom', 'cloves', 'cinamon')


# Tuple unpacking:
# Assign each tuple value to a separate variable
# spice1 gets 'cardamom'
# spice2 gets 'cloves'
# spice3 gets 'cinamon'
(spice1, spice2, spice3) = masala_spices


# Print the values stored in the variables using an f-string
print(f'Main masala spices: {spice1}, {spice2}, {spice3}')


# Create two variables and assign values at the same time
# ginger_ratio = 2
# cardmom_ratio = 1
ginger_ratio, cardmom_ratio = 2, 1


# Print the original ratio values
print(f'Ratio is G {ginger_ratio} and C {cardmom_ratio}')


# Swap the values of two variables without using a temporary variable
# Before:
# ginger_ratio = 2
# cardmom_ratio = 1
#
# After:
# ginger_ratio = 1
# cardmom_ratio = 2
ginger_ratio, cardmom_ratio = cardmom_ratio, ginger_ratio


# Print the swapped values
print(f'Ratio is G {ginger_ratio} and C {cardmom_ratio}')


# Membership testing using the "in" operator
# Checks whether a value exists inside the tuple
#
# 'ginger' is not present in masala_spices, so output will be False
print(f"Is ginger in masala spices? {'ginger' in masala_spices}")


# 'cinamon' exists in the tuple, so output will be True
print(f"Is cinamon in masala spices? {'cinamon' in masala_spices}")


# Python is case-sensitive
# 'Cinamon' with capital C is different from 'cinamon'
# Therefore, output will be False
print(f"Is Cinamon in masala spices? {'Cinamon' in masala_spices}")
Output:
Main masala spices: cardamom, cloves, cinamon

Ratio is G 2 and C 1

Ratio is G 1 and C 2

Is ginger in masala spices? False

Is cinamon in masala spices? True

Is Cinamon in masala spices? False
Key concepts demonstrated:
1. Tuple immutability
masala_spices[0] = 'ginger'

❌ Error:

TypeError: 'tuple' object does not support item assignment
2. Tuple unpacking

Instead of:

spice1 = masala_spices[0]
spice2 = masala_spices[1]
spice3 = masala_spices[2]

Python allows:

spice1, spice2, spice3 = masala_spices
3. Swapping variables

Traditional way:

temp = ginger_ratio
ginger_ratio = cardmom_ratio
cardmom_ratio = temp

Python shortcut:

ginger_ratio, cardmom_ratio = cardmom_ratio, ginger_ratio
4. Membership testing

The in operator checks if an item exists:

'cloves' in masala_spices

Output:

True

Remember: Python is case-sensitive

'cinamon' == 'Cinamon'

Output:

False
'''