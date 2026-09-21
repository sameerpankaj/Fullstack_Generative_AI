# class BaseChai:
#     def __init__(self, type_):
#         self.type = type_


#     def prepare(self):
#         print(f'Preparing {self.type} chai...')


# class MasalaChai(BaseChai):
#     def add_spices(self):
#         print('Adding cardamom, ginger, cloves.')


# class ChaiShop:
#     chai_cls = BaseChai

#     def __init__(self):
#         self.chai =self.chai_cls('Regular')


#     def serve(self):
#         print(f'Serving {self.chai.type} chai in the shop')
#         self.chai.prepare()


# class FancyChaiShop(ChaiShop):
#     chai_cls = MasalaChai

# shop = ChaiShop()
# fancy = FancyChaiShop()
# shop.serve()
# fancy.serve()
# fancy.chai.add_spices()

class BaseChai:

    def __init__(self, type_):
        # __init__ runs automatically when a BaseChai object is created.
        # type_ is the chai type passed to the object.

        self.type = type_
        # Store the chai type inside this particular object.


    def prepare(self):
        # Method for preparing the chai.

        print(f'Preparing {self.type} chai...')
        # self.type gets the type belonging to the current object.


class MasalaChai(BaseChai):
    # MasalaChai INHERITS from BaseChai.
    #
    # Therefore MasalaChai automatically gets:
    # 1. __init__()
    # 2. prepare()
    #
    # We only need to add things that are special to MasalaChai.

    def add_spices(self):
        # A method that exists only for MasalaChai.

        print('Adding cardamom, ginger, cloves.')


class ChaiShop:

    chai_cls = BaseChai
    # This is a CLASS ATTRIBUTE.
    #
    # It tells ChaiShop which chai class it should create.
    # By default:
    # chai_cls = BaseChai


    def __init__(self):
        # Runs when a ChaiShop object is created.

        self.chai = self.chai_cls('Regular')
        # self.chai_cls means:
        # "Look at the chai_cls belonging to this particular shop."
        #
        # For a normal ChaiShop:
        # self.chai_cls = BaseChai
        #
        # Therefore this becomes:
        # self.chai = BaseChai('Regular')


    def serve(self):
        # Serve the chai in the shop.

        print(f'Serving {self.chai.type} chai in the shop')
        # self.chai.type gives the type of chai.

        self.chai.prepare()
        # Call the prepare() method of the chai object.


class FancyChaiShop(ChaiShop):
    # FancyChaiShop inherits everything from ChaiShop.

    chai_cls = MasalaChai
    # BUT it changes chai_cls.
    #
    # Normal ChaiShop:
    # chai_cls = BaseChai
    #
    # FancyChaiShop:
    # chai_cls = MasalaChai


shop = ChaiShop()
# Creates a normal ChaiShop.
#
# Because chai_cls = BaseChai:
# self.chai = BaseChai('Regular')


fancy = FancyChaiShop()
# Creates a FancyChaiShop.
#
# FancyChaiShop has:
# chai_cls = MasalaChai
#
# Therefore:
# self.chai = MasalaChai('Regular')


shop.serve()
# Calls the serve() method inherited from ChaiShop.


fancy.serve()
# Calls the SAME serve() method inherited from ChaiShop.
# But this time self.chai is a MasalaChai object.


fancy.chai.add_spices()
# fancy.chai is a MasalaChai object.
# Therefore it has access to add_spices().

'''

What is happening step by step?

The most important part is this:

class ChaiShop:
    chai_cls = BaseChai

Think of chai_cls as:

"Which type of chai should this shop create?"

For a normal shop:

ChaiShop
   |
   └── chai_cls → BaseChai

But then you create:

class FancyChaiShop(ChaiShop):
    chai_cls = MasalaChai

Now:

FancyChaiShop
   |
   └── chai_cls → MasalaChai

So the fancy shop automatically creates a different type of chai.

3. What happens when we create shop?

You write:

shop = ChaiShop()

Python runs:

def __init__(self):

Inside it:

self.chai = self.chai_cls('Regular')

For shop:

self.chai_cls
       ↓
   BaseChai

Therefore Python effectively does:

self.chai = BaseChai('Regular')

So:

shop
 └── chai
      ├── type = "Regular"
      └── class = BaseChai
4. What happens when we create fancy?

You write:

fancy = FancyChaiShop()

FancyChaiShop doesn't have its own __init__().

So Python uses the inherited one from ChaiShop:

def __init__(self):
    self.chai = self.chai_cls('Regular')

But here's the important part:

For fancy:

self.chai_cls

finds:

MasalaChai

because FancyChaiShop changed the class attribute:

chai_cls = MasalaChai

Therefore:

self.chai = MasalaChai('Regular')

So:

fancy
 └── chai
      ├── type = "Regular"
      └── class = MasalaChai
5. Why does fancy.serve() work?

This is a very important concept.

You write:

fancy.serve()

FancyChaiShop doesn't have a serve() method.

But it inherits it from ChaiShop.

So Python finds:

ChaiShop.serve()

Inside:

print(f'Serving {self.chai.type} chai in the shop')

self.chai.prepare()

Now:

self
 ↓
fancy

and:

self.chai
 ↓
MasalaChai object

Because MasalaChai inherits from BaseChai, it has:

prepare()

So:

self.chai.prepare()

runs the BaseChai.prepare() method.

6. Output

When you run:

shop.serve()

you get:

Serving Regular chai in the shop
Preparing Regular chai...

Then:

fancy.serve()

gives:

Serving Regular chai in the shop
Preparing Regular chai...

It looks the same because both have the type:

'Regular'

But internally they are different:

shop.chai  → BaseChai object
fancy.chai → MasalaChai object
7. Why does fancy.chai.add_spices() work?

This line:

fancy.chai.add_spices()

works because:

fancy.chai
     ↓
MasalaChai object

And MasalaChai contains:

def add_spices(self):
    print('Adding cardamom, ginger, cloves.')

Therefore:

Adding cardamom, ginger, cloves.

But if you tried:

shop.chai.add_spices()

you would get an error because:

shop.chai → BaseChai

and BaseChai doesn't have add_spices().

8. The inheritance structure

Think of your classes like this:

             BaseChai
                │
                │ inherits
                ↓
            MasalaChai


             ChaiShop
                │
                │ inherits
                ↓
         FancyChaiShop

But there are actually two separate inheritance relationships:

Chai inheritance
BaseChai
   ↑
MasalaChai

MasalaChai gets:

__init__()
prepare()

and adds:

add_spices()
Shop inheritance
ChaiShop
   ↑
FancyChaiShop

FancyChaiShop gets:

__init__()
serve()

but changes:

chai_cls

from:

BaseChai

to:

MasalaChai
⭐ The most important concept here

This line:

self.chai = self.chai_cls('Regular')

is extremely powerful.

It doesn't hard-code:

self.chai = BaseChai('Regular')

Instead, it says:

"Use whatever class chai_cls currently points to."

Therefore:

ChaiShop
   ↓
chai_cls = BaseChai
   ↓
BaseChai('Regular')

while:

FancyChaiShop
   ↓
chai_cls = MasalaChai
   ↓
MasalaChai('Regular')

Same __init__() code, different object created.

This is a simple example of polymorphism: the same shop code can work with different chai classes.

One-line memory trick

Inheritance = "I get your methods."
Class attribute = "I can choose which class to use."
self = "this particular object."
__init__() = "set up this object when it is created."
'''