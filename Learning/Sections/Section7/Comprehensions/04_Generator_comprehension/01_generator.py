#Generator comprehensions

# daily_sales = [5, 10, 12, 7, 3, 8, 9 , 15]

# total_cups = sum(sale for sale in daily_sales if sale > 5)

# print(total_cups)

# Generator Expression
# Create a list containing the number of cups sold each day
daily_sales = [5, 10, 12, 7, 3, 8, 9, 15]

# Add only the sales values that are greater than 5
# sale for sale in daily_sales → go through each value in daily_sales
# if sale > 5 → keep only values greater than 5
# The generator expression produces the values one at a time
# sum() adds all those values together
total_cups = sum(sale for sale in daily_sales if sale > 5)

# Print the total number of cups sold on days where sales were greater than 5
print(total_cups)

'''
Output
61

Because the values greater than 5 are:

10 + 12 + 7 + 8 + 9 + 15 = 61
🧠 Understanding this part
sale for sale in daily_sales if sale > 5

It follows this pattern:

expression for item in collection if condition

So:

sale → what we want to produce
for sale in daily_sales → go through every sale
if sale > 5 → keep only sales greater than 5
Why is it a generator?

Compare:

[sale for sale in daily_sales if sale > 5]

This creates a list:

[10, 12, 7, 8, 9, 15]

But:

(sale for sale in daily_sales if sale > 5)

creates a generator.

A generator produces the values one at a time when needed, rather than creating the whole list immediately.

That's why this is useful:

sum(sale for sale in daily_sales if sale > 5)

sum() takes each value from the generator and adds it.

⭐ Easy way to remember
[ ... ]  → List comprehension → creates a list
{ ... }  → Set comprehension → creates a set
{key: value ...} → Dictionary comprehension → creates a dictionary
( ... ) → Generator expression → produces values one at a time

For your example:

sum(sale for sale in daily_sales if sale > 5)

means:

Go through the daily sales, take only values greater than 5, and give them to sum() one at a time.

'''