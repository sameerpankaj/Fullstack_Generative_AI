#using walrus operator

# Store the number that we want to check.
value = 13

# Calculate the remainder when 'value' is divided by 5.
# The := operator (called the walrus operator) assigns the result to
# the variable 'remainder' and returns the assigned value at the same time.
if (remainder := value % 5):

    # This line executes only if the remainder is not zero.
    # It prints the remainder, showing that the number is not divisible by 5.
    print(f'Not divisible, remainder is {remainder}')


    '''
    
    Explanation
Step 1: Store the value
value = 13

A variable named value is created and assigned the number 13.

Variable	Value
value	13
Step 2: The if statement
if (remainder := value % 5):

This line uses the walrus operator (:=), also known as the assignment expression.

The walrus operator does two things at once:

It calculates the expression.
It stores the result in a variable.

First, Python calculates:

value % 5

Calculation:

13 % 5 = 3

Then Python assigns:

remainder = 3

Finally, Python checks whether the assigned value is True or False.

So this line is effectively doing:

remainder = value % 5

if remainder:

But in a single line.

Step 3: Boolean evaluation

After the assignment:

remainder = 3

Python checks:

if 3:

In Python:

Value	Boolean Result
0	False
Any non-zero number	True

Since 3 is non-zero, the condition is True.

Step 4: Execute the print statement
print(f'Not divisible, remainder is {remainder}')

Python replaces {remainder} with its value:

Not divisible, remainder is 3
Execution Flow
value = 13
      │
      ▼
value % 5
      │
      ▼
3
      │
      ▼
Assign:
remainder = 3
      │
      ▼
if 3
      │
      ▼
True
      │
      ▼
Print:
"Not divisible, remainder is 3"
Final Output
Not divisible, remainder is 3
What if the value was divisible by 5?

Example:

value = 15

if (remainder := value % 5):
    print(f'Not divisible, remainder is {remainder}')

Calculation:

15 % 5 = 0

Python performs:

remainder = 0

if 0:

Since 0 is False, the print() statement is skipped.

Output
No output

The variable remainder is still created and contains the value 0.

Without the Walrus Operator

The same code can be written as:

value = 13

remainder = value % 5

if remainder:
    print(f'Not divisible, remainder is {remainder}')

Both versions produce the same output.

The walrus operator simply lets you assign a value and test it in the same expression, making the code shorter and avoiding an extra assignment statement.

Key Concepts
:= is called the walrus operator (assignment expression).
It assigns a value to a variable and returns that value in one step.
value % 5 calculates the remainder.
13 % 5 equals 3.
Since 3 is non-zero, Python treats it as True, so the if block runs.
If the remainder were 0, the condition would be False, and nothing would be printed.
    
    '''