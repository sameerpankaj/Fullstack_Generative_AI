# def chai_report():
#     return 100, 200 # sold, remaining

# sold, remaining = chai_report()

# print('Sold ', sold)
# print('remaining: ', remaining)


# Define a function named 'chai_report'.
def chai_report():

    # Return two values from the function.
    # First value represents sold cups.
    # Second value represents remaining cups.
    return 100, 200   # sold, remaining


# Call the function and unpack the returned values.
# sold receives 100.
# remaining receives 200.
sold, remaining = chai_report()


# Print the value stored in 'sold'.
print('Sold ', sold)


# Print the value stored in 'remaining'.
print('remaining: ', remaining)


'''
Explanation

This example demonstrates:

Returning multiple values from a function
Tuple packing
Tuple unpacking
Step 1: Define the function
def chai_report():

A function named chai_report() is created.

Inside the function:

return 100, 200

Python allows returning multiple values separated by commas.

Step 2: How Python returns multiple values

This:

return 100, 200

is actually converted into a tuple:

(100, 200)

So the function returns:

(100, 200)

A tuple is an ordered collection of values.

Example:

chai_data = (100, 200)
Step 3: Call the function
sold, remaining = chai_report()

First, the function runs:

chai_report()

It returns:

(100, 200)

Then Python unpacks the tuple:

sold = 100
remaining = 200

Memory:

sold
 |
 ▼
100


remaining
 |
 ▼
200
Step 4: Print the values

First:

print('Sold ', sold)

Python replaces sold with:

100

Output:

Sold  100

Second:

print('remaining: ', remaining)

Python replaces remaining with:

200

Output:

remaining:  200
Execution Flow
Program starts
      |
      ▼
Define chai_report()
      |
      ▼
Call chai_report()
      |
      ▼
Return tuple:
(100, 200)
      |
      ▼
Unpack values:
sold = 100
remaining = 200
      |
      ▼
Print values
Final Output
Sold  100
remaining:  200
Without Unpacking

You could also write:

report = chai_report()

print(report)

Output:

(100, 200)

Here report stores the complete tuple.

More Examples
Returning three values
def chai_sales():
    return 100, 200, 50

morning, evening, night = chai_sales()

print(morning)
print(evening)
print(night)

Output:

100
200
50
Important Rule

The number of variables must match the number of returned values.

Correct:

sold, remaining = chai_report()

because:

2 values → 2 variables

Incorrect:

sold = chai_report()

because:

sold = (100, 200)

Now sold contains the whole tuple.

Key Concepts
Concept	Meaning
return	Sends data back from a function
Multiple return values	Python packs them into a tuple
Tuple	Ordered collection of values
Unpacking	Splitting tuple values into variables

In simple words:

sold, remaining = chai_report()

means:

"Run the function, receive two values, and store them separately in sold and remaining."

'''