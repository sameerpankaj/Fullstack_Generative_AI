

#mutable data types

# Create a variable named 'sugar_amount' and assign it the value 2
sugar_amount = 2

# Print the current value of the variable
print(f'Initial sugar: {sugar_amount}')

# Reassign the variable to a new value (12)
sugar_amount = 12

# Print the updated value of the variable
print(f'Second Initial sugar: {sugar_amount}')

# Print the unique identity (memory ID) of the integer object 2
print(f'ID of 2: {id(2)}')

# Print the unique identity (memory ID) of the integer object 12
print(f'ID of 12: {id(12)}')





'''
Note: id() returns the unique identity of an object during the current Python session. The actual numbers you see may differ each time you run the program.
'''


'''

Let's go through your code line by line.

sugar_amount = 2
print(f'Initial sugar: {sugar_amount}')

sugar_amount = 12

print(f'Second Initial sugar: {sugar_amount}')

print(f'ID of 2: {id(2)}')
print(f'ID of 12: {id(12)}')
Line 1
sugar_amount = 2
Creates a variable named sugar_amount.
The variable refers to the integer object 2.

Think of it like this:

sugar_amount ─────► 2
Line 2
print(f'Initial sugar: {sugar_amount}')

Output:

Initial sugar: 2

The f before the string creates an f-string, allowing you to insert the value of sugar_amount into the text.

Line 3
sugar_amount = 12

This does not change the integer 2.

Instead, it changes what sugar_amount refers to.

Before:

sugar_amount ───► 2

After:

2          (still exists)

sugar_amount ───► 12

In Python, integers are immutable, meaning they cannot be modified. Assigning a new value simply makes the variable point to a different integer object.

Line 4
print(f'Second Initial sugar: {sugar_amount}')

Output:

Second Initial sugar: 12
Line 5
print(f'ID of 2: {id(2)}')

The id() function returns the unique identity (memory identity) of an object during the program's execution.

Example output:

ID of 2: 140729778850888

Your number will likely be different.

Line 6
print(f'ID of 12: {id(12)}')

Example output:

ID of 12: 140729778851208

Again, the exact value depends on your Python session and platform.

Better demonstration

Instead of comparing the IDs of literal numbers, compare the variable before and after reassignment:

sugar_amount = 2
print(sugar_amount)
print(id(sugar_amount))

sugar_amount = 12
print(sugar_amount)
print(id(sugar_amount))

Example output:

2
2151971668568

12
2151971668888

Notice that the ID changes because sugar_amount now refers to a different integer object.

Key takeaway
Variables in Python hold references to objects.
2 and 12 are separate integer objects.
Reassigning sugar_amount does not modify the integer 2; it simply points sugar_amount to the integer 12.

This concept—variables referring to objects rather than containing values—is fundamental to understanding how Python manages memory.



'''