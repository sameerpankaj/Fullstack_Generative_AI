# 

# Define a function named 'chai_order'.
# The default value of order is set to None.
def chai_order(order=None):

    # Check if no order was provided when calling the function.
    if order is None:

        # Create a new empty list.
        # This happens every time the function is called without an argument.
        order = []

    # Print the current order list.
    print(order)


# Call the function without passing any argument.
# Since no order is provided, a new empty list is created.
chai_order()


# Call the function again without passing any argument.
# A completely new empty list is created again.
chai_order()


'''
Explanation

This example demonstrates the correct way to handle mutable default arguments in Python.

The common problem is using:

def chai_order(order=[]):

because the same list is reused every time the function is called.

Instead, we use:

def chai_order(order=None):

and create a new list inside the function.

Step 1: Function Definition
def chai_order(order=None):

Here:

order is a parameter.
None is the default value.

Meaning:

If the user does not provide an order, use None.

At this stage, no list exists.

Step 2: First Function Call
chai_order()

No argument is provided.

So Python sets:

order = None

Now the condition runs:

if order is None:

This is True.

So Python executes:

order = []

A new empty list is created:

order → []

Then:

print(order)

Output:

[]
Step 3: Second Function Call
chai_order()

Again, no argument is provided.

Python again sets:

order = None

The condition is True:

if order is None:

A new empty list is created:

order → []

Then:

print(order)

Output:

[]
Execution Flow
Program starts
      |
      ▼
Define chai_order()
      |
      ▼
Call chai_order()
      |
      ▼
order = None
      |
      ▼
Create new list []
      |
      ▼
Print []
      |
      ▼
Call chai_order() again
      |
      ▼
order = None
      |
      ▼
Create another new list []
      |
      ▼
Print []
Final Output
[]
[]
Comparison With the Wrong Approach
❌ Problematic Code
def chai_order(order=[]):
    order.append('Masala')
    print(order)

chai_order()
chai_order()

Output:

['Masala']
['Masala', 'Masala']

Why?

Because Python creates the default list only once and reuses it.

✅ Correct Approach
def chai_order(order=None):
    if order is None:
        order = []

    order.append('Masala')
    print(order)

chai_order()
chai_order()

Output:

['Masala']
['Masala']

Each function call gets a fresh list.

Why use None?

None is a special Python value meaning:

"No value has been provided."

It acts as a signal:

if order is None:

means:

"If the user didn't give an order, create a new one."

Key Concepts
Concept	Meaning
None	Represents no value
Mutable object	Object that can be changed (list, dictionary, set)
Default argument	Value used when no argument is passed
is None	Correct way to check for None
New list inside function	Prevents data from leaking between function calls

This pattern is widely used in professional Python code, especially when working with lists, dictionaries, and machine learning/data processing functions.

'''