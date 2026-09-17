# from functools import wraps

# def require_admin(func):
#     @wraps(func)
#     def wrapper(user_role):
#         if user_role != 'admin':
#             print('Access denied: Admins only')
#             return None
#         else:
#             return func(user_role)
#     return wrapper

# @require_admin
# def access_tea_inventory(role):
#     print('Access granted to tea inventory')

# access_tea_inventory('user')
# access_tea_inventory('admin')


from functools import wraps

# This decorator checks whether the user is an admin
def require_admin(func):

    # This wrapper receives the user's role
    @wraps(func)
    def wrapper(user_role):

        # If the role is NOT admin, deny access
        if user_role != 'admin':
            print('Access denied: Admins only')
            return None

        # If the role IS admin, allow the original function to run
        else:
            return func(user_role)

    # Return the wrapper function
    return wrapper


# Apply the require_admin decorator
@require_admin
def access_tea_inventory(role):

    # This runs only when the user is an admin
    print('Access granted to tea inventory')


# Try to access as a normal user
access_tea_inventory('user')

# Try to access as an admin
access_tea_inventory('admin')


'''
Let's understand it step by step
1. from functools import wraps
from functools import wraps

wraps helps the wrapper preserve information about the original function.

For example, the original function is:

access_tea_inventory

Using @wraps(func) helps Python keep its name and other metadata.

2. The decorator
def require_admin(func):

require_admin is the decorator function.

func represents the original function:

access_tea_inventory

So conceptually:

func
 ↓
access_tea_inventory()
3. The wrapper
def wrapper(user_role):

The wrapper is the function that will actually be called when you write:

access_tea_inventory('user')

After decoration, Python effectively does:

access_tea_inventory = require_admin(access_tea_inventory)

So access_tea_inventory now refers to the wrapper.

4. Check the role
if user_role != 'admin':

This asks:

Is the user's role anything other than "admin"?

For:

access_tea_inventory('user')

we have:

user_role = 'user'

Therefore:

'user' != 'admin'

is True.

So Python executes:

print('Access denied: Admins only')
return None

The original function doesn't run.

5. What happens with admin?

When you write:

access_tea_inventory('admin')

we get:

user_role = 'admin'

Now:

user_role != 'admin'

is False.

So Python goes to:

return func(user_role)

func is the original:

access_tea_inventory(role)

So it effectively calls:

access_tea_inventory('admin')

and prints:

Access granted to tea inventory
🔥 The complete flow

When you write:

access_tea_inventory('user')

the flow is:

access_tea_inventory('user')
             ↓
         wrapper('user')
             ↓
      Is user == admin?
             ↓
            NO
             ↓
   Access denied

For:

access_tea_inventory('admin')

the flow is:

access_tea_inventory('admin')
             ↓
         wrapper('admin')
             ↓
      Is user == admin?
             ↓
           YES
             ↓
       func('admin')
             ↓
   Access granted
⭐ The main concept

A decorator can control whether a function is allowed to execute.

That's why decorators are commonly used for:

🔐 Authentication
👤 Authorization
📝 Logging
⏱️ Timing
🐞 Debugging
📊 Monitoring

Your example is specifically authorization: checking whether the user has permission to access something.

'''