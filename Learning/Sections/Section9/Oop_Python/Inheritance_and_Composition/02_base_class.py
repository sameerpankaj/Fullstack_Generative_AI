# #base class


# class Chai:
#     def __init__(self, type_, strength):
#         self.type = type_
#         self.strength = strength

# #deriving base class using code duplication
# # class GingerChai(Chai):
# #     def __init__(self, type_, strength, spice_level):
# #         self.type =type
# #         self.strength = strength
# #         self.spice_level = spice_level



# #deriving base class using explicit call
# # class GingerChai(Chai):
# #     def __init__(self, type_, strength, spice_level):
# #         Chai.__init__(self, type_, strength)
# #         self.spice_level = spice_level


# #super() method to derive base class
# class GingerChai(Chai):
#     def __init__(self, type_, strength):
#         super().__init__(type_, strength)
#         self.spice_level = self.spice_level

# ============================================================
# BASE CLASS
# ============================================================

class Chai:

    def __init__(self, type_, strength):
        # __init__() is automatically called when a Chai object
        # or a child-class object is created.
        #
        # self      -> refers to the current object
        # type_     -> chai type passed by the user
        # strength  -> chai strength passed by the user

        self.type = type_
        # Store the chai type inside the object.
        # Example:
        # self.type = 'Masala'

        self.strength = strength
        # Store the chai strength inside the object.
        # Example:
        # self.strength = 'Strong'


# ============================================================
# DERIVING CHILD CLASS USING CODE DUPLICATION
# ============================================================

# class GingerChai(Chai):
#     # GingerChai inherits from Chai.
#
#     def __init__(self, type_, strength, spice_level):
#         # We have to initialize three attributes:
#         # type_, strength, and spice_level
#
#         self.type = type_
#         # This is copied from the parent Chai class.
#
#         self.strength = strength
#         # This is also copied from the parent Chai class.
#
#         self.spice_level = spice_level
#         # This is new and specific to GingerChai.
#
#
# PROBLEM:
# We are duplicating the code from Chai.__init__().
# If the parent class changes, we would need to update
# this code manually as well.


# ============================================================
# DERIVING CHILD CLASS USING EXPLICIT PARENT CALL
# ============================================================

# class GingerChai(Chai):
#     # GingerChai inherits from Chai.
#
#     def __init__(self, type_, strength, spice_level):
#
#         Chai.__init__(self, type_, strength)
#         # Explicitly call the parent's __init__() method.
#         #
#         # This allows Chai to take care of:
#         # self.type
#         # self.strength
#
#         self.spice_level = spice_level
#         # GingerChai takes care of its own additional attribute.
#
#
# This is better than code duplication because we reuse
# the parent's __init__() method.
# However, we have to explicitly write the parent class name:
# Chai.__init__(...)


# ============================================================
# DERIVING CHILD CLASS USING super()
# ============================================================

class GingerChai(Chai):
    # GingerChai is a child/subclass of Chai.
    #
    # Therefore GingerChai inherits things from Chai,
    # including its __init__() method.
    #
    # We are going to override __init__() because
    # GingerChai needs one additional value: spice_level.

    def __init__(self, type_, strength, spice_level):
        # GingerChai's __init__() receives three values:
        #
        # type_       -> type of chai
        # strength    -> strength of chai
        # spice_level -> amount/level of spices

        super().__init__(type_, strength)
        # super() refers to the parent class.
        #
        # Therefore this calls:
        #
        # Chai.__init__(self, type_, strength)
        #
        # The parent class handles:
        # self.type
        # self.strength

        self.spice_level = spice_level
        # GingerChai handles its own additional attribute.



