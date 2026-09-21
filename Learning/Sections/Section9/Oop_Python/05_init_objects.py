# #initialization

# class ChaiOrder:
#     def __init__(self, type_, size):
#         self.type = type_
#         self.size = size

#     def summary(self):
#         return f'{self.size} ml of {self.type} chai'


# order = ChaiOrder('Masala', 200)
# print(order.summary())


# order_two = ChaiOrder('Ginger', 220)
# print(order_two.summary())

class ChaiOrder:

    def __init__(self, type_, size):
        # __init__ runs automatically when we create a new ChaiOrder object.
        #
        # self  -> the object being created
        # type_ -> the chai type given by us
        # size  -> the chai size given by us

        self.type = type_
        # Store the value of type_ inside this particular object.
        # For example: self.type = 'Masala'

        self.size = size
        # Store the value of size inside this particular object.
        # For example: self.size = 200


    def summary(self):
        # This method gives us a summary of the chai order.

        return f'{self.size} ml of {self.type} chai'
        # self.size  -> size belonging to this object
        # self.type  -> type belonging to this object


order = ChaiOrder('Masala', 200)
# Creates a ChaiOrder object.
#
# Python automatically calls:
# __init__(order, 'Masala', 200)
#
# So:
# order.type = 'Masala'
# order.size = 200


print(order.summary())
# Calls summary() for the order object.
#
# self = order
#
# Therefore:
# self.size -> 200
# self.type -> 'Masala'
#
# Output:
# 200 ml of Masala chai


order_two = ChaiOrder('Ginger', 220)
# Creates another ChaiOrder object.
#
# Python automatically calls:
# __init__(order_two, 'Ginger', 220)
#
# So:
# order_two.type = 'Ginger'
# order_two.size = 220


print(order_two.summary())
# self = order_two
#
# self.size -> 220
# self.type -> 'Ginger'
#
# Output:
# 220 ml of Ginger chai


'''

Output
200 ml of Masala chai
220 ml of Ginger chai
2. What exactly happens here?

When you write:

order = ChaiOrder('Masala', 200)

Python creates an object and automatically calls:

__init__(order, 'Masala', 200)

So inside:

def __init__(self, type_, size):

the values are:

self  → order
type_ → 'Masala'
size  → 200

Then:

self.type = type_

becomes:

order.type = 'Masala'

And:

self.size = size

becomes:

order.size = 200

So your object now looks conceptually like:

order
 ├── type = 'Masala'
 └── size = 200
3. What happens with order_two?

When you write:

order_two = ChaiOrder('Ginger', 220)

Python creates a different object.

Now:

order_two
 ├── type = 'Ginger'
 └── size = 220

So you have two independent objects:

order
 ├── type = 'Masala'
 └── size = 200


order_two
 ├── type = 'Ginger'
 └── size = 220

This is why:

print(order.summary())

gives:

200 ml of Masala chai

while:

print(order_two.summary())

gives:

220 ml of Ginger chai
4. Understanding self with a simple trick

Remember this rule:

self means "this particular object."

For:

order.summary()

Python essentially does:

ChaiOrder.summary(order)

Therefore:

self = order

For:

order_two.summary()

Python essentially does:

ChaiOrder.summary(order_two)

Therefore:

self = order_two

That's why the same summary() method can work with different objects.

5. Why do we use type_ instead of type?

You wrote:

def __init__(self, type_, size):

instead of:

def __init__(self, type, size):

This is a common Python convention.

type already has a special built-in meaning in Python:

type(123)

returns:

<class 'int'>

So using:

type_

helps avoid confusing the parameter with Python's built-in type().

Then you can still store it as:

self.type = type_
The big picture

This code:

class ChaiOrder:

    def __init__(self, type_, size):
        self.type = type_
        self.size = size

    def summary(self):
        return f'{self.size} ml of {self.type} chai'

creates a blueprint for chai orders.

Then:

order = ChaiOrder('Masala', 200)

creates one object.

And:

order_two = ChaiOrder('Ginger', 220)

creates another object.

Think of it like this:

             ChaiOrder CLASS
             (Blueprint)
                  │
          ┌───────┴───────┐
          ↓               ↓
       order          order_two
          │               │
     Masala, 200      Ginger, 220
          │               │
          ↓               ↓
       summary()       summary()
          │               │
          ↓               ↓
  200 ml of          220 ml of
  Masala chai        Ginger chai
⭐ Three things to remember
__init__() → sets up the object when it is created.
self → refers to the current object.
self.variable → stores data specifically inside that object.

This is the foundation you'll need before moving into instance attributes vs class attributes, which connects directly to your previous Chaicup example.

'''