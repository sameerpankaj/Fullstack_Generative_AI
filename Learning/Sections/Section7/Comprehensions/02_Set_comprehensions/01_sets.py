# #set comprehension

# #1
# favourite_chais = [
#     'Masala Chai', 'Green Tea', 'Masala Chai', 'Lemon Tea', 'Green Tea', 'Elaichi Chai'
# ]

# unique_chai = {chai for chai in favourite_chais }

# print(unique_chai)

# unique_chai = {chai for chai in favourite_chais if len(chai) < 8 }
# print(unique_chai)



# #2
# recipes = {
#     'Masala Chai': ['ginger', 'cardmom', 'clove'],
#     'Elaichi Chai': ['cardmom', 'milk'],
#     'Spicy Chai': ['ginger', 'black pepper', 'clove']
# }

# unique_spices = {spice for ingredients in recipes.values() for spice in ingredients}

# print(unique_spices)


# 1. Create a list containing some duplicate chai names
favourite_chais = [
    'Masala Chai',
    'Green Tea',
    'Masala Chai',
    'Lemon Tea',
    'Green Tea',
    'Elaichi Chai'
]

# Create a set containing all chai names from the list
# A set automatically removes duplicate values
unique_chai = {chai for chai in favourite_chais}

# Print the unique chai names
print(unique_chai)


# Create a set containing only chai names with fewer than 8 characters
# len(chai) counts the number of characters in each chai name
unique_chai = {chai for chai in favourite_chais if len(chai) < 8}

# Print the chai names that have fewer than 8 characters
print(unique_chai)


# 2. Create a dictionary where each chai has a list of ingredients
recipes = {
    'Masala Chai': ['ginger', 'cardmom', 'clove'],
    'Elaichi Chai': ['cardmom', 'milk'],
    'Spicy Chai': ['ginger', 'black pepper', 'clove']
}

# Create a set containing every ingredient from all the recipes
# recipes.values() gives us each ingredient list
# The inner loop goes through each ingredient in that list
# Because the result is a set, duplicate ingredients are automatically removed
unique_spices = {
    spice
    for ingredients in recipes.values()
    for spice in ingredients
}

# Print all unique ingredients
print(unique_spices)

'''
What is Set Comprehension?

Set comprehension is very similar to list comprehension, but you use { } instead of [ ].

List comprehension:

[chai for chai in favourite_chais]

Set comprehension:

{chai for chai in favourite_chais}

The biggest difference is:

A list can contain duplicates, but a set automatically removes duplicates.

So:

['Masala Chai', 'Green Tea', 'Masala Chai', 'Green Tea']

becomes:

{'Masala Chai', 'Green Tea'}
Your second example

This:

unique_spices = {
    spice
    for ingredients in recipes.values()
    for spice in ingredients
}

can be understood as:

For each ingredient list in recipes
    For each spice in that ingredient list
        put the spice into the set

The result will contain:

{'ginger', 'cardmom', 'clove', 'milk', 'black pepper'}

Even though ginger and clove appear in multiple recipes, they appear only once in the set.

🧠 Remember
[ ]  → List comprehension
{ }  → Set comprehension
{key: value} → Dictionary comprehension

And for set comprehension:

{value for item in collection if condition}

For example:

{chai for chai in favourite_chais if len(chai) < 8}

means:

Take each chai, keep it only if its length is less than 8, and put the results into a set.


'''