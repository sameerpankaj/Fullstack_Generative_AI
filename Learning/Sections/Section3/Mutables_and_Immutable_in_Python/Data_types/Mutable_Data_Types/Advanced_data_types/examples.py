# import arrow


# brewing_time = arrow.utcnow()
# brewing_time.to('Europe/Rome')

# from collections import namedtuple
# chai_profile = namedtuple('chaiProfile', ['flavor', 'aroma'])

import arrow
from collections import namedtuple

# Get the current UTC time.
brewing_time = arrow.utcnow()

# Convert the time to the Europe/Rome timezone.
brewing_time = brewing_time.to('Europe/Rome')

# Print the converted time.
print(brewing_time)

# Create a namedtuple class.
ChaiProfile = namedtuple('ChaiProfile', ['flavor', 'aroma'])

# Create an instance of the namedtuple.
chai = ChaiProfile(flavor='Masala', aroma='Spicy')

# Print the values.
print(chai)
print(chai.flavor)
print(chai.aroma)