'''

1. Base class

Your base class is:

class Chai:

    def __init__(self, type_, strength):
        self.type = type_
        self.strength = strength
What does this do?

Chai is the parent/base class.

When you create:

chai = Chai('Masala', 'Strong')

Python calls:

__init__(chai, 'Masala', 'Strong')

So:

self.type = type_

becomes:

chai.type = 'Masala'

And:

self.strength = strength

becomes:

chai.strength = 'Strong'

So the object contains:

chai
 ├── type = "Masala"
 └── strength = "Strong"
2. First commented approach — code duplication

You had:

# class GingerChai(Chai):
#     def __init__(self, type_, strength, spice_level):
#         self.type = type_
#         self.strength = strength
#         self.spice_level = spice_level

This is technically possible.

Here:

class GingerChai(Chai):

means:

GingerChai inherits from Chai.

But then you duplicate the parent's initialization code:

self.type = type_
self.strength = strength

The parent already has exactly this code:

class Chai:

    def __init__(self, type_, strength):
        self.type = type_
        self.strength = strength

So duplication isn't ideal.

Why?

Imagine the parent later changes:

self.strength = strength.upper()

You would have to remember to change the duplicated code in GingerChai too.

That's why we normally reuse the parent's __init__().

3. Second commented approach — explicitly calling the parent

You then showed:

# class GingerChai(Chai):
#     def __init__(self, type_, strength, spice_level):
#         Chai.__init__(self, type_, strength)
#         self.spice_level = spice_level

This is much better.

Here:

Chai.__init__(self, type_, strength)

means:

"Run the __init__() method from the Chai class for this GingerChai object."

Suppose:

ginger = GingerChai('Ginger', 'Strong', 5)

Then:

Chai.__init__(self, type_, strength)

effectively does:

ginger.type = 'Ginger'
ginger.strength = 'Strong'

Then:

self.spice_level = spice_level

does:

ginger.spice_level = 5

So you get:

ginger
 ├── type = "Ginger"
 ├── strength = "Strong"
 └── spice_level = 5

This works.

4. The modern/recommended approach: super()

Instead of:

Chai.__init__(self, type_, strength)

Python gives us:

super().__init__(type_, strength)

So your idea of the final code is correct, but your final code has two mistakes.

You wrote:

class GingerChai(Chai):

    def __init__(self, type_, strength):
        super().__init__(type_, strength)
        self.spice_level = self.spice_level
❌ Problem 1: spice_level isn't a parameter

You have:

def __init__(self, type_, strength):

but you need:

def __init__(self, type_, strength, spice_level):

because GingerChai needs to receive a spice level.

❌ Problem 2: this line is incorrect

You wrote:

self.spice_level = self.spice_level

You're saying:

"Take self.spice_level and assign it back to self.spice_level."

But self.spice_level doesn't exist yet!

You need:

self.spice_level = spice_level
5. Correct version
class Chai:
    # Base/parent class

    def __init__(self, type_, strength):
        # Initialize the attributes common to all chai types

        self.type = type_
        self.strength = strength


class GingerChai(Chai):
    # GingerChai inherits from Chai

    def __init__(self, type_, strength, spice_level):

        # Call the parent's __init__()
        # This sets:
        # self.type
        # self.strength

        super().__init__(type_, strength)

        # Now add something specific to GingerChai
        self.spice_level = spice_level

Now:

ginger = GingerChai('Ginger', 'Strong', 5)

print(ginger.type)
print(ginger.strength)
print(ginger.spice_level)

Output:

Ginger
Strong
5
6. Understanding super() visually

This is probably the most important part.

You have:

             Chai
              │
              │ parent
              ↓
         GingerChai

Chai knows how to create:

type
strength

GingerChai needs:

type
strength
spice_level

So GingerChai says:

"Parent, you take care of type and strength. I'll take care of spice_level."

That's exactly what this does:

super().__init__(type_, strength)

Then:

self.spice_level = spice_level

adds the special GingerChai attribute.

7. What happens step by step?

When you do:

ginger = GingerChai('Ginger', 'Strong', 5)

Python enters:

def __init__(self, type_, strength, spice_level):

Values are:

self         → ginger object
type_        → "Ginger"
strength     → "Strong"
spice_level  → 5

Then:

super().__init__(type_, strength)

calls the parent's:

Chai.__init__(self, type_, strength)

which creates:

self.type = type_
self.strength = strength

So now:

ginger
 ├── type = "Ginger"
 └── strength = "Strong"

Then GingerChai continues:

self.spice_level = spice_level

Now:

ginger
 ├── type = "Ginger"
 ├── strength = "Strong"
 └── spice_level = 5
8. Difference between the three approaches
Approach 1 — duplication ❌
class GingerChai(Chai):
    def __init__(self, type_, strength, spice_level):
        self.type = type_
        self.strength = strength
        self.spice_level = spice_level

You rewrite the parent's code.

Approach 2 — explicit parent call ✅
class GingerChai(Chai):
    def __init__(self, type_, strength, spice_level):
        Chai.__init__(self, type_, strength)
        self.spice_level = spice_level

Works, but you explicitly mention the parent class.

Approach 3 — super() ⭐
class GingerChai(Chai):
    def __init__(self, type_, strength, spice_level):
        super().__init__(type_, strength)
        self.spice_level = spice_level

This is generally the preferred approach.

🧠 Easy way to remember

Think of super() as:

"Go to my parent and use its version of this method."

So:

super().__init__(type_, strength)

means:

"Parent Chai, please run your __init__() and set up the things you know about."

Then:

self.spice_level = spice_level

means:

"Now I'll add the thing that is special to GingerChai."

Final mental model
Chai
 │
 ├── type
 └── strength
       ↑
       │ inherited through super()
       │
GingerChai
 │
 └── spice_level

So the child reuses the parent's initialization instead of duplicating it, then adds its own additional attribute.


'''