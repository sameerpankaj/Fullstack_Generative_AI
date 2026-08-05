# def pure_chai(cups):
#     return cups * 10

# total_chai = 0



# #this way is not recommended
# def impure_chai(cups):
#     global total_chai
#     total_chai *= cups


# Define a pure function.
# A pure function always produces the same output for the same input
# and does not modify any external variables.
def pure_chai(cups):

    # Calculate and return the total price.
    # Assuming each cup costs 10.
    return cups * 10


# Global variable to keep track of total chai.
total_chai = 0


# This way is NOT recommended.
# This function changes a global variable, making it an impure function.
def impure_chai(cups):

    # Tell Python to use the global variable 'total_chai'.
    global total_chai

    # Modify the global variable.
    # Multiply the current value by the number of cups.
    total_chai *= cups


'''
Explanation

This example compares pure functions and impure functions.

Understanding this difference is important because pure functions are easier to read, test, and maintain.

Part 1: Pure Function
def pure_chai(cups):
    return cups * 10

This is called a pure function.

It only depends on its input (cups) and returns a result.

It does not change anything outside the function.

Example
print(pure_chai(5))

Calculation:

5 × 10 = 50

Output:

50

If you call it again:

print(pure_chai(5))

Output is still:

50

The result is always the same for the same input.

Why is it called "Pure"?

A pure function has two properties:

1. Same input → Same output
pure_chai(3)

Always returns:

30
2. No side effects

It does not change:

Global variables
Files
Databases
User input

It only returns a value.

Part 2: Global Variable
total_chai = 0

This variable exists outside all functions.

It belongs to the global scope.

Current value:

total_chai = 0
Part 3: Impure Function
def impure_chai(cups):

This function uses:

global total_chai

which means:

"Use the global variable instead of creating a local one."

Then:

total_chai *= cups

updates the global variable.

Suppose:

total_chai = 10

and you call:

impure_chai(5)

Calculation:

10 × 5 = 50

Now:

total_chai = 50

The function has changed data outside itself.

This is called a side effect.

Why is this NOT Recommended?

Imagine this code:

total_chai = 10

impure_chai(2)

print(total_chai)

Output:

20

The value changed even though you never directly assigned:

total_chai = 20

Someone reading your code must inspect the function to understand why total_chai changed.

This makes programs harder to understand and debug.

Better Approach

Instead of changing a global variable:

def pure_chai(cups):
    return cups * 10

bill = pure_chai(5)

print(bill)

Output:

50

Everything is clear:

Input → Output
No hidden changes
Note About Your Code

Your function contains:

total_chai *= cups

Since:

total_chai = 0

the result will always be:

0 × cups = 0

For example:

total_chai = 0

impure_chai(5)

print(total_chai)

Output:

0

If your goal is to keep a running total, you probably meant:

total_chai += cups

This adds the number of cups to the total.

Example:

total_chai = 0

impure_chai(5)   # total_chai = 5
impure_chai(3)   # total_chai = 8
Execution Flow (Pure Function)
Call pure_chai(5)
        |
        ▼
Calculate:
5 × 10
        |
        ▼
Return 50
        |
        ▼
Nothing else changes
Execution Flow (Impure Function)
Global:
total_chai = 10
        |
        ▼
Call impure_chai(5)
        |
        ▼
Modify global variable
        |
        ▼
total_chai = 50
Pure vs Impure Functions
Feature	Pure Function	Impure Function
Uses only inputs	✅ Yes	❌ Not always
Returns a value	✅ Yes	May or may not
Modifies global variables	❌ No	✅ Yes
Same input gives same output	✅ Yes	❌ Not guaranteed
Easy to test	✅ Yes	❌ Harder
Key Concepts
A pure function depends only on its inputs and returns a value.
An impure function changes data outside the function (such as a global variable).
Using global variables can make code harder to understand because changes happen as side effects.
In most cases, prefer writing pure functions and use their returned values rather than modifying global state.

'''