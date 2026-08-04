# def chai_counter():
#     chai_order = 'lemon' # Enclosing scope
#     def print_order():
#         chai_order = 'Ginger'
#         print('Inner', chai_order)
#     print_order()
#     print('Outer ', chai_order)


# chai_order = 'Tulsi' #Global scope
# chai_counter()
# print('Global:', chai_order)

# Define a function named 'chai_counter'.
def chai_counter():

    # Create a variable inside chai_counter().
    # This variable belongs to the enclosing scope
    # for the inner function print_order().
    chai_order = 'lemon'  # Enclosing scope


    # Define a nested function inside chai_counter().
    def print_order():

        # Create a new local variable named chai_order.
        # This belongs only to print_order().
        chai_order = 'Ginger'

        # Print the local chai_order from print_order().
        print('Inner', chai_order)


    # Call the inner function.
    print_order()


    # Print chai_order from the enclosing function scope.
    # This uses the chai_order defined inside chai_counter().
    print('Outer', chai_order)


# Create a global variable.
# This exists outside all functions.
chai_order = 'Tulsi'  # Global scope


# Call the outer function.
chai_counter()


# Print the global chai_order variable.
print('Global:', chai_order)


'''

Explanation

This example demonstrates nested functions and Python's LEGB scope rule.

Python searches for variables in this order:

L → E → G → B

Letter	Scope	Meaning
L	Local	Current function
E	Enclosing	Outer function containing the current function
G	Global	Outside all functions
B	Built-in	Python's built-in names
Program Structure

Your code has three levels of chai_order:

Global scope
│
└── chai_order = 'Tulsi'
│
└── chai_counter()
      │
      └── chai_order = 'lemon'  (Enclosing scope)
      │
      └── print_order()
              │
              └── chai_order = 'Ginger' (Local scope)

Although all variables have the same name, they are different variables.

Step 1: Create the outer function
def chai_counter():

Python creates a function called chai_counter.

The function does not run yet.

Step 2: Create enclosing variable

Inside chai_counter():

chai_order = 'lemon'

This variable belongs to the chai_counter() function.

It is called an enclosing variable because it surrounds the nested function print_order().

Step 3: Create the inner function
def print_order():

This creates another function inside chai_counter().

A function inside another function is called a nested function.

Step 4: Create local variable inside inner function

Inside print_order():

chai_order = 'Ginger'

This is a new variable.

It belongs only to print_order().

When Python sees:

print('Inner', chai_order)

it searches:

Local scope → finds 'Ginger'
Stops searching

So it prints:

Inner Ginger
Step 5: Call the inner function

Inside chai_counter():

print_order()

The inner function runs.

Execution:

print_order()
      |
      ▼
chai_order = 'Ginger'
      |
      ▼
print Inner Ginger

Output:

Inner Ginger
Step 6: Print from outer function

After print_order() finishes:

print('Outer', chai_order)

Now Python looks for chai_order.

It searches:

Local scope of chai_counter() ✅
Finds:
chai_order = 'lemon'

So it prints:

Outer lemon

It does not use:

chai_order = 'Ginger'

because that variable existed only inside print_order().

Step 7: Create global variable

Outside all functions:

chai_order = 'Tulsi'

This creates a global variable.

Step 8: Call chai_counter()
chai_counter()

Execution:

Global chai_order = Tulsi

chai_counter()
        |
        ▼
Enclosing chai_order = lemon
        |
        ▼
print_order()
        |
        ▼
Local chai_order = Ginger
Step 9: Print global variable

After chai_counter() finishes:

print('Global:', chai_order)

Python is outside all functions.

It uses the global variable:

chai_order = 'Tulsi'

Output:

Global: Tulsi
Complete Execution Flow
Program starts
      |
      ▼
Create global variable:
chai_order = "Tulsi"
      |
      ▼
Call chai_counter()
      |
      ▼
Create enclosing variable:
chai_order = "lemon"
      |
      ▼
Call print_order()
      |
      ▼
Create local variable:
chai_order = "Ginger"
      |
      ▼
Print:
Inner Ginger
      |
      ▼
Return to chai_counter()
      |
      ▼
Print:
Outer lemon
      |
      ▼
Function ends
      |
      ▼
Print global:
Global: Tulsi
Final Output
Inner Ginger
Outer lemon
Global: Tulsi
Important Concept: Variable Shadowing

This code demonstrates variable shadowing.

The same variable name exists at different levels:

chai_order = 'Tulsi'      # Global

chai_order = 'lemon'      # Enclosing

chai_order = 'Ginger'     # Local

The inner variable hides the outer variable temporarily.

Python always follows:

Local → Enclosing → Global → Built-in

So:

Inside print_order()

Python finds:

Ginger
Inside chai_counter()

Python finds:

lemon
Outside functions

Python finds:

Tulsi
Key Concepts
Local scope: Variable inside the current function.
Enclosing scope: Variable inside an outer function when using nested functions.
Global scope: Variable outside all functions.
Nested function: A function defined inside another function.
LEGB rule: Python's method for finding variables.
Shadowing: A variable with the same name in a smaller scope hides the outer variable.

'''