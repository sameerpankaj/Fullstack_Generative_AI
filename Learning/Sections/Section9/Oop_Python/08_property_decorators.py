# class TeaLeaf:
#     def __init__(self, age):
#         self._age = age


#     @property
#     def age(self):
#         return self._age + 2

#     @age.setter
#     def age(self, age):
#         if 1 <= age <= 5:
#             self._age = age
#         else:
#             raise ValueError('Tea leaf age must be  between 1 and 5 years')

# leaf = TeaLeaf(2)
# print(leaf.age)
# leaf.age = 4
# print(leaf.age)

class TeaLeaf:

    # Constructor / initializer method
    # 'self' refers to the current object (instance)
    # 'age' is the value passed when creating the object
    def __init__(self, age):

        # '_age' is an instance attribute.
        # The leading '_' is a convention meaning:
        # "This attribute is intended for internal use."
        self._age = age


    # @property converts this method into a property.
    # This method is called the "getter".
    # It allows us to access age like an attribute:
    #     leaf.age
    # instead of:
    #     leaf.age()
    @property
    def age(self):

        # Return the internal _age value + 2
        return self._age + 2


    # @age.setter defines the "setter" for the age property.
    # It is automatically called when we write:
    #     leaf.age = 4
    @age.setter
    def age(self, age):

        # Validate the new age.
        # Only values between 1 and 5 are accepted.
        if 1 <= age <= 5:

            # Store the validated value in the internal attribute.
            self._age = age

        else:

            # Raise an exception if the value is invalid.
            raise ValueError(
                'Tea leaf age must be between 1 and 5 years'
            )


# Create a TeaLeaf object.
# __init__() is automatically called.
# age = 2
leaf = TeaLeaf(2)


# Access the age property.
# This automatically calls the getter:
#     age(self)
#
# _age = 2
# getter returns 2 + 2 = 4
print(leaf.age)


# Assign a new value to the age property.
# This automatically calls the setter:
#     age(self, 4)
#
# The setter checks:
#     1 <= 4 <= 5
# True
#
# Then:
#     self._age = 4
leaf.age = 4


# Access the property again.
# Getter returns:
#     self._age + 2
#     4 + 2
#     6
print(leaf.age)



'''

Output
4
6
🔑 What is actually happening?

The most important thing to understand is that:

leaf.age

looks like normal attribute access, but Python is actually calling your @property method.

When you write:
print(leaf.age)

Python effectively does:

TeaLeaf.age.__get__(leaf, TeaLeaf)

You don't normally need to write that yourself, but internally the property mechanism uses the descriptor protocol.

Your getter:

@property
def age(self):
    return self._age + 2

gets executed.

When you write leaf.age = 4

This is even more important.

You might think Python simply does:

leaf.age = 4

But because age has a setter:

@age.setter
def age(self, age):

Python calls the setter.

Conceptually:

leaf.age = 4
       │
       ▼
@age.setter
       │
       ▼
age(self, 4)
       │
       ▼
1 <= 4 <= 5 ?
       │
      YES
       │
       ▼
self._age = 4
📚 Technical terms you should know
Term	Meaning in your code
Class	TeaLeaf — blueprint for creating objects
Object / Instance	leaf — an actual TeaLeaf object
Constructor / Initializer	__init__() initializes the object
Instance attribute	self._age — data stored inside each object
self	Reference to the current object
Property	age — controlled access to an attribute
Getter	@property def age(self) — reads/gets the value
Setter	@age.setter def age(...) — changes/sets the value
Decorator	@property, @age.setter — modifies how methods behave
Encapsulation	Controlling access to internal data
Data validation	Checking 1 <= age <= 5 before storing
Private-like attribute	_age — underscore indicates internal-use convention
Exception	ValueError — signals invalid input
Descriptor	Python mechanism behind property
Getter logic	return self._age + 2
Setter logic	Validates and updates _age
⭐ Why use @property?

Without a property, you could simply do:

class TeaLeaf:

    def __init__(self, age):
        self.age = age

Then someone could do:

leaf.age = 100

There is no validation.

With a property:

@age.setter
def age(self, age):
    if 1 <= age <= 5:
        self._age = age
    else:
        raise ValueError(...)

you control what values can be assigned.

So:

leaf.age = 4     # ✅
leaf.age = 1     # ✅
leaf.age = 5     # ✅
leaf.age = 10    # ❌ ValueError

This is one of the main reasons properties are useful.

⚠️ One unusual thing in your example

Your getter says:

return self._age + 2

So the value you store and the value you see are different.

For example:

leaf = TeaLeaf(2)

Internally:

self._age = 2

But:

print(leaf.age)

returns:

2 + 2 = 4

Then:

leaf.age = 4

stores:

self._age = 4

but:

print(leaf.age)

returns:

4 + 2 = 6

So remember:

             Internal value       Public value
             ──────────────       ────────────
             self._age            leaf.age
                  │                    │
                  │                    │
                2                    2 + 2
                                      ↓
                                      4

The + 2 is just logic you've intentionally put into the getter.

🧠 The most important pattern to memorize
class Example:

    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        # GETTER
        return self._value

    @value.setter
    def value(self, value):
        # SETTER
        # validation
        self._value = value

Then you can use it naturally:

obj = Example(10)

print(obj.value)   # getter

obj.value = 20     # setter

print(obj.value)   # getter
One-line memory trick

@property = GET
@age.setter = SET
_age = INTERNAL DATA
validation = protect the data

'''
