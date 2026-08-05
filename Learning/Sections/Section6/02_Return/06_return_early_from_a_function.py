# def chai_status(cups_left):
#     if cups_left == 0:
#         return 'Sorry, Chai Over'
#     return 'Chai is ready'
#     print('chai')



# print(chai_status(0))
# print(chai_status(5))


# Define a function named 'chai_status'.
# It takes one parameter: cups_left.
def chai_status(cups_left):

    # Check if there are no cups left.
    if cups_left == 0:

        # Return this message and immediately exit the function.
        return 'Sorry, Chai Over'


    # If cups_left is not 0, this line executes.
    # Return this message and exit the function.
    return 'Chai is ready'


    # This line will NEVER execute because it comes after return.
    # Once Python reaches return, the function stops.
    print('chai')



# Call the function with cups_left = 0.
# The if condition is True, so it returns "Sorry, Chai Over".
print(chai_status(0))


# Call the function with cups_left = 5.
# The if condition is False, so it returns "Chai is ready".
print(chai_status(5))


'''
Explanation

This example demonstrates:

Conditional return (if + return)
Function execution flow
Why code after return does not run
Step 1: Function Definition
def chai_status(cups_left):

A function named chai_status() is created.

It accepts one input:

cups_left

This parameter tells the function how many cups are remaining.

Step 2: First Function Call
print(chai_status(0))

Python sends:

cups_left = 0

Inside the function:

if cups_left == 0:

Condition:

0 == 0 → True

So Python executes:

return 'Sorry, Chai Over'

The function immediately stops.

Returned value:

Sorry, Chai Over

Then:

print()

displays it.

Output:

Sorry, Chai Over
Step 3: Second Function Call
print(chai_status(5))

Python sends:

cups_left = 5

Condition:

if cups_left == 0:

Checking:

5 == 0 → False

The if block is skipped.

Python reaches:

return 'Chai is ready'

The function stops and returns:

Chai is ready

Then print() displays it.

Output:

Chai is ready
Why Does print('chai') Never Run?

Your code:

return 'Chai is ready'

print('chai')

The print() is after return.

When Python reaches:

return 'Chai is ready'

it does two things:

Sends the value back.
Ends the function immediately.

So this code:

print('chai')

is unreachable.

Example:

def test():
    return 10
    print("Hello")

Output:

10

"Hello" is never printed.

Execution Flow

For chai_status(0):

Call function
      |
      ▼
cups_left = 0
      |
      ▼
Is cups_left == 0?
      |
      ▼
Yes
      |
      ▼
return "Sorry, Chai Over"
      |
      ▼
Function ends

For chai_status(5):

Call function
      |
      ▼
cups_left = 5
      |
      ▼
Is cups_left == 0?
      |
      ▼
No
      |
      ▼
return "Chai is ready"
      |
      ▼
Function ends
Final Output
Sorry, Chai Over
Chai is ready
Important Rule About return

Whenever Python executes a return statement:

✅ Function stops immediately
✅ Value is sent back
❌ Remaining code inside the function does not run

Example:

def make_chai():
    print("Making chai")
    return "Ready"
    print("Serve chai")

Output:

Making chai
Ready

Serve chai never appears because it is after return.

Key Concepts
Concept	Meaning
Parameter	Input received by a function (cups_left)
if condition	Makes a decision
return	Sends value back and stops function
Unreachable code	Code that can never execute
Function call	Runs the function

Your function is correctly written; the only unnecessary part is:

print('chai')

because it can never execute.

'''

