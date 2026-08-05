# chai_types = ['Light', 'Kadak', 'Ginger', 'Kadak']

# strong_chai = list(filter(lambda chai: chai=='Kadak', chai_types))

# print(strong_chai)

# Create a list containing different types of chai.
chai_types = ['Light', 'Kadak', 'Ginger', 'Kadak']


# Use the filter() function to keep only the chai types
# that are equal to 'Kadak'.
#
# lambda chai: chai == 'Kadak'
# - 'chai' represents each element of the list.
# - If the element is 'Kadak', the lambda returns True.
# - If not, it returns False.
#
# filter() returns only the elements for which the lambda returns True.
# list() converts the filter object into a list.
strong_chai = list(filter(lambda chai: chai == 'Kadak', chai_types))


# Print the filtered list.
print(strong_chai)

# but if we want to filter the type which is not kadak, then we can use
# strong_chai = list(filter(lambda chai: chai != 'Kadak', chai_types))


'''
Explanation

This program demonstrates how to use filter() with a lambda function to extract specific items from a list.

Step 1: Create the List
chai_types = ['Light', 'Kadak', 'Ginger', 'Kadak']

A list named chai_types is created.

It contains four elements:

Index    Value
-----    -----
0        Light
1        Kadak
2        Ginger
3        Kadak
Step 2: Understanding filter()
filter(lambda chai: chai == 'Kadak', chai_types)

The syntax of filter() is:

filter(function, iterable)
function → Decides whether to keep an item.
iterable → The list to process.

Here:

lambda chai: chai == 'Kadak'

is the function.

Step 3: Understanding the Lambda Function
lambda chai: chai == 'Kadak'

This is a short anonymous function.

It is equivalent to:

def is_kadak(chai):
    return chai == 'Kadak'

The lambda checks:

"Is the current chai equal to 'Kadak'?"

If yes:

True

If no:

False
Step 4: How filter() Processes Each Item

Python checks every item in the list one by one.

First item
chai = 'Light'

Check:

'Light' == 'Kadak'

Result:

False

Not included.

Second item
chai = 'Kadak'

Check:

'Kadak' == 'Kadak'

Result:

True

Included.

Third item
chai = 'Ginger'

Check:

'Ginger' == 'Kadak'

Result:

False

Not included.

Fourth item
chai = 'Kadak'

Check:

'Kadak' == 'Kadak'

Result:

True

Included.

Step 5: Result of filter()

After checking all elements, filter() keeps only the matching ones.

Result:

['Kadak', 'Kadak']

However, filter() returns a filter object, not a list.

So:

list(...)

converts it into a normal Python list.

Step 6: Print the Result
print(strong_chai)

Output:

['Kadak', 'Kadak']
Execution Flow
chai_types
│
├── Light
│      │
│      ▼
│   Is it 'Kadak'?
│      │
│      └── No ❌
│
├── Kadak
│      │
│      ▼
│   Is it 'Kadak'?
│      │
│      └── Yes ✅
│
├── Ginger
│      │
│      ▼
│   Is it 'Kadak'?
│      │
│      └── No ❌
│
├── Kadak
│      │
│      ▼
│   Is it 'Kadak'?
│      │
│      └── Yes ✅
│
▼
Final List:
['Kadak', 'Kadak']
Final Output
['Kadak', 'Kadak']
Without Using Lambda

The same program can be written using a normal function:

def is_kadak(chai):
    return chai == 'Kadak'

strong_chai = list(filter(is_kadak, chai_types))

print(strong_chai)

Output:

['Kadak', 'Kadak']
Key Concepts
Concept	Meaning
filter()	Selects items that satisfy a condition
lambda	A short anonymous function
chai	Represents each element in the list
==	Compares two values
list()	Converts the filter object into a list
In simple words

Your program says:

"Go through each chai type. If it is 'Kadak', keep it. Otherwise, ignore it. Finally, store all matching chai types in a new list and print them."


'''

