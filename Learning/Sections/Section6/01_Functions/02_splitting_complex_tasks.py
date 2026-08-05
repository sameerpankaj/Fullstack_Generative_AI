#Splitting complex tasks
# def fetch_sales():
#     print('Fetching the sales data')

# def filter_valid_sales():
#     print('Filtering valid sales data')

# def summarize_data():
#     print('Summarizing the sales data')

# def generate_report():
#     fetch_sales()
#     filter_valid_sales()
#     summarize_data()
#     print('Report is ready')


# generate_report()


# Define a function to fetch sales data.
def fetch_sales():

    # Print a message indicating that sales data is being fetched.
    print('Fetching the sales data')


# Define a function to filter valid sales records.
def filter_valid_sales():

    # Print a message indicating that invalid sales data is removed.
    print('Filtering valid sales data')


# Define a function to summarize the sales data.
def summarize_data():

    # Print a message indicating that sales data is being summarized.
    print('Summarizing the sales data')


# Define the main function that generates the report.
def generate_report():

    # Call the function to fetch sales data.
    fetch_sales()

    # Call the function to filter the sales data.
    filter_valid_sales()

    # Call the function to create a summary of the data.
    summarize_data()

    # Print a message after all report preparation steps are completed.
    print('Report is ready')


# Call the main function to start the report generation process.
generate_report()


'''

Explanation
1. Creating small functions

This program is divided into four functions:

fetch_sales()
filter_valid_sales()
summarize_data()
generate_report()

Each function performs one specific task.

This is called modular programming — breaking a large task into smaller, reusable pieces.

Function 1: Fetch sales data
def fetch_sales():
    print('Fetching the sales data')

This function only prints:

Fetching the sales data

It does not run immediately when Python reads the code.

A function only runs when it is called.

Example:

fetch_sales()
Function 2: Filter sales data
def filter_valid_sales():
    print('Filtering valid sales data')

This function represents checking the sales records and keeping only valid entries.

When called:

filter_valid_sales()

Output:

Filtering valid sales data
Function 3: Summarize data
def summarize_data():
    print('Summarizing the sales data')

This function represents creating a summary, such as:

total sales
average sales
number of transactions

Currently, it only prints a message.

Function 4: Generate report
def generate_report():

This is the main function that controls the whole workflow.

Inside it:

fetch_sales()

calls the first function.

Then:

filter_valid_sales()

calls the second function.

Then:

summarize_data()

calls the third function.

Finally:

print('Report is ready')

prints the completion message.

Function Calling Flow

When Python reaches:

generate_report()

the execution starts.

The flow is:

generate_report()
        |
        ▼
fetch_sales()
        |
        ▼
filter_valid_sales()
        |
        ▼
summarize_data()
        |
        ▼
Print "Report is ready"
Step-by-Step Execution
Step 1

Python runs:

generate_report()

It enters the function.

Step 2

Inside generate_report():

fetch_sales()

runs.

Output:

Fetching the sales data
Step 3

Next:

filter_valid_sales()

runs.

Output:

Filtering valid sales data
Step 4

Next:

summarize_data()

runs.

Output:

Summarizing the sales data
Step 5

Finally:

print('Report is ready')

runs.

Output:

Report is ready
Final Output
Fetching the sales data
Filtering valid sales data
Summarizing the sales data
Report is ready
Why structure code this way?

Instead of writing everything together:

print('Fetching the sales data')
print('Filtering valid sales data')
print('Summarizing the sales data')
print('Report is ready')

we create separate functions.

Advantages:

1. Reusability

You can call:

fetch_sales()

whenever you need sales data.

2. Easier debugging

If something goes wrong with filtering, you only check:

filter_valid_sales()

instead of searching through a large program.

3. Better organization

generate_report() describes the overall process:

fetch → filter → summarize → report

This makes the code easier for other programmers to understand.

Key Concepts
def creates a function.
A function runs only when it is called.
Functions can call other functions.
generate_report() acts as the main controller.
Breaking programs into small functions improves readability and maintenance.

'''