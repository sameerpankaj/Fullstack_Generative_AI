# Create a list containing different tea flavours.
# Some items represent available flavours, while others represent their status.
flavours = ['Ginger', 'Out of stock', 'Lemon', 'Discontinued', 'Tulsi']


# Start a for loop.
# The loop takes each item from the flavours list one by one
# and stores the current item in the variable called "flavour".
for flavour in flavours:

    # Check if the current flavour is "Out of stock".
    # If this condition is True, the continue statement will skip
    # the remaining code inside the loop and move directly to the next item.
    if flavour == 'Out of stock':
        continue


    # Check if the current flavour is "Discontinued".
    # If this condition is True, the break statement will immediately
    # stop the entire loop.
    if flavour == 'Discontinued':
        break


    # This line runs only when the flavour is not:
    # 1. "Out of stock"
    # 2. "Discontinued"
    #
    # It prints the available flavour name.
    print(f'{flavour} item found')


# This line is outside the loop.
# It executes after the loop finishes.
# The loop can finish either:
# - naturally after checking all items
# - or early because of the break statement
print(f'Outside of loop')


'''

Step-by-step explanation:
1. Creating the list
flavours = ['Ginger', 'Out of stock', 'Lemon', 'Discontinued', 'Tulsi']

Python creates a list:

Position	Value
1	Ginger
2	Out of stock
3	Lemon
4	Discontinued
5	Tulsi
2. Starting the loop
for flavour in flavours:

The loop takes one item at a time from the list.

The execution happens like this:

First iteration

Current value:

flavour = 'Ginger'

Check:

if flavour == 'Out of stock':

False → continue.

Check:

if flavour == 'Discontinued':

False → continue.

Execute:

print(f'{flavour} item found')

Output:

Ginger item found
Second iteration

Current value:

flavour = 'Out of stock'

Check:

if flavour == 'Out of stock':

True.

Python executes:

continue

Meaning:

"Ignore this item and immediately go to the next item."

So it does not execute:

print(f'{flavour} item found')

No output is produced.

Third iteration

Current value:

flavour = 'Lemon'

Check:

if flavour == 'Out of stock':

False.

Check:

if flavour == 'Discontinued':

False.

Print executes:

Lemon item found
Fourth iteration

Current value:

flavour = 'Discontinued'

Check:

if flavour == 'Discontinued':

True.

Python executes:

break

Meaning:

"Stop the loop completely."

The loop ends here.

The remaining item:

'Tulsi'

is never checked.

3. Code after the loop

Now Python reaches:

print(f'Outside of loop')

Because this line is outside the for loop, it runs after the loop ends.

Output:

Outside of loop
Final output:
Ginger item found
Lemon item found
Outside of loop
Simple real-world analogy:

Imagine checking tea flavours in a shop:

✅ Ginger → available → show it
❌ Out of stock → skip it
✅ Lemon → available → show it
🛑 Discontinued → stop searching
Tulsi → never checked because the search already stopped

So:

continue = "Skip this one, check the next one"
break = "Stop the whole search"

'''