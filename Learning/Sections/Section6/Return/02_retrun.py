# def make_chai():
#     return 'Here is your masala chai'

# return_value = make_chai()
# print(return_value)


# Define a function named 'make_chai'.
def make_chai():

    # Return a string value from the function.
    # The returned value will be sent back to the caller.
    return 'Here is your masala chai'


# Call the function and store the returned value
# in a variable named 'return_value'.
return_value = make_chai()


# Print the value stored in the variable.
print(return_value)


'''
Explanation

This example shows how to store a function's return value in a variable.

The function does not directly print anything. Instead, it returns a value, and we decide what to do with that value.

Step 1: Define the function
def make_chai():

This creates a function called make_chai.

At this point, Python only creates the function. It does not execute the code inside it.

Step 2: Return a value

Inside the function:

return 'Here is your masala chai'

The return statement sends a value back.

The function produces:

Here is your masala chai

But it does not display it yet.

Step 3: Call the function and store the result
return_value = make_chai()

This line has two actions:

1. Run the function

Python executes:

make_chai()

The function returns:

'Here is your masala chai'
2. Store the returned value

Python assigns:

return_value = 'Here is your masala chai'

Now the variable contains the returned message.

Memory:

return_value
      |
      ▼
"Here is your masala chai"
Step 4: Print the variable
print(return_value)

Python prints the value stored inside return_value.

Output:

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
return "Here is your masala chai"
      |
      ▼
Store in return_value
      |
      ▼
print(return_value)
      |
      ▼
Display message
Final Output
Here is your masala chai
Difference Between This and Previous Example
Previous:
print(make_chai())

Flow:

Function runs
      ↓
Returns value
      ↓
Print immediately
Current:
return_value = make_chai()
print(return_value)

Flow:

Function runs
      ↓
Returns value
      ↓
Store value in variable
      ↓
Use variable later
      ↓
Print value
Why store return values?

Storing the result allows you to reuse it.

Example:

chai = make_chai()

print(chai)
print(chai.upper())

Output:

Here is your masala chai
HERE IS YOUR MASALA CHAI
Key Concepts
Concept	Meaning
def	Creates a function
return	Sends a value back from a function
Function call	Executes the function
Variable assignment	Stores the returned value
print()	Displays the stored value

So this line:

return_value = make_chai()

means:

"Run make_chai(), take the returned message, and save it inside return_value."

'''


