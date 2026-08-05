# def chai_report():
#     return 100, 20, 10 # sold, remaining

# sold, remaining, not_paid = chai_report()

# print('Sold ', sold)
# print('remaining: ', remaining)


# Define a function named 'chai_report'.
def chai_report():

    # Return three values from the function.
    # 1st value = sold cups
    # 2nd value = remaining cups
    # 3rd value = unpaid orders
    return 100, 20, 10


# Call the function and unpack the returned values.
# sold receives 100
# remaining receives 20
# not_paid receives 10
sold, remaining, not_paid = chai_report()


# Print the number of sold cups.
print('Sold ', sold)


# Print the remaining cups.
print('remaining: ', remaining)


'''
Explanation

This example demonstrates returning multiple values and unpacking them into variables.

Step 1: Define the function
def chai_report():

A function named chai_report() is created.

The function is not executed yet.

Step 2: Return multiple values

Inside the function:

return 100, 20, 10

Python treats multiple returned values as a tuple.

It is equivalent to:

return (100, 20, 10)

The function returns:

(100, 20, 10)
Step 3: Call the function
sold, remaining, not_paid = chai_report()

First, the function runs:

chai_report()

It returns:

(100, 20, 10)

Then Python unpacks the tuple:

sold       = 100
remaining  = 20
not_paid   = 10

It is the same as writing:

sold = 100
remaining = 20
not_paid = 10
Step 4: Print the values
First print:
print('Sold ', sold)

sold contains:

100

Output:

Sold  100
Second print:
print('remaining: ', remaining)

remaining contains:

20

Output:

remaining: 20
What About not_paid?

You returned:

10

and stored it:

not_paid = 10

But you never printed it.

If you add:

print('Not paid:', not_paid)

Output becomes:

Sold  100
remaining: 20
Not paid: 10
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
(100, 20, 10)
      |
      ▼
Unpack:
sold = 100
remaining = 20
not_paid = 10
      |
      ▼
Print sold and remaining
Important Rule: Number of Variables Must Match

Your code:

sold, remaining, not_paid = chai_report()

works because:

3 returned values
=
3 variables
Example of Error
sold, remaining = chai_report()

Python gives:

ValueError: too many values to unpack

because:

3 values returned
but only 2 variables
Key Concepts
Concept	Meaning
return 100, 20, 10	Returns multiple values
Tuple	Python groups returned values together
Unpacking	Separating tuple values into variables
sold	Receives first value
remaining	Receives second value
not_paid	Receives third value

In simple words:

sold, remaining, not_paid = chai_report()

means:

"Run the function, take the three returned values, and store them separately in three variables."


'''