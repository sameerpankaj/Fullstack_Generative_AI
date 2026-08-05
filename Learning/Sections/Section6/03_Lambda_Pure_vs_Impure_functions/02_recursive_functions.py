# def pour_chai(n):
#     print(n)
#     if n == 0:
#         return 'All cups poured'
#     return pour_chai(n-1)

# print(pour_chai(3))



# Define a recursive function named 'pour_chai'.
# It takes one parameter 'n', which represents the number of cups left to pour.
def pour_chai(n):

    # Print the current value of n.
    print(n)

    # Base case:
    # If no cups are left (n == 0),
    # stop the recursion and return a message.
    if n == 0:
        return 'All cups poured'

    # Recursive case:
    # Call the same function again with one less cup.
    return pour_chai(n - 1)


# Call the function with n = 3 and print the final returned value.
print(pour_chai(3))


'''
Explanation

This example demonstrates recursion in Python.

A recursive function is a function that calls itself until a stopping condition (called the base case) is reached.

Step 1: Function Definition
def pour_chai(n):

A function named pour_chai() is created.

It accepts one parameter:

n

Here, n represents the number of cups left to pour.

Step 2: First Function Call
print(pour_chai(3))

Python calls:

pour_chai(3)

So:

n = 3
Step 3: Print the Current Value
print(n)

Output:

3
Step 4: Check the Base Case
if n == 0:

Is:

3 == 0

No.

So Python executes:

return pour_chai(n - 1)

which becomes:

return pour_chai(2)
Step 5: Second Call

Now Python enters:

pour_chai(2)

Prints:

2

Checks:

2 == 0

False.

Calls:

pour_chai(1)
Step 6: Third Call

Now:

pour_chai(1)

Prints:

1

Checks:

1 == 0

False.

Calls:

pour_chai(0)
Step 7: Base Case

Now:

pour_chai(0)

Prints:

0

Condition:

0 == 0

True.

So Python executes:

return 'All cups poured'

The recursion stops here.

Step 8: Returning Back

The returned value travels back through every previous function call.

pour_chai(0)
      │
      ▼
"All cups poured"
      │
      ▼
returned to pour_chai(1)
      │
      ▼
returned to pour_chai(2)
      │
      ▼
returned to pour_chai(3)
      │
      ▼
printed by print()
Execution Flow
pour_chai(3)
│
├── print(3)
│
└── pour_chai(2)
      │
      ├── print(2)
      │
      └── pour_chai(1)
            │
            ├── print(1)
            │
            └── pour_chai(0)
                  │
                  ├── print(0)
                  │
                  └── return "All cups poured"
Final Output
3
2
1
0
All cups poured
Understanding the Base Case

Every recursive function must have a base case.

Your base case is:

if n == 0:
    return 'All cups poured'

Without it, the function would keep calling itself forever until Python raises a RecursionError.

Example:

def bad_function():
    return bad_function()

Output:

RecursionError: maximum recursion depth exceeded
Understanding the Recursive Case

This line:

return pour_chai(n - 1)

means:

"Reduce the problem by one and let the function solve the smaller problem."

Each call reduces n:

3
↓
2
↓
1
↓
0

Eventually, the base case is reached.

Visual Representation
            pour_chai(3)
                 |
            print(3)
                 |
            pour_chai(2)
                 |
            print(2)
                 |
            pour_chai(1)
                 |
            print(1)
                 |
            pour_chai(0)
                 |
            print(0)
                 |
      return "All cups poured"
                 |
         Return to previous call
                 |
         Return to previous call
                 |
         Return to previous call
                 |
           print(final result)
Key Concepts
Concept	Meaning
Recursion	A function calling itself
Base case	The condition that stops recursion (n == 0)
Recursive case	The function calls itself with a smaller value (n - 1)
return	Sends the final result back through all recursive calls
In simple words

Your function is saying:

Start with 3 cups.
Pour one cup and reduce the count.
Keep repeating until no cups are left.
**When n becomes 0, stop and return "All cups poured"."

'''