#snack suggestion project

# Ask the user to enter the name of a snack.
# The .lower() method converts the input to lowercase,
# so the program accepts inputs like "Cookies", "COOKIES", or "cookies".
snacks = input('Enter name of the Snacks:\n').lower()

# Check if the entered snack is either "cookies" or "samosa".
# If it matches, confirm the order and display the snack name.
if snacks == 'cookies' or snacks == 'samosa':
    print(f'Great choice! We will serve you {snacks}')
else:
    # If the snack is not available, inform the user.
    print('Unavailable')

#  or

    '''
    
    
    # Ask the user to enter the name of a snack.
# Convert the input to lowercase for case-insensitive comparison.
snacks = input('Enter name of the Snacks:\n').lower()

# Check if the snack is one of the available options.
if snacks in ('cookies', 'samosa'):
    print(f'Great choice! We will serve you {snacks}')
else:
    print('Unavailable')

The second version is generally preferred because it's shorter, easier to read, and scales better when checking multiple values.
    '''
    