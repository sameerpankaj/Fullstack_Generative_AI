# Create a list of users.
# Each user is stored as a dictionary containing:
# id, total purchase amount, and coupon code.
users = [
    {'id': 1, 'total': 100, 'coupon': 'P20'},
    {'id': 2, 'total': 150, 'coupon': 'F20'},
    {'id': 3, 'total': 80, 'coupon': 'P50'},
]


# Create a dictionary that stores coupon rules.
# Each coupon code is the key.
# The value is a tuple:
# (percentage discount, fixed discount amount)
discounts = {
    'P20': (0.2, 0),   # 20% discount
    'F10': (0.5, 0),   # 50% discount
    'P50': (0, 10),    # $10 fixed discount
}


# Loop through each user dictionary in the users list.
for user in users:

    # Get the discount details for the user's coupon.
    # The tuple is unpacked into two variables:
    # percent stores percentage discount
    # fixed stores fixed discount amount
    #
    # If the coupon does not exist, use (0, 0) as the default value.
    percent, fixed = discounts.get(user['coupon'], (0, 0))


    # Calculate the discount amount.
    # Percentage discount is calculated using:
    # total amount × percentage
    #
    # Fixed discount is added directly.
    discount = user['total'] * percent + fixed


    # Print the user's id, purchase amount, and discount received.
    print(f"{user['id']} paid {user['total']} and got discount for next visit of ${discount}")


'''

Explanation Step-by-Step
1. Creating the users list
users = [
    {'id': 1, 'total': 100, 'coupon': 'P20'},
    {'id': 2, 'total': 150, 'coupon': 'F20'},
    {'id': 3, 'total': 80, 'coupon': 'P50'},
]

Here we have a list containing three dictionaries.

Each dictionary represents one user.

Example:

{'id': 1, 'total': 100, 'coupon': 'P20'}

means:

Key	Value
id	1
total	100
coupon	P20
2. Creating the discount dictionary
discounts = {
    'P20': (0.2, 0),
    'F10': (0.5, 0),
    'P50': (0, 10),
}

This dictionary stores coupon rules.

The structure is:

coupon code : (percentage discount, fixed discount)

Example:

'P20': (0.2, 0)

means:

Coupon: P20
Percentage discount: 0.2 = 20%
Fixed discount: $0
3. The for loop
for user in users:

The loop goes through each user one by one.

First loop:
user = {'id': 1, 'total': 100, 'coupon': 'P20'}
4. Getting the coupon discount
percent, fixed = discounts.get(user['coupon'], (0, 0))

Let's break this down.

Get the user's coupon:
user['coupon']

For the first user:

'P20'
Search in the discounts dictionary:
discounts.get('P20', (0, 0))

Python finds:

(0.2, 0)

Then tuple unpacking happens:

percent = 0.2
fixed = 0
What does .get() do?

The .get() method safely retrieves a dictionary value.

Example:

discounts.get('P20', (0,0))

Output:

(0.2, 0)

But:

discounts.get('F20', (0,0))

Output:

(0,0)

because F20 does not exist in the dictionary.

5. Calculating the discount
discount = user['total'] * percent + fixed

For the first user:

total = 100
percent = 0.2
fixed = 0

Calculation:

discount = 100 × 0.2 + 0
discount = 20

So:

discount = 20
6. Printing the result
print(f"{user['id']} paid {user['total']} and got discount for next visit of ${discount}")

The f-string replaces variables with their values.

Output:

1 paid 100 and got discount for next visit of $20.0
Complete Execution
User 1

Coupon:

P20

Discount:

100 × 20% = $20

Output:

1 paid 100 and got discount for next visit of $20.0
User 2

Coupon:

F20

But F20 is not available:

discounts.get('F20', (0,0))

returns:

(0,0)

So:

discount = 150 × 0 + 0

Output:

2 paid 150 and got discount for next visit of $0

If you wanted a fixed $20 discount, add:

'F20': (0, 20)
User 3

Coupon:

P50

Discount rule:

(0,10)

Meaning:

0% percentage discount
$10 fixed discount

Calculation:

discount = 80 × 0 + 10

Output:

3 paid 80 and got discount for next visit of $10
Final Output
1 paid 100 and got discount for next visit of $20.0
2 paid 150 and got discount for next visit of $0
3 paid 80 and got discount for next visit of $10
Key Python Concepts Used
1. List of dictionaries

Used to store multiple users:

users = [{'id':1}, {'id':2}]
2. Dictionary lookup
discounts.get(key, default_value)

Safely gets a value.

3. Tuple unpacking
percent, fixed = (0.2, 0)

is the same as:

percent = 0.2
fixed = 0
4. f-string formatting
f"{variable}"

allows variables to be inserted directly into text.

'''
