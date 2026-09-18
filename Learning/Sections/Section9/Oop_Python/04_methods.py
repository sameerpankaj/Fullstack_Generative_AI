#methods
#functions created inside class are called methods

# class Chaicup:
#     size = 150 #ml

#     def describe(self):
#         return f'A {self.size} ml cup chai cup'


# cup = Chaicup()
# print(cup.describe())
# print(Chaicup.describe(cup))

# cup_two = Chaicup()
# cup_two.size = 100
# print(Chaicup.describe(cup_two))


class Chaicup:
    size = 150  # Class attribute: every Chaicup starts with 150 ml

    def describe(self):
        # self refers to the particular object calling this method
        return f'{self.size} ml cup chai cup'


cup = Chaicup()
# Creates an object called cup.
# Since we didn't give it its own size, it uses the class attribute: 150


print(cup.describe())
# Python automatically passes cup as self.
# Same as: Chaicup.describe(cup)
# Output: 150 ml cup chai cup


print(Chaicup.describe(cup))
# Here we call the method through the class.
# We manually provide cup as the self argument.
# Output: 150 ml cup chai cup


cup_two = Chaicup()
# Creates another Chaicup object.


cup_two.size = 100
# Creates an instance attribute called size for cup_two.
# This overrides the class attribute for this particular object.


print(Chaicup.describe(cup_two))
# We manually pass cup_two as self.
# self.size therefore means cup_two.size, which is 100.
# Output: 100 ml cup chai cup


'''
Output
150 ml cup chai cup
150 ml cup chai cup
100 ml cup chai cup
The most important concept: self

Think of:

cup = Chaicup()

as creating a real cup object.

When you write:

cup.describe()

Python essentially does:

Chaicup.describe(cup)

So this:

def describe(self):

means:

"Give me the object that is calling this method."

Therefore:

self.size

means:

"Get the size belonging to the object currently being used."

Why does cup_two give 100?

Initially the class says:

class Chaicup:
    size = 150

So:

cup.size

is 150.

And:

cup_two.size

is also 150.

But then:

cup_two.size = 100

gives only cup_two its own size.

So now:

Class Chaicup → size = 150

cup            → no personal size → uses 150
cup_two        → personal size = 100

Therefore:

cup.describe()

→ 150 ml cup chai cup

while:

cup_two.describe()

→ 100 ml cup chai cup

One very useful rule

Remember this:

object.method()

is generally equivalent to:

Class.method(object)

So:

cup.describe()

is equivalent to:

Chaicup.describe(cup)

and:

cup_two.describe()

is equivalent to:

Chaicup.describe(cup_two)

That's why self is so important: self tells the method which object it is working with.

'''