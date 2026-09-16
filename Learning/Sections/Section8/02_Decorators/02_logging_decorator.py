# from functools import wraps

# def log_activity(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         print(f'🚀 Calling: {func.__name__}')
#         result = func(*args, **kwargs)
#         print(f'✅Finished:{func.__name__}')
#         return result
#     return wrapper

# @log_activity
# def brew_chai(type, milk='no'):
#     print(f'Brewing {type} chai and milk status {milk}')

# brew_chai('Masala')

from functools import wraps  # Imports wraps to preserve the original function's information


def log_activity(func):  # Creates a decorator that receives a function

    @wraps(func)  # Keeps the original function name and other metadata

    def wrapper(*args, **kwargs):  # Wrapper can accept any positional and keyword arguments

        print(f'🚀 Calling: {func.__name__}')  # Prints the name of the function being called

        result = func(*args, **kwargs)  # Calls the original function and stores its result

        print(f'✅ Finished: {func.__name__}')  # Prints when the function has finished

        return result  # Returns the original function's result

    return wrapper  # Returns the wrapper function


@log_activity  # Applies the decorator to brew_chai
def brew_chai(type, milk='no'):  # Defines brew_chai with type and optional milk
    print(f'Brewing {type} chai and milk status {milk}')  # Prints the chai order


brew_chai('Masala')  # Calls brew_chai with type='Masala'


'''
What happens with @log_activity?

This line:

@log_activity
def brew_chai(type, milk='no'):

is essentially the same as:

def brew_chai(type, milk='no'):
    print(f'Brewing {type} chai and milk status {milk}')

brew_chai = log_activity(brew_chai)

So the original brew_chai function is passed into log_activity().

Inside:

def log_activity(func):

func now refers to the original brew_chai.

3. What is wrapper?
def wrapper(*args, **kwargs):

wrapper is the new function that replaces brew_chai.

When you eventually write:

brew_chai('Masala')

you're actually calling:

wrapper('Masala')

because the decorator replaced brew_chai with wrapper.

4. What are *args and **kwargs?

Here:

def wrapper(*args, **kwargs):

*args collects positional arguments.

So:

brew_chai('Masala')

means:

args = ('Masala',)

**kwargs collects keyword arguments.

For example:

brew_chai('Masala', milk='yes')

would give:

args = ('Masala',)
kwargs = {'milk': 'yes'}

This allows the decorator to work with functions having different arguments.

5. The important line
result = func(*args, **kwargs)

This calls the original function.

For your example:

func(*args, **kwargs)

becomes approximately:

brew_chai('Masala')

Then the original function executes:

print(f'Brewing {type} chai and milk status {milk}')

Since you didn't provide milk, Python uses the default:

milk = 'no'

So it prints:

Brewing Masala chai and milk status no
6. Why result?

This:

result = func(*args, **kwargs)

stores whatever the original function returns.

For example, if the function had:

return "Chai ready"

then:

result

would contain:

Chai ready

And:

return result

passes that value back to whoever called the function.

Your current brew_chai() doesn't explicitly return anything, so result is:

None
7. Final output

When you run:

brew_chai('Masala')

you get:

🚀 Calling: brew_chai
Brewing Masala chai and milk status no
✅ Finished: brew_chai
🧠 The decorator flow

Think of it like this:

brew_chai('Masala')
       ↓
   wrapper()
       ↓
🚀 Calling brew_chai
       ↓
original brew_chai()
       ↓
Brewing Masala chai...
       ↓
✅ Finished brew_chai

So the main purpose of this decorator is:

"Whenever a function runs, automatically print a message before and after it."

This pattern is very common for logging, timing, authentication, debugging, and monitoring in real Python applications.


'''