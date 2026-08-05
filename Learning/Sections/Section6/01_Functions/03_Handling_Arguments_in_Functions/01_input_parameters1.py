# chai = [1, 2, 3]
# def edit_chai(cup):
#     cup[1] = 42

# edit_chai(chai)
# print(chai)


# def make_chai(tea, milk, sugar):
#     print(tea, milk, sugar)

# make_chai('Darjeeling', 'yes', 'Low')#positional
# make_chai(tea='Green', sugar='Medium', milk='No') #keywords


# def special_chai(*ingredients, **extras):
#     print('Ingredients', ingredients)
#     print('Extras', extras)

# special_chai('Cinnamon', 'Cardmom', sweetener='honey', foam='yes')

# def chai_order(order=[]):
#     order.append('Masala')
#     print(order)

# chai_order()
# chai_order()

# Create a list named 'chai'.
# Lists are mutable, meaning their contents can be changed.
chai = [1, 2, 3]


# Define a function that accepts one parameter 'cup'.
def edit_chai(cup):

    # Change the second element of the list.
    # Index 1 means the second item because indexing starts from 0.
    cup[1] = 42


# Pass the list 'chai' to the function.
edit_chai(chai)


# Print the modified list.
print(chai)



# Define a function with three parameters.
def make_chai(tea, milk, sugar):

    # Print the values received by the parameters.
    print(tea, milk, sugar)


# Positional arguments:
# Values are assigned according to their position.
make_chai('Darjeeling', 'yes', 'Low')


# Keyword arguments:
# Values are assigned using parameter names.
# The order does not matter.
make_chai(tea='Green', sugar='Medium', milk='No')



# Define a function that accepts:
# *ingredients → multiple positional arguments
# **extras → multiple keyword arguments
def special_chai(*ingredients, **extras):

    # ingredients is stored as a tuple.
    print('Ingredients', ingredients)

    # extras is stored as a dictionary.
    print('Extras', extras)


# Passing multiple positional and keyword arguments.
special_chai(
    'Cinnamon',
    'Cardmom',
    sweetener='honey',
    foam='yes'
)



# Define a function with a default mutable argument.
# The default value is created only once.
def chai_order(order=[]):

    # Add 'Masala' to the existing list.
    order.append('Masala')

    # Print the list.
    print(order)


# First call uses the default empty list.
chai_order()

# Second call uses the SAME list from the first call.
chai_order()


'''
Explanation

This code covers several important Python concepts:

Mutable objects and function arguments
Positional arguments
Keyword arguments
*args and **kwargs
The danger of mutable default arguments
Part 1: Passing a List to a Function
chai = [1, 2, 3]

A list is created:

chai → [1, 2, 3]

Lists are mutable, meaning they can be changed.

Function:

def edit_chai(cup):
    cup[1] = 42

The function receives the same list.

When we call:

edit_chai(chai)

Python passes the reference to the list.

Inside the function:

cup[1] = 42

Changes:

Before:

[1, 2, 3]

After:

[1, 42, 3]

So:

print(chai)

Output:

[1, 42, 3]
Important Difference
Immutable objects:

Examples:

int
float
string
tuple

Changing them creates a new object.

Mutable objects:

Examples:

list
dictionary
set

They can be changed directly.

Part 2: Positional Arguments

Function:

def make_chai(tea, milk, sugar):

It expects three values.

Calling:

make_chai('Darjeeling', 'yes', 'Low')

Python matches by position:

Parameter	Value
tea	Darjeeling
milk	yes
sugar	Low

Output:

Darjeeling yes Low
Part 3: Keyword Arguments

Example:

make_chai(tea='Green', sugar='Medium', milk='No')

Here we specify parameter names.

Python matches:

tea → Green
milk → No
sugar → Medium

The order does not matter.

Output:

Green No Medium
Positional vs Keyword
Positional
make_chai('Green', 'No', 'Medium')

Problem:

You must remember the order.

Keyword
make_chai(
    tea='Green',
    milk='No',
    sugar='Medium'
)

Advantage:

Easier to read
Order does not matter
Part 4: *args (Multiple Positional Arguments)

Function:

def special_chai(*ingredients, **extras):

*ingredients collects all extra positional arguments.

Example:

special_chai('Cinnamon', 'Cardmom')

Python stores them as a tuple:

ingredients = ('Cinnamon', 'Cardmom')

Output:

Ingredients ('Cinnamon', 'Cardmom')
Part 5: **kwargs (Multiple Keyword Arguments)

Keyword arguments:

sweetener='honey'
foam='yes'

are collected into a dictionary:

extras = {
    'sweetener': 'honey',
    'foam': 'yes'
}

Output:

Extras {'sweetener': 'honey', 'foam': 'yes'}
Complete special_chai() Output
Ingredients ('Cinnamon', 'Cardmom')
Extras {'sweetener': 'honey', 'foam': 'yes'}
Part 6: Default Mutable Argument Problem

Function:

def chai_order(order=[]):

Here the default value is a list.

Many beginners expect:

First call → []
Second call → []

But Python behaves differently.

First call
chai_order()

Uses the default list:

[]

Then:

order.append('Masala')

Becomes:

['Masala']

Output:

['Masala']
Second call
chai_order()

Python does not create a new list.

It uses the same list:

['Masala']

Then appends again:

['Masala', 'Masala']

Output:

['Masala', 'Masala']
Why is this a problem?

Because the list keeps its previous values.

Usually, we want every function call to start fresh.

Correct Way

Use None:

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

Now each call gets a new list.

Final Output of Your Complete Program
[1, 42, 3]

Darjeeling yes Low

Green No Medium

Ingredients ('Cinnamon', 'Cardmom')
Extras {'sweetener': 'honey', 'foam': 'yes'}

['Masala']
['Masala', 'Masala']
Key Concepts Summary
Concept	Example	Meaning
Mutable object	list	Can be changed directly
Positional arguments	make_chai('Darjeeling','yes','Low')	Matched by order
Keyword arguments	tea='Green'	Matched by name
*args	*ingredients	Collects multiple positional arguments
**kwargs	**extras	Collects multiple keyword arguments
Mutable default argument	order=[]	Same object reused between calls
Safe default	order=None	Creates a fresh object each time

'''

