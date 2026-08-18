# def chai_flavor(flavor='masala'):
#     '''Return the flavor of chai.'''


#     return flavor

# print(chai_flavor.__doc__)

# print(chai_flavor.__name__)

# 

# Define a function named chai_flavor.
# The function has one parameter called "flavor".
# If no value is provided for flavor, it will automatically use "masala".
def chai_flavor(flavor='masala'):

    # This is the docstring of the function.
    # It describes what the function does.
    '''Return the flavor of chai.'''

    # Return the value stored in the "flavor" parameter.
    return flavor


# __doc__ is a special attribute that stores the function's docstring.
# This prints: Return the flavor of chai.
print(chai_flavor.__doc__)


# __name__ is a special attribute that stores the function's name.
# This prints: chai_flavor
print(chai_flavor.__name__)


'''

Now let's understand it step by step
Step 1: Create the function
def chai_flavor(flavor='masala'):

You're creating a function called chai_flavor.

It accepts one parameter:

flavor

And you've given it a default value:

'masala'

Therefore:

chai_flavor()

means:

chai_flavor('masala')

automatically.

Step 2: The docstring
Return the flavor of chai.

This is a docstring.

It is documentation explaining what the function is supposed to do.

Python automatically stores this text in:

chai_flavor.__doc__

Therefore:

print(chai_flavor.__doc__)

prints:

Return the flavor of chai.
Step 3: Return the flavor
return flavor

This tells Python:

"Give back whatever value is currently stored in flavor."

For example:

chai_flavor()

returns:

masala

And:

chai_flavor('ginger')

returns:

ginger
Step 4: __doc__
chai_flavor.__doc__

__doc__ is a special attribute that contains the function's documentation.

So:

print(chai_flavor.__doc__)

gives:

Return the flavor of chai.
Step 5: __name__
chai_flavor.__name__

__name__ is another special attribute.

It contains the name of the function.

So:

print(chai_flavor.__name__)

gives:

chai_flavor
Final output
Return the flavor of chai.
chai_flavor
🧠 The key idea

You can think of the function as having information attached to it:

chai_flavor
    │
    ├── __name__ → "chai_flavor"
    │
    └── __doc__  → "Return the flavor of chai."

While calling the function:

chai_flavor()

actually executes the function and returns:

masala

So remember:

() → call/run the function
.__name__ → function's name
.__doc__ → function's documentation

'''