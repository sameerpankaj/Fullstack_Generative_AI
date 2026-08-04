# chai = 'Ginger chai'

# def prepare_chai(order):
#     print('Preparing ', order)

# prepare_chai(chai)
# print(chai)


# Create a global variable named 'chai'.
# It stores a string value.
chai = 'Ginger chai'


# Define a function named 'prepare_chai'.
# The parameter 'order' will receive a value when the function is called.
def prepare_chai(order):

    # Print the value stored in the parameter 'order'.
    print('Preparing ', order)


# Call the function and pass the value of the global variable 'chai'
# as an argument.
prepare_chai(chai)


# Print the global variable 'chai'.
# The original value is unchanged.
print(chai)


'''

Explanation

This example demonstrates passing variables as arguments to functions.

The important concept is:

When you pass a variable to a function, Python passes the value (for immutable objects like strings), and the original variable remains unchanged unless you modify it explicitly.

Step 1: Create the variable
chai = 'Ginger chai'

A global variable named chai is created.

Memory:

chai → "Ginger chai"
Step 2: Define the function
def prepare_chai(order):

This creates a function called prepare_chai.

It has one parameter:

order

A parameter is a placeholder that receives a value when the function is called.

Step 3: Call the function
prepare_chai(chai)

Here:

chai is the argument.
order is the parameter.

Python takes the value of chai:

'Ginger chai'

and passes it to the function.

Inside the function:

order = 'Ginger chai'

Now the function has:

prepare_chai()
        |
        └── order = "Ginger chai"
Step 4: Execute the print statement inside the function

Inside:

print('Preparing ', order)

Python replaces order with its value:

Preparing Ginger chai
Step 5: Print the original variable

After the function finishes:

print(chai)

Python prints the global variable:

chai = 'Ginger chai'

Output:

Ginger chai

The value is unchanged.

Execution Flow
Program starts
      |
      ▼
Create:
chai = "Ginger chai"
      |
      ▼
Call:
prepare_chai(chai)
      |
      ▼
Copy value:
order = "Ginger chai"
      |
      ▼
Print:
Preparing Ginger chai
      |
      ▼
Return to main program
      |
      ▼
Print:
Ginger chai
Final Output
Preparing Ginger chai
Ginger chai
Parameters vs Arguments
Term	Example in your code	Meaning
Parameter	order	Variable in function definition
Argument	chai	Value passed during function call

Example:

def prepare_chai(order):

order → parameter

prepare_chai(chai)

chai → argument

Important Concept: Strings are Immutable

Strings cannot be changed after creation.

Example:

def prepare_chai(order):
    order = 'Masala chai'
    print(order)

chai = 'Ginger chai'

prepare_chai(chai)

print(chai)

Output:

Masala chai
Ginger chai

Why?

Because inside the function:

order = 'Masala chai'

creates a new local variable.

It does not change:

chai = 'Ginger chai'
Key Concepts
A function can receive values through parameters.
Values passed into functions are called arguments.
The function gets its own local variable (order).
Changing the local variable does not affect the original global variable.
Strings are immutable objects in Python.
Output:
Preparing Ginger chai
Ginger chai

'''