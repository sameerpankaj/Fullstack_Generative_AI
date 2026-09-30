
class ChaiOrder:
    def __init__(self, tea_type, sweetness, size):
        self.tea_type = tea_type
        self.sweetness = sweetness
        self.size = size

    @classmethod
    def from_dict(cls, order_data):
        return cls(
            order_data['tea_type'],
            order_data['sweetness'],
            order_data['size'],
        )

    @classmethod
    def from_string(cls, order_string):
        tea_type, sweetness, size = order_string.split('-')
        return cls(tea_type, sweetness, size)


class ChaiUtils:
    @staticmethod
    def is_valid_size(size):
        return size in ['Small', 'Medium', 'Large']

print(ChaiUtils.is_valid_size('Medium'))


order1 = ChaiOrder.from_dict({'tea_type': 'masala', 'sweetness': 'medium', 'size': 'Large'})

order2 = ChaiOrder.from_string('Ginger-Low-Small')

order3 = ChaiOrder('Large', 'Low', 'Large')


print(order1.__dict__)
print(order2.__dict__)
print(order3.__dict__)


'''
1. The basic difference
	@classmethod	@staticmethod
First parameter	cls	None
Receives class automatically?	✅ Yes	❌ No
Receives object automatically?	❌ No	❌ No
Can access class attributes through cls?	✅ Yes	❌ Not automatically
Can create/return class objects easily?	✅ Yes	❌ Not automatically
Needs an instance?	❌ No	❌ No
Typical use	Alternative constructors, class-level operations	Utility/helper functions
Simple memory trick

Class method → I need the CLASS.
Static method → I don't need the CLASS or OBJECT.

2. @staticmethod

Let's use your chai example:

class ChaiUtilities:

    @staticmethod
    def clean_ingredients(text):
        return [item.strip() for item in text.split(',')]


raw = 'water , milk , ginger , honey'

cleaned = ChaiUtilities.clean_ingredients(raw)

print(cleaned)

Output:

['water', 'milk', 'ginger', 'honey']

Here:

ChaiUtilities.clean_ingredients(raw)

Python simply passes:

raw

to:

text

There is no self and no cls.

Why?

Because this function doesn't care about:

a particular chai object
the ChaiUtilities class
class attributes

It just receives some text and cleans it.

So a static method is basically:

"I'm putting this function inside the class because it logically belongs here, but I don't need the class or object."

3. @classmethod

Now consider:

class Chai:

    shop_name = "Sameer's Chai Shop"

    @classmethod
    def show_shop_name(cls):
        return cls.shop_name

We can call:

print(Chai.show_shop_name())

Output:

Sameer's Chai Shop

Python automatically passes the class:

Chai.show_shop_name()

is effectively like:

Chai.show_shop_name(Chai)

So:

cls

refers to:

Chai

Therefore:

cls.shop_name

means:

Chai.shop_name
4. Why would we need classmethod?

One very important use is an alternative constructor.

Suppose we have:

class Chai:

    def __init__(self, type_, size):
        self.type = type_
        self.size = size

Normally:

chai = Chai("Masala", 200)

But perhaps we want to create a Chai object from a string:

Masala,200

We could do:

class Chai:

    def __init__(self, type_, size):
        self.type = type_
        self.size = size

    @classmethod
    def from_string(cls, text):
        type_, size = text.split(',')
        return cls(type_, int(size))


chai = Chai.from_string("Masala,200")

print(chai.type)
print(chai.size)

Output:

Masala
200

Notice:

return cls(type_, int(size))

cls represents the class that called the method.

So:

Chai.from_string(...)

causes:

cls = Chai

Then:

cls(type_, int(size))

becomes effectively:

Chai(type_, int(size))

That's extremely useful.

5. The big advantage of classmethod

Consider inheritance:

class Chai:

    def __init__(self, type_, size):
        self.type = type_
        self.size = size

    @classmethod
    def from_string(cls, text):
        type_, size = text.split(',')
        return cls(type_, int(size))


class MasalaChai(Chai):
    pass

Now:

chai = MasalaChai.from_string("Masala,250")

What does cls become?

MasalaChai

Therefore:

return cls(type_, int(size))

creates:

MasalaChai("Masala", 250)

This is one reason classmethod is powerful.

If you had hard-coded:

return Chai(type_, int(size))

you would always create a Chai, even when a subclass called the method.

6. Static method example

Suppose we have:

class Chai:

    @staticmethod
    def is_valid_size(size):
        return size in [100, 150, 200, 250]

We can do:

print(Chai.is_valid_size(200))

Output:

True

There is no need for:

self

or:

cls

The function only needs the size argument.

7. Class method vs static method side-by-side
class Chai:

    shop_name = "Sameer's Chai Shop"

    @classmethod
    def show_shop(cls):
        return cls.shop_name

    @staticmethod
    def calculate_price(size):
        return size * 0.05
Class method
Chai.show_shop()

Python effectively does:

Chai.show_shop(Chai)

So:

cls = Chai

It can access:

cls.shop_name
Static method
Chai.calculate_price(200)

Python does not automatically add anything.

Conceptually:

calculate_price(200)

So:

size = 200

That's it.

8. Pros and cons
@classmethod
Pros ✅

1. Can access class data

cls.shop_name

2. Excellent for alternative constructors

Chai.from_string(...)

3. Works nicely with inheritance

Because cls refers to the class that actually called the method.

4. Can modify class-level state

For example:

class Chai:

    total_orders = 0

    @classmethod
    def add_order(cls):
        cls.total_orders += 1
Cons ❌

1. Slightly more complicated

You need to understand cls.

2. Tightly connected to the class

If your function doesn't need class information, using classmethod is unnecessary.

3. Not ideal for general-purpose utility functions

If a function doesn't need class state, staticmethod is usually clearer.

9. @staticmethod
Pros ✅

1. Simple

No self, no cls.

@staticmethod
def clean(text):
    ...

2. Good for utility/helper functions

Examples:

clean_ingredients()
calculate_price()
validate_size()
convert_temperature()

3. Doesn't require creating an object

You can directly do:

ChaiUtilities.clean_ingredients(text)

4. Makes dependencies clear

If the method only needs its arguments, that's obvious.

Cons ❌

1. Cannot automatically access class state

You don't get:

cls

automatically.

2. Not useful when you actually need the class

If you need:

cls.shop_name

then a static method isn't the right tool.

3. Sometimes a normal function would be better

If the function has no meaningful relationship to the class, putting it inside a class as a static method may add unnecessary structure.

10. What about self?

This is the third important piece.

Instance method
class Chai:

    def describe(self):
        return "This is chai"

Called:

chai = Chai()
chai.describe()

Python effectively does:

Chai.describe(chai)

So:

self → object
Class method
@classmethod
def something(cls):
    ...

Called:

Chai.something()

Python effectively does:

Chai.something(Chai)

So:

cls → class
Static method
@staticmethod
def something(value):
    ...

Called:

Chai.something(10)

Python effectively does:

something(10)

So:

nothing is automatically passed
11. Easy diagram

Think of it this way:

                    Python automatically gives you
                              │
          ┌───────────────────┼───────────────────┐
          │                   │                   │
          ▼                   ▼                   ▼

   Instance Method       Class Method       Static Method
       self                  cls                  nothing
         │                    │
         ▼                    ▼
      OBJECT                CLASS
         │                    │
         ▼                    ▼
   chai.type            Chai.shop_name
Remember:
self → specific object
cls  → class
static → neither
12. When should you use which?

A very practical rule:

Ask yourself:

"Does this method need information from a specific object?"

If yes:

def method(self):

➡️ Instance method

"Does this method need information from the class itself?"

If yes:

@classmethod
def method(cls):

➡️ Class method

"Does this method only need the arguments I give it?"

If yes:

@staticmethod
def method(value):

➡️ Static method

Chai example
class Chai:

    shop_name = "Sameer's Chai Shop"

    def describe(self):
        # Needs this particular chai object's data
        return f"{self.type} chai - {self.size} ml"

    @classmethod
    def shop(cls):
        # Needs class-level information
        return cls.shop_name

    @staticmethod
    def valid_size(size):
        # Doesn't need object or class
        return size in [100, 150, 200, 250]

Think of the three as:

Instance method: "Tell me about THIS chai."
Class method: "Tell me about THIS chai class."
Static method: "Just give me the data and I'll do the calculation."

That distinction will make @classmethod and @staticmethod much easier to recognize in real Python code.

'''