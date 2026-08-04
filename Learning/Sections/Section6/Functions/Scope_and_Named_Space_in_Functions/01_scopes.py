# def serve_chai():
#     chai_type = 'Masala' #Local scope
#     print(f'Inside functions {chai_type}')


# chai_type = 'Lemon' #global scope
# serve_chai()
# print(f'Outside function {chai_type}')


# Define a function named 'serve_chai'.
def serve_chai():

    # Create a local variable named 'chai_type'.
    # This variable exists only inside this function.
    chai_type = 'Masala'  # Local scope

    # Print the value of the local variable.
    print(f'Inside function: {chai_type}')


# Create a global variable named 'chai_type'.
# This variable exists throughout the entire program.
chai_type = 'Lemon'  # Global scope


# Call the function.
# Python will use the local chai_type inside the function.
serve_chai()


# Print the global variable.
# Python uses the global chai_type because we are outside the function.
print(f'Outside function: {chai_type}')

'''
Explanation

This example demonstrates variable scope in Python.

Scope means the area of a program where a variable can be accessed.

Python mainly has:

Local scope → Variables created inside a function.
Global scope → Variables created outside all functions.
Step 1: Define the function
def serve_chai():

This creates a function called serve_chai.

The code inside the function does not run immediately. It runs only when we call:

serve_chai()
Step 2: Create a local variable

Inside the function:

chai_type = 'Masala'

This creates a local variable.

It belongs only to the function:

serve_chai()
     |
     └── chai_type = 'Masala'

You can access it inside the function:

print(chai_type)

But you cannot access it outside the function.

Example:

def serve_chai():
    chai_type = 'Masala'

serve_chai()

print(chai_type)

This would give:

NameError: name 'chai_type' is not defined

because the variable only exists inside the function.

Step 3: Create a global variable

Outside the function:

chai_type = 'Lemon'

This creates a global variable.

It belongs to the whole program:

Program
 |
 ├── chai_type = 'Lemon'
 |
 └── serve_chai()
        |
        └── chai_type = 'Masala'
Step 4: Call the function
serve_chai()

Python enters the function.

Inside the function:

print(f'Inside function {chai_type}')

Which chai_type does Python use?

It looks first in the local scope.

It finds:

chai_type = 'Masala'

So the output is:

Inside function Masala
Step 5: Print outside the function

After the function finishes:

print(f'Outside function {chai_type}')

Now Python is outside the function.

The local variable:

chai_type = 'Masala'

no longer exists.

Python looks in the global scope and finds:

chai_type = 'Lemon'

Output:

Outside function Lemon
Execution Flow
Program starts
      |
      ▼
Create function serve_chai()
      |
      ▼
Create global variable:
chai_type = "Lemon"
      |
      ▼
Call serve_chai()
      |
      ▼
Inside function:
Create local variable:
chai_type = "Masala"
      |
      ▼
Print:
Inside function Masala
      |
      ▼
Function ends
(local variable removed)
      |
      ▼
Print global variable:
Outside function Lemon
Final Output
Inside function Masala
Outside function Lemon
Important Concept: Same Variable Name, Different Variables

Even though both variables have the same name:

chai_type

they are different variables.

Local variable:
def serve_chai():
    chai_type = 'Masala'

Exists only inside the function.

Global variable:
chai_type = 'Lemon'

Exists throughout the program.

They do not overwrite each other.

What if we want to modify the global variable?

Normally, a function cannot change a global variable directly.

Example:

chai_type = 'Lemon'

def serve_chai():
    chai_type = 'Masala'

serve_chai()

print(chai_type)

Output:

Lemon

The function created a new local variable instead.

To modify the global variable, use global:

chai_type = 'Lemon'

def serve_chai():
    global chai_type
    chai_type = 'Masala'

serve_chai()

print(chai_type)

Output:

Masala
Key Concepts
Concept	Meaning	Example
Local scope	Variable inside a function	chai_type = 'Masala'
Global scope	Variable outside functions	chai_type = 'Lemon'
Function call	Runs the function	serve_chai()
Local variables override global variables inside functions	Python checks local scope first	Masala is printed inside
global keyword	Allows changing global variables	global chai_type

This concept is very important when working with larger Python programs because functions often create and manage their own local data.

'''