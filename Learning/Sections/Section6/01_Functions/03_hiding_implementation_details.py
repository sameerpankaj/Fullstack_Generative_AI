'''
```
You are building a simple app that registers users.
You want to separate concerns: getting input, validating it, and saving it.
Task:
--Write reigister_user( ) that calls:
  .get_input( )
  .validate_input( )
  .save_to_db( )
```


'''

# def get_input():
#     print('Getting user input')

# def validate_input():
#     print('Validating the user information')

# def save_to_db():
#     print('saving to database')

# def register_user():
#     get_input()
#     validate_input()
#     save_to_db()
#     print('User registration complete')

# register_user()


# Define a function to get information from the user.
def get_input():

    # Display a message indicating that the program is collecting user input.
    print('Getting user input')


# Define a function to validate the user's information.
def validate_input():

    # Display a message indicating that the entered information is being validated.
    print('Validating the user information')


# Define a function to save the user's information to a database.
def save_to_db():

    # Display a message indicating that the data is being saved.
    print('Saving to database')


# Define the main function that handles the complete user registration process.
def register_user():

    # Step 1: Get the user's information.
    get_input()

    # Step 2: Validate the entered information.
    validate_input()

    # Step 3: Save the validated information to the database.
    save_to_db()

    # Step 4: Display a success message.
    print('User registration complete')


# Start the registration process by calling the main function.
register_user()


'''
Explanation
What does this program do?

This program simulates a user registration system.

Instead of putting all the code into one function, the task is divided into smaller functions, where each function performs one specific job.

The registration process follows these steps:

Get user information.
Validate the information.
Save the information.
Confirm that registration is complete.
Step 1: Define get_input()
def get_input():
    print('Getting user input')

This function represents collecting information from the user.

In a real application, this might ask the user to enter:

Name
Email
Password
Phone number

For this example, it simply prints:

Getting user input
Step 2: Define validate_input()
def validate_input():
    print('Validating the user information')

This function represents checking whether the user's information is valid.

Examples of validation include:

Is the email address valid?
Is the password long enough?
Are required fields filled in?
Is the username already taken?

For this example, it simply prints:

Validating the user information
Step 3: Define save_to_db()
def save_to_db():
    print('Saving to database')

This function represents storing the user's information in a database.

In a real application, it might save data such as:

Field	Example
Name	Aman
Email	aman@example.com
Password	(encrypted password)

For this example, it simply prints:

Saving to database
Step 4: Define register_user()
def register_user():

This is the main function.

It controls the entire registration process.

Inside it:

get_input()

collects the user's information.

Next:

validate_input()

checks whether the information is valid.

Next:

save_to_db()

stores the information.

Finally:

print('User registration complete')

prints the success message.

Step 5: Call the function
register_user()

This starts the registration process.

If this line were removed, none of the functions would execute because defining a function does not run it.

Execution Flow

When Python executes:

register_user()

the following happens:

register_user()
        │
        ▼
get_input()
        │
        ▼
validate_input()
        │
        ▼
save_to_db()
        │
        ▼
Print:
"User registration complete"
Step-by-Step Execution
Step 1

Python reaches:

register_user()

Execution enters the register_user() function.

Step 2

The first statement is:

get_input()

Output:

Getting user input
Step 3

Next:

validate_input()

Output:

Validating the user information
Step 4

Next:

save_to_db()

Output:

Saving to database
Step 5

Finally:

print('User registration complete')

Output:

User registration complete
Final Output
Getting user input
Validating the user information
Saving to database
User registration complete
Real-World Analogy

Imagine registering at a hotel:

Customer arrives
      │
      ▼
Reception asks for your details
      │
      ▼
Reception checks your ID
      │
      ▼
Reception enters your details into the computer
      │
      ▼
Room is booked successfully

This is exactly how your program is organized:

register_user()
      │
      ├── get_input()
      │
      ├── validate_input()
      │
      ├── save_to_db()
      │
      └── Registration Complete
Key Concepts
def defines a function.
A function does not run until it is called.
register_user() is the main function that coordinates the registration process.
Functions can call other functions.
Dividing a large task into smaller functions makes code:
More readable – easier to understand.
Reusable – each function can be used elsewhere.
Easier to maintain – changes can be made in one function without affecting the others.
Easier to debug – problems can be isolated to a specific function.

'''