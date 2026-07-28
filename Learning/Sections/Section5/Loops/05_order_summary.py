#use of zip in loop

'''

```
You are preparing an order summary with customer names and their total bill.
Task:
  Use two lists: one for names and on for bills.
  Print: '[Name] paid amount in rupees'

```

'''

# List of people's names
names = ['Hitesh', 'Meera', 'Sam', 'Ali']

# Corresponding bill amounts in rupees
bills = [50, 70, 100, 55]

# zip(names, bills) pairs each name with its corresponding bill amount.
# It creates pairs like:
# ('Hitesh', 50)
# ('Meera', 70)
# ('Sam', 100)
# ('Ali', 55)

# Loop through each (name, amount) pair
for name, amount in zip(names, bills):
    
    # Print the formatted output using an f-string
    print(f'{name} paid {amount} rupees')


    '''
    Output
Hitesh paid 50 rupees
Meera paid 70 rupees
Sam paid 100 rupees
Ali paid 55 rupees
What zip() does
# Example to understand zip()

names = ['Hitesh', 'Meera', 'Sam']
bills = [50, 70, 100]

# Convert the zip object to a list so we can see its contents
print(list(zip(names, bills)))

Output:

[('Hitesh', 50), ('Meera', 70), ('Sam', 100)]
How the for loop works
# Each tuple from zip() is automatically unpacked
# into the variables 'name' and 'amount'

for name, amount in zip(names, bills):
    print(name, amount)

This is equivalent to writing:

pairs = [('Hitesh', 50), ('Meera', 70), ('Sam', 100), ('Ali', 55)]

for pair in pairs:
    name = pair[0]      # First element of the tuple
    amount = pair[1]    # Second element of the tuple
    print(f'{name} paid {amount} rupees')
Key points to remember
zip() combines two or more iterables element by element.
The for loop automatically unpacks each tuple into separate variables.
If the lists have different lengths, zip() stops when the shortest list ends.

For example:

names = ['Hitesh', 'Meera', 'Sam', 'Ali']
bills = [50, 70]

for name, amount in zip(names, bills):
    print(f'{name} paid {amount} rupees')

Output:

Hitesh paid 50 rupees
Meera paid 70 rupees

Notice that Sam and Ali are ignored because bills has only two values.
    
    
    '''
