# Create a list of tuples.
# Each tuple contains an employee's name and age.
staff = [('Amit', 16), ('Zara', 17), ('Raj', 15)]

# Loop through each employee in the staff list.
# Each tuple is unpacked into the variables 'name' and 'age'.
for name, age in staff:

    # Check if the employee is 18 years old or older.
    if age >= 18:

        # If the condition is True, print that the employee is eligible.
        print(f'{name} is eligible to manage the staff')

        # Exit the loop immediately after finding the first eligible employee.
        break

# This else block belongs to the for loop, not the if statement.
# It runs only if the loop finishes without encountering a break.
else:

    # Print this message if no employee is 18 or older.
    print(f'No one is eligible for managing the staff')


'''

Explanation
Step 1: Creating the list
staff = [('Amit', 16), ('Zara', 17), ('Raj', 15)]

This creates a list containing three tuples.

Employee	Age
Amit	16
Zara	17
Raj	15
Step 2: Starting the loop
for name, age in staff:

The loop goes through each tuple one at a time.

First iteration
name = 'Amit'
age = 16
Step 3: Checking the condition
if age >= 18:

Python checks:

16 >= 18

Result:

False

Since the condition is False, the print() statement and break are skipped.

Second iteration
name = 'Zara'
age = 17

Python checks:

17 >= 18

Result:

False

Again, nothing is printed.

Third iteration
name = 'Raj'
age = 15

Python checks:

15 >= 18

Result:

False

Again, nothing is printed.

Step 4: What happens to break?

The break statement is never executed because no employee satisfies the condition age >= 18.

So the loop completes normally after checking all three employees.

Step 5: The else block
else:
    print('No one is eligible for managing the staff')

This else belongs to the for loop, not the if.

A for...else statement works like this:

If the loop is stopped using break, the else block is skipped.
If the loop finishes normally (without break), the else block runs.

Since no break occurred, Python executes:

print('No one is eligible for managing the staff')
Execution Flow
staff list
     │
     ▼
Amit (16)
     │
16 >= 18 ?
     │
    No
     │
     ▼
Zara (17)
     │
17 >= 18 ?
     │
    No
     │
     ▼
Raj (15)
     │
15 >= 18 ?
     │
    No
     │
     ▼
Loop finishes normally
     │
     ▼
Execute else
     │
     ▼
Print:
"No one is eligible for managing the staff"
Final Output
No one is eligible for managing the staff
What if someone was 18 or older?

Suppose the list was:

staff = [('Amit', 16), ('Zara', 20), ('Raj', 15)]

Execution:

Amit → 16 >= 18 → False
Zara → 20 >= 18 → True
Print:
Zara is eligible to manage the staff
Execute break
Exit the loop immediately.
Skip the else block.
Output
Zara is eligible to manage the staff
Key Concepts
for loops iterate through each item in a sequence.
if age >= 18 checks whether an employee is at least 18 years old.
break immediately exits the loop when a matching employee is found.
The else attached to a for loop runs only if the loop completes without executing a break. This makes for...else especially useful for searching through a list.

'''