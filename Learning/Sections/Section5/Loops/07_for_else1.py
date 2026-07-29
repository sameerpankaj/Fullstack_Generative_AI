# Create a list of tuples.
# Each tuple contains an employee's name and age.
staff = [('Amit', 16), ('Zara', 17), ('Raj', 15)]

# Loop through each tuple in the staff list.
# The tuple is unpacked into two variables: name and age.
for name, age in staff:

    # Check if the employee's age is less than or equal to 18.
    if age <= 18:

        # If the condition is True, print that the employee is eligible.
        print(f'{name} is eligible to manage the staff')

        # Exit the loop immediately after finding the first eligible employee.
        break

# The else block belongs to the for loop, NOT the if statement.
# It executes only if the loop finishes without encountering a break.
else:
    print(f'No one is eligible for managing the staff')


'''

Explanation
Step 1: Creating the list
staff = [('Amit', 16), ('Zara', 17), ('Raj', 15)]

This creates a list containing three tuples.

Name	Age
Amit	16
Zara	17
Raj	15
Step 2: Looping through the list
for name, age in staff:

Each tuple is unpacked into two variables:

name stores the employee's name.
age stores the employee's age.

The loop runs like this:

First iteration

name = 'Amit'
age = 16
Step 3: Checking the condition
if age <= 18:

For Amit:

16 <= 18

This is True.

So Python executes:

print(f'{name} is eligible to manage the staff')

Output:

Amit is eligible to manage the staff
Step 4: The break statement
break

break immediately stops the loop.

This means Python does not check:

Zara
Raj

The loop ends as soon as Amit is found eligible.

Step 5: The else block
else:
    print('No one is eligible for managing the staff')

This else belongs to the for loop, not the if statement.

A for...else works like this:

If the loop finishes without a break, the else block runs.
If the loop is stopped by a break, the else block is skipped.

Since break was executed when Amit was found eligible, the else block is not executed.

Execution Flow
staff list
     │
     ▼
Amit (16)
     │
     ▼
16 <= 18 ?
     │
    Yes
     │
     ▼
Print:
"Amit is eligible to manage the staff"
     │
     ▼
break
     │
     ▼
Loop ends
     │
     ▼
Skip else
Final Output
Amit is eligible to manage the staff
What if no one met the condition?

Suppose the list was:

staff = [('Amit', 25), ('Zara', 30), ('Raj', 22)]

The loop would check:

25 ≤ 18 → False
30 ≤ 18 → False
22 ≤ 18 → False

No break would occur.

After the loop finishes normally, the else block executes.

Output:

No one is eligible for managing the staff
Key Concept

The for...else statement is commonly used when searching through a collection:

Item found → execute break → else is skipped.
Item not found → loop completes normally → else executes.

'''