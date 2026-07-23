

# Ask the user to enter their preferred cup size.
# The .lower() method converts the input to lowercase,
# allowing inputs like "Small", "SMALL", or "small" to be treated the same.
cup_size = input('Enter preferred cup size (small/medium/large): ').lower()

# Check the selected cup size and display the corresponding price.
if cup_size == 'small':
    # Price for a small cup.
    print('You need to pay ₹10')

elif cup_size == 'medium':
    # Price for a medium cup.
    print('You need to pay ₹15')

elif cup_size == 'large':
    # Price for a large cup.
    print('You need to pay ₹20')

else:
    # Executed if the entered cup size is not available.
    print('Size not available')