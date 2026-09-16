# from functools import wraps

# def my_decorator(func):
#     def wrapper():
#         print('Before function runs')
#         func()
#         print('After function runs')
#     return wrapper

# @my_decorator
# def greet():
#     print('Hello from decorators class from chaicode')


# greet()
# print(greet.__name__)


from functools import wraps
# Import 'wraps' from Python's functools module.
# In THIS particular program, wraps is imported but not actually used.
# We will see later why 'wraps' is normally used with decorators.


def my_decorator(func):
    # Define a decorator function called my_decorator().
    # 'func' will receive the function that we want to decorate.


    def wrapper():
        # Define an inner function called wrapper().
        # This function will replace the original function after decoration.

        print('Before function runs')
        # Print this message BEFORE the original function runs.

        func()
        # Call the original function that was passed to my_decorator().
        # In our example, 'func' will be the greet() function.

        print('After function runs')
        # Print this message AFTER the original function finishes.


    return wrapper
    # Return the wrapper function.
    # The decorator gives this new function back to Python.


@my_decorator
# This is decorator syntax.
# It tells Python to pass the function below (greet)
# into my_decorator().
#
# It is essentially the same as:
# greet = my_decorator(greet)


def greet():
    # Define the original greet() function.

    print('Hello from decorators class from chaicode')
    # This is what the original greet() function does.


greet()
# Call greet().
# BUT because of the decorator, 'greet' now refers to wrapper().
# Therefore wrapper() runs instead of directly running the original greet().


print(greet.__name__)
# Print the name of the function currently stored in 'greet'.
# Since greet was replaced by wrapper, this prints:
# wrapper


'''
First understand what a decorator does

A decorator allows you to add behavior to a function without changing the function's original code.

Your original function is:

def greet():
    print('Hello from decorators class from chaicode')

You want something to happen:

BEFORE greet()
      ↓
greet()
      ↓
AFTER greet()

The decorator does exactly that.

3. What is my_decorator(func)?

You have:

def my_decorator(func):

Here func is a parameter.

It will receive another function.

In your case:

greet

So eventually Python does something conceptually like:

my_decorator(greet)

Therefore:

func

inside the decorator refers to:

greet
4. What is wrapper()?

Inside your decorator:

def wrapper():

This is another function.

It contains:

print('Before function runs')

func()

print('After function runs')

So wrapper() basically says:

"Before you run the original function, do this. Then run the original function. Then do this afterward."

5. The MOST important part: @my_decorator

You wrote:

@my_decorator
def greet():
    ...

This looks special, but Python converts it approximately to:

def greet():
    print('Hello from decorators class from chaicode')

greet = my_decorator(greet)

⭐ This is the key concept.

The original greet function is passed into:

my_decorator(greet)

Inside:

def my_decorator(func):

we now have:

func → original greet()

Then:

return wrapper

returns the wrapper function.

So now:

greet
 ↓
wrapper

The name greet now refers to wrapper.

6. What happens when you call greet()?

You write:

greet()

But remember:

greet → wrapper

So you're actually calling:

wrapper()

The wrapper starts:

print('Before function runs')

Output:

Before function runs

Then:

func()

Remember:

func → original greet()

So the original function runs:

print('Hello from decorators class from chaicode')

Output:

Hello from decorators class from chaicode

Then:

print('After function runs')

Output:

After function runs
7. Complete output from greet()

Therefore:

Before function runs
Hello from decorators class from chaicode
After function runs
8. Now the interesting part: greet.__name__

You have:

print(greet.__name__)

You might expect:

greet

But your program actually prints:

wrapper
Why?

Because after decoration:

greet
 ↓
wrapper

The name greet is now pointing to the wrapper function.

So:

greet.__name__

is effectively asking:

"What is the name of the function that greet currently refers to?"

Answer:

wrapper
9. But why did we import wraps?

At the beginning you have:

from functools import wraps

But you didn't use it.

Normally, we use it like this:

from functools import wraps

def my_decorator(func):

    @wraps(func)
    def wrapper():
        print('Before function runs')
        func()
        print('After function runs')

    return wrapper

Now:

@my_decorator
def greet():
    print('Hello')

When you run:

print(greet.__name__)

you get:

greet

instead of:

wrapper
10. Why do we need @wraps(func)?

Without wraps:

original greet()
       ↓
   decorator
       ↓
   wrapper()
       ↓
greet now points to wrapper

Therefore:

greet.__name__

gives:

wrapper

With:

@wraps(func)

Python preserves important information from the original function.

So:

greet.__name__

gives:

greet
⭐ The most important concept

Remember this:

@my_decorator
def greet():

is essentially:

greet = my_decorator(greet)

And your decorator does:

original greet()
       ↓
my_decorator(greet)
       ↓
wrapper()
       ↓
greet now refers to wrapper

Then:

greet()

actually executes:

wrapper()
   ↓
Before function runs
   ↓
original greet()
   ↓
Hello from decorators class from chaicode
   ↓
After function runs

And because you didn't use @wraps(func):

print(greet.__name__)

prints:

wrapper
🧠 One sentence to remember:

A decorator takes a function, wraps additional behavior around it, and returns the modified/replacement function.


'''