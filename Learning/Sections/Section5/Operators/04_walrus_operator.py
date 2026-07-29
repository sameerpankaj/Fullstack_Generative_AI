# Create a list of available chai flavors.
flavours = ['masala', 'ginger', 'lemon', 'mint']

# Display all the available flavors to the user.
print('Available flavours: ', flavours)

# Keep asking the user to choose a flavor until they enter
# one that exists in the 'flavours' list.
# The walrus operator (:=) stores the user's input in the
# variable 'flavor' and immediately checks whether it is
# NOT in the list of available flavors.
while (flavor := input('Choose your flavor: ')) not in flavours:

    # If the entered flavor is not available,
    # display an error message.
    print(f'Sorry, {flavor} is not available')

# This line runs after the while loop finishes.
# It means the user has finally entered a valid flavor.
print(f'You chose {flavor} chai')



'''

Explanation
Step 1: Create a list of available flavors
flavours = ['masala', 'ginger', 'lemon', 'mint']

This creates a list containing the flavors that the tea shop offers.

Index	Flavor
0	masala
1	ginger
2	lemon
3	mint
Step 2: Display the available flavors
print('Available flavours: ', flavours)

Output:

Available flavours: ['masala', 'ginger', 'lemon', 'mint']

This helps the user know which flavors they can choose.

Step 3: The while loop
while (flavor := input('Choose your flavor: ')) not in flavours:

This line does three things:

1. Ask the user for input
input('Choose your flavor: ')

For example, the user types:

orange
2. Store the input

The walrus operator (:=) stores the input in the variable:

flavor = 'orange'
3. Check whether the flavor exists

Python checks:

'orange' not in ['masala', 'ginger', 'lemon', 'mint']

Since "orange" is not in the list, the result is:

True

Because the condition is True, the while loop executes.

Step 4: Print the error message
print(f'Sorry, {flavor} is not available')

Output:

Sorry, orange is not available

The loop then repeats and asks again.

Step 5: User enters a valid flavor

Suppose the user now enters:

ginger

Python stores:

flavor = 'ginger'

Then checks:

'ginger' not in ['masala', 'ginger', 'lemon', 'mint']

Result:

False

Since the condition is False, the while loop stops.

Step 6: Print the final message

After leaving the loop, Python executes:

print(f'You chose {flavor} chai')

Output:

You chose ginger chai
Example Execution
User enters an invalid flavor first
Available flavours: ['masala', 'ginger', 'lemon', 'mint']

Choose your flavor: orange
Sorry, orange is not available

Choose your flavor: coffee
Sorry, coffee is not available

Choose your flavor: ginger
You chose ginger chai
User enters a valid flavor immediately

Input:

Choose your flavor: mint

Python checks:

'mint' not in flavours

Result:

False

The loop never runs, and the output is simply:

You chose mint chai
Execution Flow
Display available flavors
          │
          ▼
Ask user for a flavor
          │
          ▼
Store input in "flavor"
          │
          ▼
Is flavor NOT in the list?
          │
     Yes ─┴─ No
      │         │
      ▼         ▼
Print error   Exit loop
      │         │
      └─────────┘
          │
          ▼
Print:
"You chose <flavor> chai"
Without the Walrus Operator

The same program can be written as:

flavours = ['masala', 'ginger', 'lemon', 'mint']

print('Available flavours:', flavours)

flavor = input('Choose your flavor: ')

while flavor not in flavours:
    print(f'Sorry, {flavor} is not available')
    flavor = input('Choose your flavor: ')

print(f'You chose {flavor} chai')

Both versions work the same way. The walrus operator simply combines the assignment and the condition into one line, making the code shorter.

Key Concepts
while repeats a block of code as long as its condition is True.
input() reads text entered by the user.
:= (walrus operator) assigns the user's input to flavor and returns that value in the same expression.
not in checks whether a value does not exist in a list.
The loop continues until the user enters one of the valid flavors: masala, ginger, lemon, or mint. After a valid choice, the loop ends and the confirmation message is displayed.


'''