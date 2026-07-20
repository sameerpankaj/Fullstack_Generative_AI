#immutable data types

# Create an empty set named 'spice_mix'
spice_mix = set()

# Print the memory ID of the set before adding elements
print(f'Initial spice mix id: {id(spice_mix)}')
print(f'Initial spice mix id: {spice_mix}')

# Add 'Ginger' to the set
spice_mix.add('Ginger')

# Add 'cardamom' to the set
spice_mix.add('cardamom')

# Print the memory ID of the set after adding elements
print(f'After spice mix id: {id(spice_mix)}')
print(f'After spice mix id: {spice_mix}')

#Note: the id never changes,