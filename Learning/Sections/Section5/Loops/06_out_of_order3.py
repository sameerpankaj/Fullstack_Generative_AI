# Create a list containing different tea flavours and their status
flavours = ['Ginger', 'Out of stock', 'Lemon', 'Discontinued', 'Tulsi']


# Start a loop that checks each flavour one by one from the list
for flavour in flavours:


    # Check if the current flavour is "Out of stock"
    # If it is, skip this item and immediately move to the next flavour
    if flavour == 'Out of stock':
        continue


    # Check if the current flavour is "Discontinued"
    # If it is, print the message and then stop the loop completely
    if flavour == 'Discontinued':
        print(f'{flavour} item found')
        break


# This line is outside the loop.
# It executes after the loop finishes.
# The loop finishes because of "break" when "Discontinued" is found.
print(f'Outside of loop')


'''
Step-by-step explanation:
List creation
flavours = ['Ginger', 'Out of stock', 'Lemon', 'Discontinued', 'Tulsi']

A list is created with 5 items:

Ginger
Out of stock
Lemon
Discontinued
Tulsi
Loop starts
for flavour in flavours:

Python takes each item from the list one by one and stores it in the variable flavour.

First iteration

Current value:

flavour = 'Ginger'

Check:

if flavour == 'Out of stock':

Result:

False

So Python skips this block.

Next check:

if flavour == 'Discontinued':

Result:

False

So nothing happens.

The loop moves to the next item.

No output is printed.

Second iteration

Current value:

flavour = 'Out of stock'

First condition:

if flavour == 'Out of stock':
    continue

Condition is True.

Python executes:

continue

Meaning:

Skip the current item and immediately start the next loop iteration.

So Python does not check:

if flavour == 'Discontinued'

and moves to:

Lemon

No output is printed.

Third iteration

Current value:

flavour = 'Lemon'

Check:

if flavour == 'Out of stock':

False.

Check:

if flavour == 'Discontinued':

False.

Nothing is printed.

Move to the next item.

Fourth iteration

Current value:

flavour = 'Discontinued'

First condition:

if flavour == 'Out of stock':

False.

Second condition:

if flavour == 'Discontinued':

True.

Now Python executes:

print(f'{flavour} item found')

Output:

Discontinued item found

Then:

break

runs.

break means:

Stop the loop immediately.

The remaining item:

Tulsi

is never checked.

After the loop

Python reaches:

print(f'Outside of loop')

This is outside the loop, so it runs after the loop stops.

Output:

Outside of loop
Final output:
Discontinued item found
Outside of loop
Important difference from your previous code:

Previously you had:

print(f'{flavour} item found')

outside the if flavour == 'Discontinued' block.

That printed available items before "Discontinued".

Now you have:

if flavour == 'Discontinued':
    print(f'{flavour} item found')
    break

So the program prints only when it finds "Discontinued".

The logic is now:

Ignore "Out of stock" ✅
Ignore "Ginger" and "Lemon" (because there is no print statement for them) ✅
When "Discontinued" appears → print it → stop the loop 🛑
Print "Outside of loop" after the loop finishes ✅

'''
