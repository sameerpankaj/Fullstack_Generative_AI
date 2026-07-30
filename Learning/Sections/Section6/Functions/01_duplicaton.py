#Reducing code duplication

# def print_order(name, chai_type):  # when we pass something in the function definition is called parameters: name and chai_type are parameters here
#     print(f'{name} ordered {chai_type} chai!')

# print_order('Aman', 'masala') #when we pass something in the function call is called arguments
# print_order('Hitesh', 'Ginger')
# print_order('Jia', 'Tulsi')


# Define a function named 'print_order'.
# The function accepts two parameters:
# 1. name - the customer's name
# 2. chai_type - the type of chai ordered
def print_order(name, chai_type):  # Parameters are variables that receive values when the function is called.

    # Print a message showing which customer ordered which type of chai.
    print(f'{name} ordered {chai_type} chai!')


# Call the function and pass two arguments:
# 'Aman' is assigned to the parameter 'name'
# 'masala' is assigned to the parameter 'chai_type'
print_order('Aman', 'masala')


# Call the function again with different arguments.
print_order('Hitesh', 'Ginger')


# Call the function a third time with another set of arguments.
print_order('Jia', 'Tulsi')


'''
Explanation
What is a Function?

A function is a reusable block of code that performs a specific task.

Instead of writing the same code multiple times, you can write it once inside a function and call it whenever you need it.

Step 1: Defining the function
def print_order(name, chai_type):

Let's break it down:

def → Keyword used to define a function.
print_order → The name of the function.
name, chai_type → These are the parameters.
What are Parameters?

Parameters are variables listed in the function definition. They act as placeholders that receive values when the function is called.

Here:

name
chai_type

are parameters.

Think of them as empty containers waiting to receive data.

Step 2: Function body
print(f'{name} ordered {chai_type} chai!')

This line uses an f-string to insert the values of name and chai_type into the output.

The function doesn't know what name or chai_type are until it is called.

Step 3: Calling the function
print_order('Aman', 'masala')

This is called a function call.

The values you pass to the function are called arguments.

Here:

'Aman' is the first argument.
'masala' is the second argument.

Python matches the arguments to the parameters by their position:

Parameter	Argument
name	'Aman'
chai_type	'masala'

So inside the function, Python treats it as:

name = 'Aman'
chai_type = 'masala'

Then it executes:

print(f'{name} ordered {chai_type} chai!')

Output:

Aman ordered masala chai!
Step 4: Second function call
print_order('Hitesh', 'Ginger')

Python assigns:

Parameter	Argument
name	'Hitesh'
chai_type	'Ginger'

Output:

Hitesh ordered Ginger chai!
Step 5: Third function call
print_order('Jia', 'Tulsi')

Python assigns:

Parameter	Argument
name	'Jia'
chai_type	'Tulsi'

Output:

Jia ordered Tulsi chai!
Execution Flow
Program starts
      │
      ▼
Function is defined
      │
      ▼
print_order('Aman', 'masala')
      │
      ▼
name = "Aman"
chai_type = "masala"
      │
      ▼
Print:
"Aman ordered masala chai!"
      │
      ▼
print_order('Hitesh', 'Ginger')
      │
      ▼
name = "Hitesh"
chai_type = "Ginger"
      │
      ▼
Print:
"Hitesh ordered Ginger chai!"
      │
      ▼
print_order('Jia', 'Tulsi')
      │
      ▼
name = "Jia"
chai_type = "Tulsi"
      │
      ▼
Print:
"Jia ordered Tulsi chai!"
Final Output
Aman ordered masala chai!
Hitesh ordered Ginger chai!
Jia ordered Tulsi chai!
Parameters vs Arguments

This is one of the most important concepts in Python.

Parameters	Arguments
Declared in the function definition.	Passed when calling the function.
Act as placeholders for incoming values.	Actual values supplied to the function.
Example: name, chai_type	Example: 'Aman', 'masala'
Function Definition (Parameters)
def print_order(name, chai_type):

Here, name and chai_type are parameters.

Function Call (Arguments)
print_order('Aman', 'masala')

Here, 'Aman' and 'masala' are arguments.

Why use functions?

Without a function, you would have to write:

print('Aman ordered masala chai!')
print('Hitesh ordered Ginger chai!')
print('Jia ordered Tulsi chai!')

With a function, you write the printing logic only once and reuse it with different arguments. This makes your code:

Reusable – write once, use many times.
Readable – easier to understand.
Maintainable – if the message format changes, you only update it in one place.


'''