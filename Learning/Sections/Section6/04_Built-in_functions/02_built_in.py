# 


# Define a function named "chai_flavor".
# It has one parameter called "flavor".
# If no flavor is provided when calling the function,
# the default value "masala" will be used.
def chai_flavor(flavor='masala'):

    # This is the function's docstring.
    # It describes what the function does.
    """Return the flavor of chai."""

    # Create a local variable called "chai"
    # and store the value "ginger" in it.
    chai = "ginger"

    # Return the value of the "flavor" parameter.
    # Notice that we are NOT returning the "chai" variable.
    return flavor


# Access the function's __doc__ attribute.
# It contains the docstring written inside the function.
print(chai_flavor.__doc__)


# Access the function's __name__ attribute.
# It contains the name of the function.
print(chai_flavor.__name__)


'''
What happens when Python runs this?

First, Python defines the function:

def chai_flavor(flavor='masala'):

At this point, Python knows:

Function name → chai_flavor
Parameter → flavor
Default value → 'masala'

Then Python sees:

"""Return the flavor of chai."""

This becomes the function's docstring.

You can access it using:

chai_flavor.__doc__
3. What about chai = "ginger"?

This line:

chai = "ginger"

creates a variable called chai.

However, it has no effect on the result, because you don't return chai.

You return:

return flavor

So if you actually called:

print(chai_flavor())

the result would be:

masala

not:

ginger

Why?

Because:

flavor → "masala"
chai   → "ginger"

and the function says:

return flavor

Therefore, "masala" is returned.

If you changed it to:

return chai

then:

print(chai_flavor())

would produce:

ginger
4. Understanding __doc__

This:

print(chai_flavor.__doc__)

prints the function's documentation.

Output:

Return the flavor of chai.

The docstring is useful because you can document your functions and later inspect their documentation.

5. Understanding __name__

This:

print(chai_flavor.__name__)

asks Python:

"What is the name of this function?"

Output:

chai_flavor
Final output

Your code produces:

Return the flavor of chai.
chai_flavor
⭐ Important point to remember

There are three different things inside your function:

def chai_flavor(flavor='masala'):
    """Return the flavor of chai."""
    chai = "ginger"
    return flavor
Code	Purpose
flavor='masala'	Parameter with a default value
"""Return..."""	Docstring/documentation
chai = "ginger"	Local variable
return flavor	Returns the value of flavor

And outside the function:

chai_flavor.__doc__

→ gets the documentation

chai_flavor.__name__

→ gets the function name

One subtle but important lesson: chai = "ginger" is created every time the function runs, but because you never use or return it, it doesn't affect the output.

'''