# def make_chai():
#     # return 'Here is your masala chai'
#     print('Here is your masala chai')

# return_value = make_chai()

# print(return_value)


# Define a function named 'make_chai'.
def make_chai():

    # This line is commented out, so Python ignores it.
    # It would return a value if it were active.
    # return 'Here is your masala chai'


    # Print the message on the screen.
    # This displays the text but does not send a value back.
    print('Here is your masala chai')


# Call the function and store its returned value
# in the variable 'return_value'.
return_value = make_chai()


# Print the value stored in 'return_value'.
print(return_value)


'''

Explanation

This example demonstrates the important difference between print() and return.

Step 1: Define the function
def make_chai():

A function named make_chai() is created.

The function does not run immediately.

Step 2: Inside the function

You have:

# return 'Here is your masala chai'

This line is commented.

Because of #, Python ignores it.

If it were active:

return 'Here is your masala chai'

the function would send the value back.

Instead, you have:

print('Here is your masala chai')

This only displays text.

It does not return anything.

Step 3: Call the function
return_value = make_chai()

Python executes the function.

Inside the function:

print('Here is your masala chai')

prints:

Here is your masala chai

After printing, the function finishes.

Since there is no return statement, Python automatically returns:

None

So this line becomes:

return_value = None
Step 4: Print the returned value

Now Python executes:

print(return_value)

But:

return_value = None

So it prints:

None
Final Output
Here is your masala chai
None
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
Print:
"Here is your masala chai"
      |
      ▼
No return statement found
      |
      ▼
Python returns None
      |
      ▼
return_value = None
      |
      ▼
print(return_value)
      |
      ▼
Print:
None
Difference Between print() and return
Using print()
def make_chai():
    print('Masala chai')

Purpose:

Shows something on the screen.
Does not give a value back.

Example:

result = make_chai()

result becomes:

None
Using return
def make_chai():
    return 'Masala chai'

Purpose:

Sends a value back.
Can be stored and reused.

Example:

result = make_chai()

Now:

result = 'Masala chai'
Simple Analogy

Imagine ordering chai:

print()

The chai seller shouts:

"Your masala chai is ready!"

You hear it, but you don't receive anything to use later.

return

The seller gives you the actual chai cup.

You can:

drink it
store it
pass it to someone else
Key Concepts
Feature	print()	return
Displays output	✅ Yes	❌ No
Sends value back	❌ No	✅ Yes
Can store result	❌ No	✅ Yes
Default function result	None	Returned value

So in your code:

return_value = make_chai()

stores:

None

because the function prints the message but does not return it.

'''