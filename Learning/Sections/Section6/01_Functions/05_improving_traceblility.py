'''
```
Your shop adds a 10% VAT on every order.
You want this to be consistent and traceable.
Task:
  .Write add_vat(price, vat_rate)
  .Use it to compute final prices to 3 orders

```

'''

# def add_vat(price, vat_rate):
#     return price * (100 + vat_rate) / 100


# orders = [100, 150, 150]

# for price in orders:
#     final_amount = add_vat(price, 10)
#     print(f'Original: {price}, Final with VAT: {final_amount}')

# Define a function named 'add_vat'.
# The function accepts two parameters:
# 1. price - the original price of the item.
# 2. vat_rate - the VAT percentage to add.
def add_vat(price, vat_rate):

    # Calculate the final price after adding VAT.
    # Formula:
    # Final Price = Original Price × (100 + VAT Rate) ÷ 100
    return price * (100 + vat_rate) / 100


# Create a list containing the original prices of three orders.
orders = [100, 150, 150]


# Loop through each price in the orders list.
for price in orders:

    # Call the add_vat() function with:
    # - the current order price
    # - a VAT rate of 10%
    # Store the returned value in 'final_amount'.
    final_amount = add_vat(price, 10)

    # Print both the original price and the final price after adding VAT.
    print(f'Original: {price}, Final with VAT: {final_amount}')


    '''
    
    Explanation
What does this program do?

This program calculates the final price of each order after adding VAT (Value Added Tax).

The VAT rate used is 10%.

Step 1: Define the function
def add_vat(price, vat_rate):

This creates a function named add_vat.

It has two parameters:

Parameter	Meaning
price	Original price of the order
vat_rate	VAT percentage

The function doesn't execute yet—it is only defined.

Step 2: Calculate the VAT
return price * (100 + vat_rate) / 100

This formula calculates the final amount after adding VAT.

The formula is:

Final Price = Original Price × (100 + VAT Rate) ÷ 100
Example

Suppose:

price = 100
vat_rate = 10

Calculation:

100 × (100 + 10) ÷ 100

= 100 × 110 ÷ 100

= 110

The function returns:

110
Step 3: Create the list
orders = [100, 150, 150]

This creates a list containing three order prices.

Order	Price
1	100
2	150
3	150
Step 4: Start the loop
for price in orders:

The loop goes through each price one by one.

First Iteration

Python assigns:

price = 100

Then calls:

final_amount = add_vat(100, 10)

Inside the function:

price = 100
vat_rate = 10

Calculation:

100 × 110 ÷ 100

=110

The function returns:

110

So:

final_amount = 110

Then Python prints:

Original: 100, Final with VAT: 110.0
Second Iteration

Python assigns:

price = 150

Then:

add_vat(150,10)

Calculation:

150 × 110 ÷100

=165

Output:

Original: 150, Final with VAT: 165.0
Third Iteration

Again:

price = 150

The calculation is the same.

Output:

Original: 150, Final with VAT: 165.0
Execution Flow
Program starts
      │
      ▼
Define add_vat()
      │
      ▼
orders = [100,150,150]
      │
      ▼
Loop begins
      │
      ├──────────────┐
      ▼              │
price = 100          │
      │              │
add_vat(100,10)      │
      │              │
returns 110          │
      │              │
Print result         │
      │              │
      ▼              │
price = 150          │
      │              │
add_vat(150,10)      │
      │              │
returns 165          │
      │              │
Print result         │
      │              │
      ▼              │
price = 150          │
      │              │
add_vat(150,10)      │
      │              │
returns 165          │
      │              │
Print result         │
      └──────────────┘
Final Output
Original: 100, Final with VAT: 110.0
Original: 150, Final with VAT: 165.0
Original: 150, Final with VAT: 165.0
Understanding the Formula

The function uses:

price * (100 + vat_rate) / 100

For a 10% VAT:

100 + 10 = 110

So the formula becomes:

price × 110 ÷100

which is the same as:

price × 1.10

You could also write the function like this:

def add_vat(price, vat_rate):
    return price * (1 + vat_rate / 100)

Both versions produce the same result.

Key Concepts
Function (def) groups reusable code into one place.
Parameters (price, vat_rate) receive values when the function is called.
Arguments (100, 10) are the actual values passed to the function.
return sends the calculated final price back to the caller.
for loop processes each order in the orders list one at a time.
f-strings insert variable values directly into the printed message.
    
    '''