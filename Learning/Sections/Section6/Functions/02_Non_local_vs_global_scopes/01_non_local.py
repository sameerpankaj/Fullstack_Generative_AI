# def update_order():
#     chai_type = 'Elaichi'
#     def kitchen():
#         nonlocal chai_type
#         chai_type = 'Kesar'
#     kitchen()
#     print('After kitchen update', chai_type)

# update_order()

# Define a function named 'update_order'.
def update_order():

    # Create a variable inside the outer function.
    # This variable belongs to the enclosing scope.
    chai_type = 'Elaichi'


    # Define a nested function inside update_order().
    def kitchen():

        # The 'nonlocal' keyword tells Python:
        # "Use the chai_type variable from the outer function,
        # not create a new local variable."
        nonlocal chai_type

        # Update the enclosing function's chai_type variable.
        chai_type = 'Kesar'


    # Call the inner function.
    kitchen()


    # Print the updated value of chai_type from the outer function.
    print('After kitchen update', chai_type)


# Call the function to start execution.
update_order()


'''
Explanation

This example demonstrates the nonlocal keyword in Python.

nonlocal is used when a nested function needs to modify a variable from its enclosing (outer) function.

Program Structure

Your code has two scopes:

update_order()  ← Outer function
│
├── chai_type = 'Elaichi'  ← Enclosing variable
│
└── kitchen()  ← Inner function
       │
       └── modifies chai_type using nonlocal
Step 1: Create the outer function
def update_order():

This creates a function named update_order.

The function does not run until we call:

update_order()
Step 2: Create the enclosing variable

Inside update_order():

chai_type = 'Elaichi'

A variable is created:

chai_type = "Elaichi"

This variable belongs to update_order().

It is not global and not local to kitchen().

It is called an enclosing variable.

Step 3: Create the inner function
def kitchen():

This creates a nested function.

kitchen() can access variables from update_order().

Step 4: Understanding nonlocal

Inside kitchen():

nonlocal chai_type

This line is very important.

Without nonlocal, Python would create a new local variable.

Example without nonlocal:

def update_order():
    chai_type = 'Elaichi'

    def kitchen():
        chai_type = 'Kesar'

    kitchen()
    print(chai_type)

Output:

Elaichi

Why?

Because:

chai_type = 'Kesar'

creates a new variable inside kitchen().

It does not change the outer variable.

With nonlocal:

nonlocal chai_type

Python understands:

"I want to modify the chai_type variable from the outer function."

So this:

chai_type = 'Kesar'

changes:

Before:
chai_type = "Elaichi"

After:
chai_type = "Kesar"
Step 5: Calling the inner function
kitchen()

Execution:

Before calling:

chai_type = "Elaichi"

Inside kitchen():

chai_type = "Kesar"

Because of nonlocal, the outer variable is updated.

Now:

chai_type = "Kesar"
Step 6: Print the updated value
print('After kitchen update', chai_type)

The outer function now sees:

chai_type = 'Kesar'

So output:

After kitchen update Kesar
Execution Flow
Program starts
      |
      ▼
Call update_order()
      |
      ▼
Create:
chai_type = "Elaichi"
      |
      ▼
Call kitchen()
      |
      ▼
nonlocal chai_type
      |
      ▼
Change outer variable:
chai_type = "Kesar"
      |
      ▼
Return to update_order()
      |
      ▼
Print:
After kitchen update Kesar
Final Output
After kitchen update Kesar
Difference Between Local, Nonlocal, and Global
Keyword	Scope	Can modify?
Local variable	Inside current function	Yes
nonlocal	Variable in outer function	Yes
global	Variable outside all functions	Yes
Example Comparison
Local
def kitchen():
    chai_type = "Kesar"

Creates a new variable only inside kitchen().

Nonlocal
def kitchen():
    nonlocal chai_type
    chai_type = "Kesar"

Changes the variable from the outer function.

Global
global chai_type
chai_type = "Kesar"

Changes a variable outside all functions.

Key Concepts
Nested functions can access variables from their outer functions.
nonlocal allows an inner function to modify an enclosing function's variable.
Without nonlocal, Python creates a new local variable.
nonlocal works only with variables from an enclosing function, not global variables.
The output is:
After kitchen update Kesar


'''
