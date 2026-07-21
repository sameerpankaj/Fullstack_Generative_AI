#sets

# Create a set containing the essential spices.
# A set stores unique, unordered elements (duplicates are not allowed).
essentials_spices = {'cardamom', 'ginger', 'cinnamon'}

# Create another set containing optional spices.
optional_spices = {'cloves', 'ginger', 'black pepper'}

#Union of sets
# Use the union operator (|) to combine both sets.
# The result contains all unique spices from both sets.
# Since 'ginger' appears in both sets, it is included only once.
all_spices = essentials_spices | optional_spices

# Print the combined set of spices.
print(f'All spices: {all_spices}')


# Find the intersection of the two sets.
# The intersection operator (&) returns only the elements
# that are present in both sets.
common_spices = essentials_spices & optional_spices

# Print the common spices found in both sets.
print(f'Common spices: {common_spices}')

'''
Expected Output
Common spices: {'ginger'}

Note: In your original code, you calculated common_spices but printed optional_spices. To display the intersection, you should print common_spices instead.
'''

# Find the difference between the two sets.
# The difference operator (-) returns the elements
# that are present in the first set but NOT in the second set.
only_in_essential = essentials_spices - optional_spices

# Print the spices that exist only in the essential_spices set.
print(f'Only in essential spices: {only_in_essential}')
'''
Expected Output
Only in essential spices: {'cardamom', 'cinnamon'}

Note: Since 'ginger' is present in both sets, it is excluded from the result. The order of items may vary because sets are unordered.

'''

#membership test
print(f"Is 'cloves' in optional spices? {'cloves' in optional_spices}")

#frozen set
'''
Here's a well-commented example of a frozenset in Python.

# A frozenset is an immutable version of a set.
# Once created, its elements cannot be added, removed, or changed.

essential_spices = frozenset({'cardamom', 'ginger', 'cinnamon'})

# Print the frozenset.
print(f'Essential spices: {essential_spices}')
Output
Essential spices: frozenset({'cardamom', 'ginger', 'cinnamon'})
Key Points about frozenset
Immutable: You cannot modify it after creation.
Unordered: Like a regular set, the order of elements is not guaranteed.
Unique elements only: Duplicate values are automatically removed.
Hashable: Unlike a normal set, a frozenset can be used as a dictionary key or as an element of another set.
Example: Trying to modify a frozenset
essential_spices = frozenset({'cardamom', 'ginger', 'cinnamon'})

# This will raise an AttributeError because frozensets are immutable.
essential_spices.add('cloves')

Error:

AttributeError: 'frozenset' object has no attribute 'add'

A regular set is used when you need to add or remove elements, while a frozenset is used when you want a collection of unique elements that should never change.

'''
