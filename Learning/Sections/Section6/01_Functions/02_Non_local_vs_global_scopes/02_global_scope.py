# chai_type = 'plain'

# def front_desk():
#     def kitchen():
#         global chai_type
#         chai_type = 'Irani'

#     kitchen()


# front_desk()
# print('Final global chai: ', chai_type)


# Create a global variable named 'chai_type'.
# This variable is accessible throughout the program.
chai_type = 'plain'   # Global scope


# Define a function named 'front_desk'.
def front_desk():

    # Define a nested function inside front_desk().
    def kitchen():

        # The 'global' keyword tells Python:
        # "Use the global chai_type variable, not create a new local variable."
        global chai_type

        # Modify the global variable.
        chai_type = 'Irani'


    # Call the inner function.
    kitchen()


# Call the outer function.
front_desk()


# Print the updated global variable.
print('Final global chai:', chai_type)


'''

Explanation

This example demonstrates the global keyword in Python.

The global keyword allows a function (even a nested function) to modify a variable that exists outside all functions.

Program Structure

The scopes in this program are:

Global Scope
│
└── chai_type = 'plain'
│
└── front_desk()
       │
       └── kitchen()
              │
              └── global chai_type
                    changes it to 'Irani'
Step 1: Create a global variable
chai_type = 'plain'

This variable is created outside any function.

It is a global variable.

Currently:

chai_type = "plain"

It can be accessed anywhere in the program.

Step 2: Define front_desk()
def front_desk():

This creates a function.

Inside it, another function is created:

def kitchen():

This is called a nested function.

Step 3: Understand the global keyword

Inside kitchen():

global chai_type

This tells Python:

"Do not create a new local variable called chai_type. Use the global variable instead."

Without global, Python would create a new local variable.

Example without global:

def kitchen():
    chai_type = 'Irani'

Here:

Global:
chai_type = "plain"

Kitchen:
chai_type = "Irani"

They would be two different variables.

The global value would remain:

plain
Step 4: Modify the global variable

With:

global chai_type

this line:

chai_type = 'Irani'

changes the global variable.

Before:

chai_type = "plain"

After:

chai_type = "Irani"
Step 5: Execute the functions

The program calls:

front_desk()

Inside front_desk():

kitchen()

runs.

Inside kitchen():

global chai_type
chai_type = 'Irani'

The global variable is updated.

Step 6: Print the final value

After:

front_desk()

Python executes:

print('Final global chai:', chai_type)

Now the global variable contains:

chai_type = 'Irani'

So the output is:

Final global chai: Irani
Execution Flow
Program starts
      |
      ▼
Create global variable:
chai_type = "plain"
      |
      ▼
Call front_desk()
      |
      ▼
Call kitchen()
      |
      ▼
global chai_type
      |
      ▼
Change global value:
chai_type = "Irani"
      |
      ▼
Return to main program
      |
      ▼
Print:
Final global chai: Irani
Final Output
Final global chai: Irani
Difference Between global and nonlocal
Keyword	Used for	Example
global	Modify a variable outside all functions	Global variable
nonlocal	Modify a variable in an outer function	Nested function variable

Example:

global
chai_type = "plain"

def kitchen():
    global chai_type
    chai_type = "Irani"

Changes the variable outside all functions.

nonlocal
def front_desk():
    chai_type = "plain"

    def kitchen():
        nonlocal chai_type
        chai_type = "Irani"

Changes the variable in the enclosing function.

Key Concepts
Global scope: Variables created outside functions.
Local scope: Variables created inside a function.
Nested function: A function inside another function.
global keyword: Allows modification of global variables inside functions.
Without global, assignment inside a function creates a new local variable.
Output:


'''