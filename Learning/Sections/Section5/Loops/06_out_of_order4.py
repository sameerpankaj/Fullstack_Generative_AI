# Create a list containing different tea flavours and their availability status
flavours = ['Ginger', 'Out of stock', 'Lemon', 'Discontinued', 'Tulsi']


# Start a loop that takes each flavour from the list one by one
for flavour in flavours:

    # Check if the current flavour is "Out of stock"
    # If yes, skip this item and immediately move to the next flavour
    if flavour == 'Out of stock':
        continue


    # Check if the current flavour is "Discontinued"
    # If yes, print the message and stop the loop completely
    if flavour == 'Discontinued':
        print(f'{flavour} item found')
        break


    # This line runs for all flavours except:
    # 1. "Out of stock" (skipped by continue)
    # 2. "Discontinued" (printed above and stopped by break)
    print(f'{flavour} item found')


# This line is outside the loop.
# It runs after the loop ends because of break or after all items are checked.
print(f'Outside of loop')

'''

Step-by-step explanation:
List creation
flavours = ['Ginger', 'Out of stock', 'Lemon', 'Discontinued', 'Tulsi']

The list contains:

Ginger
Out of stock
Lemon
Discontinued
Tulsi

The loop will check each item one by one.

Loop starts
for flavour in flavours:

Python takes the first item and stores it in the variable flavour.

1st iteration

Current value:

flavour = 'Ginger'

Check:

if flavour == 'Out of stock':

False → continue.

Check:

if flavour == 'Discontinued':

False → continue.

Now this line executes:

print(f'{flavour} item found')

Output:

Ginger item found
2nd iteration

Current value:

flavour = 'Out of stock'

First condition:

if flavour == 'Out of stock':
    continue

Condition is True.

Python executes:

continue

Meaning:

Ignore this item and jump back to the start of the loop.

So it does not execute:

print(f'{flavour} item found')

No output is printed.

3rd iteration

Current value:

flavour = 'Lemon'

Check:

if flavour == 'Out of stock'

False.

Check:

if flavour == 'Discontinued'

False.

Execute:

print(f'{flavour} item found')

Output:

Lemon item found
4th iteration

Current value:

flavour = 'Discontinued'

First condition:

if flavour == 'Out of stock':

False.

Second condition:

if flavour == 'Discontinued':

True.

Python executes:

print(f'{flavour} item found')

Output:

Discontinued item found

Then:

break

runs.

break means:

Stop the loop immediately.

The last item:

Tulsi

is never checked.

After the loop

Python reaches:

print(f'Outside of loop')

This is outside the loop, so it runs after the loop ends.

Output:

Outside of loop
Final output:
Ginger item found
Lemon item found
Discontinued item found
Outside of loop
How the program behaves in simple words:

Imagine checking tea flavours in a store:

✅ Ginger → available → print it
❌ Out of stock → ignore it and move on
✅ Lemon → available → print it
🛑 Discontinued → print it and stop searching
Tulsi → never checked because the loop stopped
Important point:

The position of this line matters:

print(f'{flavour} item found')

Because it is outside the Discontinued condition, it prints normal items like Ginger and Lemon.

But when the flavour is "Discontinued", the first print inside the if block runs, and then break stops the loop.

'''