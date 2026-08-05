# def idle_chaiwala():
#     pass

# print(idle_chaiwala())

# Define a function named 'idle_chaiwala'.
def idle_chaiwala():

    # 'pass' is a placeholder statement.
    # It tells Python to do nothing inside this function.
    # It prevents an error when the function body is empty.
    pass


# Call the function and print its returned value.
print(idle_chaiwala())


'''
Explanation

This example demonstrates the use of the pass statement in Python.

pass means:

"Do nothing for now, but keep this code structure valid."

It is commonly used when you want to create a function, class, or condition that you will complete later.

Step 1: Define the function
def idle_chaiwala():

This creates a function named idle_chaiwala.

Normally, a function must have some code inside it.

For example:

def make_chai():
    print("Making chai")

But an empty function like this:

def idle_chaiwala():

would cause an error because Python expects an indented block after :.

Step 2: Using pass
pass

The pass statement tells Python:

"There is no action here yet."

It allows the function to exist without doing anything.

Example:

def idle_chaiwala():
    pass

is valid Python code.

Step 3: Calling the function
idle_chaiwala()

The function runs.

Inside the function:

pass

does nothing.

The function finishes without a return statement.

Step 4: Understanding the output

Your code:

print(idle_chaiwala())

works like this:

First:

idle_chaiwala()

runs.

Because there is no return, Python automatically returns:

None

Then:

print(None)

prints:

None
Final Output
None
Execution Flow
Program starts
      |
      ▼
Define idle_chaiwala()
      |
      ▼
Call idle_chaiwala()
      |
      ▼
Execute pass
      |
      ▼
No return statement
      |
      ▼
Return None
      |
      ▼
print(None)
      |
      ▼
Output:
None
Why Use pass?
1. Creating a function for future work

Example:

def calculate_bill():
    pass

Later you can add:

def calculate_bill():
    return price * quantity
2. Placeholder in conditions

Example:

age = 20

if age >= 18:
    pass
else:
    print("Not allowed")

The program is valid even though the if block has no action yet.

3. Placeholder in loops

Example:

for item in range(5):
    pass

The loop runs but does nothing.

Difference Between pass, return, and print
Statement	Purpose	Example Result
pass	Do nothing	No output
print()	Display something	Shows text
return	Send a value back	Gives a result
Example Comparison
pass
def chai():
    pass

Output:

Nothing
print
def chai():
    print("Masala chai")

Output:

Masala chai
return
def chai():
    return "Masala chai"

print(chai())

Output:

Masala chai
Key Concepts
pass is an empty placeholder.
It keeps Python syntax valid.
A function without return automatically returns None.
print(idle_chaiwala()) prints None because the function does not return any value.


'''