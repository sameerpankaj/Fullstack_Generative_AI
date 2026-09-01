#list comprehension

# menu = [
#     'Masala Chai',
#     'Iced Lemon Tea',
#     'Green Tea',
#     'Iced Peach Tea',
#     'Ginger Tea'

# ]

# iced_tea = [tea for tea in menu if 'Iced' in tea]
# print(iced_tea)



# iced_tea = [tea for tea in menu if len(tea) > 10]
# print(iced_tea)

# iced_tea = [tea for tea in menu if len(tea) < 10]
# print(iced_tea)

# Create a list of tea items
menu = [
    'Masala Chai',
    'Iced Lemon Tea',
    'Green Tea',
    'Iced Peach Tea',
    'Ginger Tea'
]

# Create a new list containing only teas that have the word 'Iced' in their name
iced_tea = [tea for tea in menu if 'Iced' in tea]

# Print the teas containing 'Iced'
print(iced_tea)


# Create a new list containing teas whose names have more than 10 characters
# len(tea) counts the number of characters in the tea name
iced_tea = [tea for tea in menu if len(tea) > 10]

# Print the teas with more than 10 characters
print(iced_tea)


'''
1. Creating the menu
menu = [
    'Masala Chai',
    'Iced Lemon Tea',
    'Green Tea',
    'Iced Peach Tea',
    'Ginger Tea'
]

Here, menu is a list containing 5 strings:

Index	Item
0	'Masala Chai'
1	'Iced Lemon Tea'
2	'Green Tea'
3	'Iced Peach Tea'
4	'Ginger Tea'
2. Find teas containing "Iced"
iced_tea = [tea for tea in menu if 'Iced' in tea]

print(iced_tea)

This is called a list comprehension.

The general structure is:

[new_value for item in list if condition]

Your code:

[tea for tea in menu if 'Iced' in tea]

can be read as:

"Take each tea from menu, but only include it if 'Iced' is inside the tea name."

Let's go through the items:

'Masala Chai'     → 'Iced' in it? ❌
'Iced Lemon Tea'  → 'Iced' in it? ✅
'Green Tea'       → 'Iced' in it? ❌
'Iced Peach Tea'  → 'Iced' in it? ✅
'Ginger Tea'      → 'Iced' in it? ❌

Therefore:

['Iced Lemon Tea', 'Iced Peach Tea']

So the output is:

['Iced Lemon Tea', 'Iced Peach Tea']
3. Find teas with more than 10 characters
iced_tea = [tea for tea in menu if len(tea) > 10]

print(iced_tea)

Here:

len(tea)

means:

"Count how many characters are in tea."

For example:

len('Masala Chai')

There are 11 characters:

M a s a l a _ C h a i
1 2 3 4 5 6 7 8 9 10 11

So:

len('Masala Chai') > 10

is:

11 > 10

which is True.

Let's check all of them:

Tea	len()	> 10
Masala Chai	11	✅
Iced Lemon Tea	14	✅
Green Tea	9	❌
Iced Peach Tea	14	✅
Ginger Tea	10	❌

Therefore:

['Masala Chai', 'Iced Lemon Tea', 'Iced Peach Tea']
4. Find teas with fewer than 10 characters
iced_tea = [tea for tea in menu if len(tea) < 10]

print(iced_tea)

Now we're saying:

"Take each tea from menu, but only include it if its length is less than 10."

Again:

Tea	len()	< 10
Masala Chai	11	❌
Iced Lemon Tea	14	❌
Green Tea	9	✅
Iced Peach Tea	14	❌
Ginger Tea	10	❌

So the result is:

['Green Tea']
⭐ The important part to understand

This:

iced_tea = [tea for tea in menu if len(tea) > 10]

is basically a shorter way of writing:

iced_tea = []

for tea in menu:
    if len(tea) > 10:
        iced_tea.append(tea)

And this:

iced_tea = [tea for tea in menu if 'Iced' in tea]

is equivalent to:

iced_tea = []

for tea in menu:
    if 'Iced' in tea:
        iced_tea.append(tea)
Remember this pattern:
[WHAT_TO_STORE for ITEM in LIST if CONDITION]

For your example:

[tea for tea in menu if len(tea) > 10]

means:

WHAT: tea
FROM: menu
CONDITION: len(tea) > 10

Once you recognize that pattern, list comprehensions become much easier.

'''