'''
You are creating a tea menu board.
Each item must be numbered.
Task:
    Use enumerate() to print menu items with numbers.


'''

#Use enumerate()
# Create a list containing different types of chai
menu = ['Green', 'Lemon', 'Spiced', 'Mint']

# Classical method:
# This loops through each item in the list but does not provide
# the position (index) of each item.
#
# for m in menu:
#     print(f'Menu item is {m}')

# Since we want to display the item number along with the chai name,
# we use enumerate().

# enumerate(menu, start=1):
# - menu: The list to iterate over.
# - start=1: Starts numbering from 1 instead of the default 0.

for index, item in enumerate(menu, start=1):

    # Print the item number and the chai name
    # Example:
    # 1 : Green Chai
    # 2 : Lemon Chai
    print(f'{index} : {item} Chai')

    '''
    
    Explanation
menu = ['Green', 'Lemon', 'Spiced', 'Mint']
Creates a list of four chai flavors.
enumerate(menu, start=1)
Iterates through the list.
Returns both:
index → the item number (1, 2, 3, 4)
item → the chai flavor (Green, Lemon, etc.)
start=1
Starts counting from 1.
Without it, the numbering would start from 0.
Output
1 : Green Chai
2 : Lemon Chai
3 : Spiced Chai
4 : Mint Chai
Without start=1

If you wrote:

for index, item in enumerate(menu):
    print(f'{index} : {item} Chai')

The output would be:

0 : Green Chai
1 : Lemon Chai
2 : Spiced Chai
3 : Mint Chai
    '''



'''
The enumerate() function in Python is used when you need both the index (position) and the value while looping through a sequence like a list, tuple, or string.

Syntax
enumerate(iterable, start=0)
iterable: The sequence you want to loop through.
start (optional): The starting value of the index. By default, it is 0.
Example 1: Without enumerate()
orders = ['Hitesh', 'Aman', 'Becky', 'Carlos']

index = 0

for name in orders:
    print(index, name)
    index += 1

Output:

0 Hitesh
1 Aman
2 Becky
3 Carlos

Here, you have to manually keep track of the index.

Example 2: Using enumerate()
orders = ['Hitesh', 'Aman', 'Becky', 'Carlos']

for index, name in enumerate(orders):
    print(index, name)

Output:

0 Hitesh
1 Aman
2 Becky
3 Carlos

This is cleaner because Python automatically provides the index.

Example 3: Starting the Index from 1
orders = ['Hitesh', 'Aman', 'Becky', 'Carlos']

for token, name in enumerate(orders, start=1):
    print(f'Token #{token}: {name}')

Output:

Token #1: Hitesh
Token #2: Aman
Token #3: Becky
Token #4: Carlos
Example 4: Looping Through a String
word = "Python"

for index, letter in enumerate(word):
    print(index, letter)

Output:

0 P
1 y
2 t
3 h
4 o
5 n
Example 5: Finding an Item
fruits = ['Apple', 'Banana', 'Orange', 'Mango']

for index, fruit in enumerate(fruits):
    if fruit == 'Orange':
        print(f'Orange found at index {index}')

Output:

Orange found at index 2
How enumerate() Works

Suppose you have:

colors = ['Red', 'Green', 'Blue']

Using:

for index, color in enumerate(colors):
    print(index, color)

is similar to:

Index	Value
0	Red
1	Green
2	Blue
Why Use enumerate()?

✅ No need to manually create and increment an index variable.

❌ Instead of:

index = 0

for name in orders:
    print(index, name)
    index += 1

✅ Write:

for index, name in enumerate(orders):
    print(index, name)
Summary
enumerate() returns both the index and the value of each item in a sequence.
The default index starts at 0, but you can change it using the start parameter.
It makes your code shorter, cleaner, and less error-prone when you need both the position and the item.

'''