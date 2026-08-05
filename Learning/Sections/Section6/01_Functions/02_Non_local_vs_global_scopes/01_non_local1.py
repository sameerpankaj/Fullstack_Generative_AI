
# chai_type = 'ginger'

# def update_order():
#     chai_type = 'Elaichi'
#     def kitchen():
#         global chai_type
#         chai_type = 'Kesar'
#     kitchen()
#     print('After kitchen update', chai_type)

# update_order()


# Create a global variable named chai_type.
# This variable belongs to the global scope.
chai_type = 'ginger'


# Define the outer function.
def update_order():

    # Create a local variable inside update_order().
    # This variable belongs only to update_order().
    chai_type = 'Elaichi'


    # Define a nested function inside update_order().
    def kitchen():

        # Tell Python to use the global chai_type variable,
        # not the chai_type variable from update_order().
        global chai_type

        # Modify the global variable.
        chai_type = 'Kesar'


    # Call the nested function.
    kitchen()


    # Print the chai_type from update_order()'s local scope.
    print('After kitchen update', chai_type)


# Call the outer function.
update_order()


'''
Explanation

This example demonstrates the difference between:

Global scope
Local scope
Nested function scope
global keyword
Scope Structure

Your program has two variables with the same name:

Global Scope
│
└── chai_type = 'ginger'
│
└── update_order()
       │
       └── chai_type = 'Elaichi'  (Local scope)
       │
       └── kitchen()
              │
              └── global chai_type
                    changes global value to 'Kesar'
Step 1: Create global variable
chai_type = 'ginger'

This creates a global variable.

Current value:

Global chai_type = "ginger"
Step 2: Call update_order()
update_order()

Python enters the function.

Step 3: Create local variable inside update_order()

Inside the function:

chai_type = 'Elaichi'

This creates a new local variable.

Now memory looks like:

Global:
chai_type = "ginger"

update_order():
chai_type = "Elaichi"

The local variable does not replace the global one.

Step 4: Execute the nested function

Inside update_order():

kitchen()

Python enters kitchen().

Step 5: Use global chai_type

Inside kitchen():

global chai_type

This is the important part.

It tells Python:

"When I use chai_type here, use the global variable, not the local variable from update_order()."

So this line:

chai_type = 'Kesar'

changes:

Global:
Before → ginger
After  → Kesar

It does not change:

update_order():
chai_type = "Elaichi"
Step 6: Return to update_order()

After kitchen() finishes:

print('After kitchen update', chai_type)

Now Python looks for chai_type.

According to the LEGB rule:

Local scope of update_order() ✅
Enclosing scope
Global scope

It finds:

chai_type = 'Elaichi'

So it prints:

After kitchen update Elaichi
Step 7: What happened to the global variable?

The global variable has changed:

Before:

chai_type = "ginger"

After kitchen():

chai_type = "Kesar"

However, we never print it after calling update_order().

If we add:

print(chai_type)

at the end, the output would be:

After kitchen update Elaichi
Kesar
Execution Flow
Program starts
      |
      ▼
Global chai_type = "ginger"
      |
      ▼
Call update_order()
      |
      ▼
Create local chai_type = "Elaichi"
      |
      ▼
Call kitchen()
      |
      ▼
global chai_type
      |
      ▼
Change global chai_type:
"ginger" → "Kesar"
      |
      ▼
Return to update_order()
      |
      ▼
Print local chai_type:
"Elaichi"
Final Output of Your Code
After kitchen update Elaichi
Important Lesson

Even though kitchen() changes the global variable:

global chai_type
chai_type = 'Kesar'

the outer function still has its own local variable:

chai_type = 'Elaichi'

The two variables are separate.

Location	Value
Global scope	Kesar
update_order() local scope	Elaichi
Before running program	ginger
If you wanted to update update_order()'s variable instead

You should use nonlocal, not global:

chai_type = 'ginger'

def update_order():
    chai_type = 'Elaichi'

    def kitchen():
        nonlocal chai_type
        chai_type = 'Kesar'

    kitchen()
    print('After kitchen update', chai_type)

update_order()

Output:

After kitchen update Kesar

because nonlocal modifies the outer function's variable.

'''
