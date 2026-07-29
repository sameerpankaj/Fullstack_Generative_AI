#Continue

# Create a list containing different tea flavours and their availability status
flavours = ['Ginger', 'Out of stock', 'Lemon', 'Discontinued', 'Tulsi']

# Start a loop that goes through each flavour one by one
for flavour in flavours:

    # If the current flavour is "Out of stock", skip this item and continue with the next item
    if flavour == 'Out of stock':
        continue

    # If the current flavour is "Discontinued", stop the loop completely
    if flavour == 'Discontinued':
        break

    # Print a message for flavours that are available before reaching "Discontinued"
    print('Discontinued item found')

# This line runs after the loop ends (either normally or because of break)
print('Outside of loop')


'''

Explanation step by step:
1. Creating the list
flavours = ['Ginger', 'Out of stock', 'Lemon', 'Discontinued', 'Tulsi']

A list is created containing 5 items:

Index 0 → Ginger
Index 1 → Out of stock
Index 2 → Lemon
Index 3 → Discontinued
Index 4 → Tulsi
2. Starting the for loop
for flavour in flavours:

Python takes each item from the list one by one and stores it in the variable flavour.

The loop starts:

First iteration:
flavour = 'Ginger'

Check conditions:

if flavour == 'Out of stock':

False, so continue.

if flavour == 'Discontinued':

False, so continue.

Then:

print('Discontinued item found')

Output:

Discontinued item found
Second iteration:
flavour = 'Out of stock'

Now:

if flavour == 'Out of stock':
    continue

This condition is true.

continue means:

Skip the remaining code inside the loop and immediately go to the next item.

So this part is skipped:

if flavour == 'Discontinued':

and:

print('Discontinued item found')

Nothing is printed.

Third iteration:
flavour = 'Lemon'

Check:

if flavour == 'Out of stock':

False.

if flavour == 'Discontinued':

False.

Print runs:

Output:

Discontinued item found
Fourth iteration:
flavour = 'Discontinued'

Now:

if flavour == 'Discontinued':
    break

This condition is true.

break means:

Immediately stop the loop completely.

The loop does not check the remaining item:

Tulsi

The loop ends here.

3. Code after the loop
print('Outside of loop')

This is outside the for loop, so it always runs after the loop finishes.

Output:

Outside of loop
Final output of the program:
Discontinued item found
Discontinued item found
Outside of loop
Difference between continue and break
Keyword	Meaning	Example
continue	Skip the current item and move to the next one	Ignore "Out of stock"
break	Stop the entire loop immediately	Stop when "Discontinued" is found

A simple way to remember:

continue = "skip this one"
break = "stop everything"

'''