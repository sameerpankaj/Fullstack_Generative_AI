'''
```
You sell different chai sizes.
Instead of writing formulas everywhere, create a function.
Task:
  .Write calculate_bill(cups, price_per_cup)
  .Return total bill
  .Use this function for miltiple orders

```



'''

# def calulate_bills(cups, price_per_cup):
#     return cups * price_per_cup

# my_bill = calulate_bills(3, 15)
# print(my_bill)

# # print('order for table 2:', calulate_bills(2, 50))

# Define a function named 'calculate_bills'.
# It accepts two parameters:
# 1. cups - the number of cups purchased
# 2. price_per_cup - the price of one cup
def calulate_bills(cups, price_per_cup):

    # Calculate the total bill and return the result.
    return cups * price_per_cup


# Call the function with two arguments:
# cups = 3
# price_per_cup = 15
# Store the returned value in the variable 'my_bill'.
my_bill = calulate_bills(3, 15)


# Print the total bill.
print(my_bill)

'''
Explanation
What is this program doing?

This program calculates the total cost of buying chai.

The formula used is:

Total Bill = Number of Cups × Price per Cup
Step 1: Define the function
def calulate_bills(cups, price_per_cup):

This creates a function named calulate_bills.

It has two parameters:

cups
price_per_cup

These parameters receive values when the function is called.

At this point, the function is only defined, not executed.

Step 2: Return the calculation
return cups * price_per_cup

The return statement:

Calculates the total.
Sends the result back to the place where the function was called.

For example:

cups = 3
price_per_cup = 15

Calculation:

3 × 15 = 45

So the function returns:

45
What does return do?

return sends a value back to the caller.

Example:

def add(a, b):
    return a + b

result = add(5, 2)

Python does this:

5 + 2 = 7

Then:

result = 7

The same idea is used in your program.

Step 3: Call the function
my_bill = calulate_bills(3, 15)

Here, you're calling the function.

The arguments are:

Parameter	Argument
cups	3
price_per_cup	15

Inside the function, Python treats it as:

cups = 3
price_per_cup = 15

Then executes:

return cups * price_per_cup

Calculation:

3 × 15 = 45

The function returns:

45

So Python stores:

my_bill = 45
Step 4: Print the result
print(my_bill)

Python prints the value stored in my_bill.

Output:

45
Execution Flow
Program starts
      │
      ▼
Function is defined
      │
      ▼
calulate_bills(3, 15)
      │
      ▼
cups = 3
price_per_cup = 15
      │
      ▼
Calculate:
3 × 15
      │
      ▼
45
      │
      ▼
return 45
      │
      ▼
my_bill = 45
      │
      ▼
print(my_bill)
      │
      ▼
45
Final Output
45
What if the inputs change?
Example 1
my_bill = calulate_bills(5, 20)

Calculation:

5 × 20 = 100

Output:

100
Example 2
my_bill = calulate_bills(2, 12)

Calculation:

2 × 12 = 24

Output:

24
Improving the function name

A better version is:

def calculate_bills(cups, price_per_cup):
    return cups * price_per_cup

my_bill = calculate_bills(3, 15)
print(my_bill)

This uses the correct spelling of calculate, making the code easier to read and maintain.

Key Concepts
def defines a function.
Parameters (cups, price_per_cup) receive values passed to the function.
Arguments (3, 15) are the actual values supplied when calling the function.
return sends a value back to the caller.
The returned value is stored in my_bill.
print(my_bill) displays the calculated total bill.

'''

