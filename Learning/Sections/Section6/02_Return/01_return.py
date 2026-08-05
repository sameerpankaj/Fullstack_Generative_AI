# def make_chai():
#     return 'Here is your masala chai'


# print(make_chai())


# Define a function named 'make_chai'.
def make_chai():

    # Return a string value from the function.
    # The function sends this message back to where it was called.
    return 'Here is your masala chai'


# Call the function and print the value returned by the function.
print(make_chai())


'''

Explanation

This example demonstrates the return statement in Python.

A function can either:

Perform an action (for example, print something)
Return a value back to the caller

Here, the function returns a message.

Step 1: Define the function
def make_chai():

This creates a function called make_chai.

At this point, Python only remembers the function.

The function does not run yet.

Step 2: Return a value

Inside the function:

return 'Here is your masala chai'

The return statement does two things:

Stops the function execution.
Sends the value back to the place where the function was called.

The function produces:

Here is your masala chai
Step 3: Call the function
make_chai()

When Python sees this:

It enters the function.
Runs the return statement.
Gets the returned value.

The function call becomes:

'Here is your masala chai'
Step 4: Print the returned value

Your code:

print(make_chai())

works like this:

First:

make_chai()

returns:

'Here is your masala chai'

Then:

print('Here is your masala chai')

prints:

Here is your masala chai
Execution Flow
Program starts
      |
      ▼
Define make_chai()
      |
      ▼
Call make_chai()
      |
      ▼
Execute return statement
      |
      ▼
Return:
"Here is your masala chai"
      |
      ▼
print() displays the returned value
Final Output
Here is your masala chai
Difference Between print() and return

This is an important Python concept.

Using print()
def make_chai():
    print('Here is your masala chai')

result = make_chai()
print(result)

Output:

Here is your masala chai
None

Why?

Because the function printed the message but did not return anything.

Using return
def make_chai():
    return 'Here is your masala chai'

result = make_chai()
print(result)

Output:

Here is your masala chai

The value can be stored, reused, or passed to another function.

Example: Storing the Return Value
chai = make_chai()

print(chai)

Python does:

chai = 'Here is your masala chai'

Then:

print(chai)

Output:

Here is your masala chai
Key Concepts
Concept	Meaning
def	Creates a function
Function call	Runs the function
return	Sends a value back
print()	Displays a value on the screen
Returned value	Can be stored in a variable

In short:

print(make_chai())

means:

"Run the function → get the returned message → print that message."

'''