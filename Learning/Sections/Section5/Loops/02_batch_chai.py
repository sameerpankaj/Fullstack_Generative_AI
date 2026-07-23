'''
A chai shop makes tea in batches every 15 minutes.

You want to simulate 4 batches.

Task:

Use range() to simulate batch numbers.

Print: 'Preparing chai for batch #[number]'



'''

# Loop through batch numbers from 1 to 4.
# The range() function is not inclusive of the stop value,
# so range(1, 5) generates: 1, 2, 3, 4.
for batch in range(1, 5):

    # Print a message indicating that chai is being prepared
    # for the current batch number.
    print(f'Preparing chai for batch #{batch}')

'''
Explanation
range(1, 5)
Starts at 1 (inclusive).
Stops before 5 (exclusive).
Generates the sequence: 1, 2, 3, 4.
for batch in range(1, 5):
Executes the loop 4 times.
During each iteration, batch takes the values 1, 2, 3, and 4.
print(f'Preparing chai for batch #{batch}')
Uses an f-string to insert the current batch number into the message.
Output
Preparing chai for batch #1
Preparing chai for batch #2
Preparing chai for batch #3
Preparing chai for batch #4

Tip: A common mistake is thinking range(1, 5) includes 5. It does not. The stop value in range(start, stop) is always excluded.

'''