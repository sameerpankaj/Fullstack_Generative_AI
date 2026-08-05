# def sold_cups():
#     return 120

# total = sold_cups()
# print(total)


# Define a function named 'sold_cups'.
def sold_cups():

    # Return the number of cups sold.
    # The function sends the value 120 back to the caller.
    return 120


# Call the function and store the returned value
# in the variable 'total'.
total = sold_cups()


# Print the value stored in 'total'.
print(total)


'''
Explanation

This example demonstrates how a function can calculate or provide a value and return it to the program.

Step 1: Define the function
def sold_cups():

This creates a function called sold_cups.

At this point, Python only creates the function. The code inside it does not execute yet.

Step 2: Return a value

Inside the function:

return 120

The return statement sends the value:

120

back to wherever the function is called.

The function's job is:

"Give me the number of cups sold."

Step 3: Call the function
total = sold_cups()

Python executes the function.

Flow:

sold_cups()
      |
      ▼
return 120
      |
      ▼
total = 120

Now the variable contains:

total = 120
Step 4: Print the result
print(total)

Python displays the value stored in total.

Output:

120
Execution Flow
Program starts
      |
      ▼
Define sold_cups()
      |
      ▼
Call sold_cups()
      |
      ▼
Function returns 120
      |
      ▼
Store value:
total = 120
      |
      ▼
print(total)
      |
      ▼
Output:
120
Final Output
120
Why use return instead of print?
Using print
def sold_cups():
    print(120)

total = sold_cups()
print(total)

Output:

120
None

Because the function only displayed the value; it did not give it back.

Using return
def sold_cups():
    return 120

total = sold_cups()
print(total)

Output:

120

The returned value can be:

stored in a variable
used in calculations
passed to another function
Example: Using the Returned Value
cups = sold_cups()

revenue = cups * 5

print(revenue)

Calculation:

120 × 5 = 600

Output:

600
Key Concepts
Concept	Meaning
def	Creates a function
Function call	Runs the function
return	Sends a value back
Variable assignment	Stores returned value
print()	Displays the value

In simple words:

total = sold_cups()

means:

"Run the function, take the returned number, and store it in total."

'''