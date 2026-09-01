#Dictionary Comprehension

# tea_prices_inr = {
#     'Masala Chai': 40,
#     'Green Tea': 50,
#     'Lemon Tea': 200
# }

# tea_prices_usd = {tea:price / 80 for tea, price in tea_prices_inr.items()}

# print(tea_prices_usd)

# Create a dictionary containing tea prices in Indian Rupees (INR)
tea_prices_inr = {
    'Masala Chai': 40,
    'Green Tea': 50,
    'Lemon Tea': 200
}

# Create a new dictionary with prices converted from INR to USD
# tea and price come from each key-value pair in tea_prices_inr
# .items() gives us both the tea name (key) and its price (value)
# price / 80 converts the price from INR to USD
tea_prices_usd = {
    tea: price / 80
    for tea, price in tea_prices_inr.items()
}

# Print the new dictionary containing prices in USD
print(tea_prices_usd)


'''

Output
{'Masala Chai': 0.5, 'Green Tea': 0.625, 'Lemon Tea': 2.5}
🧠 Understanding this line
tea_prices_usd = {
    tea: price / 80
    for tea, price in tea_prices_inr.items()
}

This is dictionary comprehension.

The general structure is:

{key: value for item in collection}

Here:

tea: price / 80

means:

Keep the tea name as the key, but calculate a new value by dividing the price by 80.

And:

for tea, price in tea_prices_inr.items()

means:

Go through every key-value pair in tea_prices_inr.

What does .items() do?

Your original dictionary:

{
    'Masala Chai': 40,
    'Green Tea': 50,
    'Lemon Tea': 200
}

.items() gives you pairs:

'Masala Chai', 40
'Green Tea', 50
'Lemon Tea', 200

So Python does:

tea = 'Masala Chai'    price = 40
40 / 80 = 0.5

tea = 'Green Tea'      price = 50
50 / 80 = 0.625

tea = 'Lemon Tea'     price = 200
200 / 80 = 2.5

And creates:

{
    'Masala Chai': 0.5,
    'Green Tea': 0.625,
    'Lemon Tea': 2.5
}
⭐ The key difference

With a list comprehension:

[expression for item in list]

With a set comprehension:

{expression for item in set}

With a dictionary comprehension:

{key: value for item in dictionary}

Your example is:

{tea: price / 80 for tea, price in tea_prices_inr.items()}

So you're keeping the key (tea) and creating a new value (price / 80).

'''