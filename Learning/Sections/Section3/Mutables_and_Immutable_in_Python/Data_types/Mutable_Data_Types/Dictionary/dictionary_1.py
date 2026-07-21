#dictionaries

# chai_order = dict(type='Masala chai', size='Large', sugar=2)#in dicctionaries order does not matter
# print(f'Chai order: {chai_order}')

# chai_recipe = {}
# chai_recipe['base'] = 'black tea'
# chai_recipe['liquid'] = 'milk'

# print(f'Recipe base: {chai_recipe['base']}')# here it will only print the value stroed in base
# print(f'recepe {chai_recipe}')#here it will print both the base and liquid

# #delete
# del chai_recipe['liquid']# this will delete the element liquid and value stored in it
# print(f'Recipe: {chai_recipe}')# output will be just: Recipe: {'base': 'black tea'}

# #membership testing
# print(f"Is sugar in the order? {'sugar' in chai_order}")

# chai_order = dict(type='Ginger chai', size='Medium', sugar=1)

# #fetch keys
# print(F'Order details (keys): {chai_order.keys()}')

# #fetch values
# print(F'Order details (values): {chai_order.values()}')

# #fetch items
# print(F'Order details (items): {chai_order.items()}')

# #remove items
# last_item = chai_order.popitem()
# print(f'Removed last item: {last_item}')

# #update
# extra_spices = {'cardamom': 'crushed', 'ginger':'sliced'}
# chai_recipe.update(extra_spices)
# print(f'Updated Chai recipe: {chai_recipe}')

# chai_size = chai_order['size']
# print(f'chai size is : {chai_size}')

# #what if the item is not present, it might crash the code, so we will use different method
# customer_note = chai_order.get('note', 'No Note')
# print(f'Customer note is {customer_note}')

# customer_note = chai_order.get('size', 'No Note')
# print(f'Customer note is {customer_note}')


# Create a dictionary using the dict() constructor.
# Dictionaries store data as key-value pairs.
# The order of items is preserved in modern Python (3.7+).
chai_order = dict(type='Masala chai', size='Large', sugar=2)

# Print the entire dictionary.
print(f'Chai order: {chai_order}')

# Create an empty dictionary.
chai_recipe = {}

# Add key-value pairs to the dictionary.
chai_recipe['base'] = 'black tea'
chai_recipe['liquid'] = 'milk'

# Access and print the value associated with the 'base' key.
print(f"Recipe base: {chai_recipe['base']}")

# Print the entire dictionary.
print(f'Recipe: {chai_recipe}')

# -----------------------------------
# Delete an item from the dictionary.
# -----------------------------------
# Remove the 'liquid' key and its associated value.
del chai_recipe['liquid']

# Print the updated dictionary.
print(f'Recipe: {chai_recipe}')

# -----------------------------------
# Membership Testing
# -----------------------------------
# Check whether the key 'sugar' exists in the dictionary.
print(f"Is sugar in the order? {'sugar' in chai_order}")

# Create another dictionary.
chai_order = dict(type='Ginger chai', size='Medium', sugar=1)

# -----------------------------------
# Fetch Keys
# -----------------------------------
# Return all keys in the dictionary.
print(f'Order details (keys): {chai_order.keys()}')

# -----------------------------------
# Fetch Values
# -----------------------------------
# Return all values in the dictionary.
print(f'Order details (values): {chai_order.values()}')

# -----------------------------------
# Fetch Items
# -----------------------------------
# Return all key-value pairs as tuples.
print(f'Order details (items): {chai_order.items()}')

# -----------------------------------
# Remove the Last Item
# -----------------------------------
# popitem() removes and returns the last inserted key-value pair.
last_item = chai_order.popitem()
print(f'Removed last item: {last_item}')

# -----------------------------------
# Update a Dictionary
# -----------------------------------
# Create another dictionary containing extra spices.
extra_spices = {'cardamom': 'crushed', 'ginger': 'sliced'}

# Add or update key-value pairs in chai_recipe.
chai_recipe.update(extra_spices)

# Print the updated recipe.
print(f'Updated chai recipe: {chai_recipe}')

# -----------------------------------
# Access a Value by Key
# -----------------------------------
# Retrieve the value associated with the 'size' key.
chai_size = chai_order['size']
print(f'Chai size is: {chai_size}')

# -----------------------------------
# Safely Retrieve a Value
# -----------------------------------
# get() returns the value if the key exists.
# Otherwise, it returns the default value ('No Note')
# instead of raising a KeyError.
customer_note = chai_order.get('note', 'No Note')
print(f'Customer note is: {customer_note}')

# Since 'size' exists, get() returns its value.
customer_note = chai_order.get('size', 'No Note')
print(f'Customer note is: {customer_note}')

'''
Note

Your original comment says:

# in dictionaries order does not matter

This was true for older versions of Python. From Python 3.7 onward, dictionaries preserve insertion order, although they are still accessed by keys, not by position.

'''
