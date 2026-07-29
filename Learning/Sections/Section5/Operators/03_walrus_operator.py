# value = 13

# if remainder := value % 5:
#     print(f'Not divisible  remainder is {remainder}')

# Create a list of available chai cup sizes.
available_sizes = ['small', 'medium', 'large']

# Ask the user to enter a chai cup size.
# The walrus operator (:=) stores the user's input in the variable
# 'requested_size' and immediately checks whether it exists in the
# 'available_sizes' list.
if (requested_size := input('Enter your chai cup size: ')) in available_sizes:

    # If the entered size is available, print a confirmation message.
    print(f'Serving {requested_size} chai')

else:
    # If the entered size is not available, print an unavailable message.
    print(f'Size is unavailable - {requested_size}')


'''
Explanation
Step 1: Create a list of available sizes
available_sizes = ['small', 'medium', 'large']

This creates a list containing the cup sizes that the shop offers.

Index	Size
0	small
1	medium
2	large
Step 2: Ask the user for input
input('Enter your chai cup size: ')

Python displays the message:

Enter your chai cup size:

Suppose the user types:

medium

The input() function always returns a string, so:

'medium'

is returned.

Step 3: The walrus operator (:=)
(requested_size := input(...))

The walrus operator does two things at once:

It stores the user's input in the variable requested_size.
It returns that same value so it can be used immediately.

If the user enters:

medium

Python performs:

requested_size = 'medium'

and then uses 'medium' in the condition.

Without the walrus operator, you would write:

requested_size = input('Enter your chai cup size: ')

if requested_size in available_sizes:
    print(f'Serving {requested_size} chai')
else:
    print(f'Size is unavailable - {requested_size}')

Both versions work the same way.

Step 4: Check whether the size exists
if requested_size in available_sizes:

The in operator checks whether a value exists in a list.

For example:

'medium' in ['small', 'medium', 'large']

Result:

True

Since the condition is True, Python executes:

print(f'Serving {requested_size} chai')

Output:

Serving medium chai
Example 1: Valid input
User enters
large

Python checks:

'large' in ['small', 'medium', 'large']

Result:

True

Output:

Serving large chai
Example 2: Invalid input

Suppose the user enters:

extra large

Python checks:

'extra large' in ['small', 'medium', 'large']

Result:

False

The else block runs:

print(f'Size is unavailable - {requested_size}')

Output:

Size is unavailable - extra large
Execution Flow
When the user enters medium
available_sizes
      │
      ▼
['small', 'medium', 'large']
      │
      ▼
User enters:
medium
      │
      ▼
requested_size = "medium"
      │
      ▼
"medium" in available_sizes?
      │
     Yes
      │
      ▼
Print:
Serving medium chai
When the user enters extra large
available_sizes
      │
      ▼
['small', 'medium', 'large']
      │
      ▼
User enters:
extra large
      │
      ▼
requested_size = "extra large"
      │
      ▼
"extra large" in available_sizes?
      │
      No
      │
      ▼
Print:
Size is unavailable - extra large
Final Outputs
If the user enters:
small

Output:

Serving small chai
If the user enters:
medium

Output:

Serving medium chai
If the user enters:
large

Output:

Serving large chai
If the user enters:
extra large

Output:

Size is unavailable - extra large
Key Concepts
input() reads text entered by the user and returns it as a string.
:= (walrus operator) assigns the input to requested_size and returns it in the same expression.
in checks whether a value exists in a list.
If the entered size is found in available_sizes, the if block runs.
If the entered size is not found, the else block runs.

'''