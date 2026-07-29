
#program to find remainder without using walrus operator
# Store the number that we want to check.
value = 13

# Calculate the remainder when 'value' is divided by 5.
# The modulus (%) operator returns the remainder after division.
remainder = value % 5

# Check if 'remainder' is non-zero.
# In Python:
# - 0 is treated as False
# - Any non-zero number is treated as True
if remainder:

    # This line executes because the remainder is not zero.
    # It prints the remainder, showing that the number is not divisible by 5.
    print(f'Not divisible, remainder is {remainder}')


'''

Explanation
Step 1: Store the value
value = 13

A variable named value is created and assigned the number 13.

Variable	Value
value	13
Step 2: Find the remainder
remainder = value % 5

The modulus operator (%) calculates the remainder after division.

Calculation:

13 ÷ 5 = 2 remainder 3

So:

remainder = 3
Expression	Result
13 % 5	3
Step 3: Check the condition
if remainder:

This is the same as writing:

if remainder != 0:

In Python, numbers are treated as Boolean values:

Number	Boolean Value
0	False
Any non-zero number	True

Since:

remainder = 3

Python sees:

if 3:

Because 3 is non-zero, it is considered True.

Step 4: Execute the print statement
print(f'Not divisible, remainder is {remainder}')

Python replaces {remainder} with its value:

Not divisible, remainder is 3
Execution Flow
value = 13
      │
      ▼
13 % 5
      │
      ▼
remainder = 3
      │
      ▼
if remainder
      │
      ▼
3 is True
      │
      ▼
Print:
"Not divisible, remainder is 3"
Final Output
Not divisible, remainder is 3
What if the number was divisible by 5?

Example:

value = 15
remainder = value % 5

if remainder:
    print(f'Not divisible, remainder is {remainder}')

Calculation:

15 % 5 = 0

Now:

if 0:

Since 0 is treated as False, the print() statement is skipped.

Output:

No output
Key Concepts
% (modulus) returns the remainder after division.
13 % 5 equals 3.
In Python:
0 is False.
Any non-zero number is True.
if remainder: is a concise way of writing if remainder != 0:.
Because the remainder is 3, the condition is True, so the message is printed.
'''