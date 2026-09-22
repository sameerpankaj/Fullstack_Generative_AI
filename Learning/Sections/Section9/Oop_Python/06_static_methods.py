# #static methods

# class ChaiUtilities:
#     @staticmethod
#     def clean_ingredients(text):
#         return [item.strip() for item in text.split(',')]


# raw = 'water , milk , ginger , honey '

# # obj = ChaiUtilities()
# # obj.clean_ingredients(raw)

# cleaned = ChaiUtilities.clean_ingredients(raw)
# print(cleaned)


# ============================================================
# STATIC METHOD
# ============================================================

class ChaiUtilities:
    # ChaiUtilities is a class that contains utility/helper functions.

    @staticmethod
    def clean_ingredients(text):
        # @staticmethod tells Python that this method does NOT
        # need self or cls.
        #
        # text is simply a normal parameter.

        return [item.strip() for item in text.split(',')]
        # text.split(',')
        # ----------------
        # Splits the string wherever there is a comma.
        #
        # Example:
        # 'water , milk , ginger , honey '
        #
        # becomes approximately:
        # ['water ', ' milk ', ' ginger ', ' honey ']
        #
        # item.strip()
        # -----------
        # Removes spaces from the beginning and end of each item.
        #
        # So the final result becomes:
        # ['water', 'milk', 'ginger', 'honey']


raw = 'water , milk , ginger , honey '
# This is the original/raw ingredient string.


# obj = ChaiUtilities()
# Creates an object of ChaiUtilities.
#
# obj.clean_ingredients(raw)
# We could call the static method through the object.
# However, creating an object is unnecessary here because
# clean_ingredients() does not use self or any object data.


cleaned = ChaiUtilities.clean_ingredients(raw)
# Call the static method directly through the class.
#
# raw is passed as the 'text' parameter.


print(cleaned)
# Print the cleaned list of ingredients.


'''

Output
['water', 'milk', 'ginger', 'honey']
2. What is a static method?

Normally, when we create a method inside a class:

class Chai:

    def prepare(self):
        ...

we need self because the method works with a particular object.

For example:

chai.prepare()

Here:

self → chai

But your method:

clean_ingredients()

doesn't need a particular Chai object.

It simply takes some text:

raw = 'water , milk , ginger , honey '

and cleans it.

Therefore we don't need:

self

or:

cls

That's exactly what @staticmethod is for.

3. What does @staticmethod do?

You have:

@staticmethod
def clean_ingredients(text):

The:

@staticmethod

is a decorator.

It tells Python:

"Treat this method as a static method. Don't automatically pass self or cls."

So when you call:

ChaiUtilities.clean_ingredients(raw)

Python simply passes:

raw → text

There is no automatic:

self
4. Compare with a normal instance method
Normal method
class Chai:

    def prepare(self):
        print("Preparing chai")

Call:

chai = Chai()
chai.prepare()

Python effectively does:

Chai.prepare(chai)

So:

self → chai
Static method
class ChaiUtilities:

    @staticmethod
    def clean_ingredients(text):
        return text.strip()

Call:

ChaiUtilities.clean_ingredients(raw)

Python does not add an object:

text → raw

That's the key difference.

5. Why don't we need an object?

You commented out:

# obj = ChaiUtilities()
# obj.clean_ingredients(raw)

You could technically do this:

obj = ChaiUtilities()
obj.clean_ingredients(raw)

It would work.

But it's unnecessary.

Why?

Because clean_ingredients() doesn't use anything from obj.

For example, there is no:

self.some_variable

inside the method.

The method only works with:

text

Therefore:

ChaiUtilities.clean_ingredients(raw)

is cleaner.

6. Understanding this line

The most complicated-looking line is:

return [item.strip() for item in text.split(',')]

Let's break it down.

First:
text.split(',')

Your text is:

'water , milk , ginger , honey '

When you split using ,:

text.split(',')

you get:

['water ', ' milk ', ' ginger ', ' honey ']

Notice the spaces.

For example:

'water '
' milk '
' ginger '
' honey '
7. Then .strip()

.strip() removes whitespace from the beginning and end.

For example:

' water '.strip()

becomes:

'water'

Similarly:

' milk '.strip()

becomes:

'milk'

Therefore:

'water '  → 'water'
' milk '  → 'milk'
' ginger ' → 'ginger'
' honey '  → 'honey'
8. What is the list comprehension?

This:

[item.strip() for item in text.split(',')]

is called a list comprehension.

It's a shorter way of writing a loop.

The original:

ingredients = []

for item in text.split(','):
    ingredients.append(item.strip())

return ingredients

does exactly the same thing.

The list comprehension:

[item.strip() for item in text.split(',')]

just makes it shorter.

9. Let's visualize the entire process

Starting with:

raw = 'water , milk , ginger , honey '
Step 1
text.split(',')

gives:

['water ', ' milk ', ' ginger ', ' honey ']
Step 2

Apply:

item.strip()

to each item:

'water '  → 'water'
' milk '  → 'milk'
' ginger ' → 'ginger'
' honey '  → 'honey'
Step 3

Put them into a new list:

['water', 'milk', 'ginger', 'honey']
Step 4

Store it:

cleaned = [...]
Step 5

Print:

print(cleaned)

Output:

['water', 'milk', 'ginger', 'honey']
10. Why is this a good static method?

Think about the purpose of the class:

class ChaiUtilities:

It's a collection of chai-related utility functions.

For example, you could have:

class ChaiUtilities:

    @staticmethod
    def clean_ingredients(text):
        ...

    @staticmethod
    def calculate_price(quantity, price):
        ...

    @staticmethod
    def convert_ml_to_liters(ml):
        ...

None of these necessarily need a Chai object.

So you could use:

ChaiUtilities.clean_ingredients(raw)

or:

ChaiUtilities.calculate_price(3, 2.5)

without creating an object.

11. Static method vs normal method

This distinction is important:

Type	First parameter	Needs object?	Typical call
Instance method	self	Yes	obj.method()
Static method	None automatically	No	Class.method()
Class method	cls	No object	Class.method()

For now, focus on these two:

Instance method
class Chai:

    def describe(self):
        return self.type

It needs self because it needs information from a specific object.

Static method
class ChaiUtilities:

    @staticmethod
    def clean_ingredients(text):
        return text.strip()

It doesn't need an object. It's simply a utility function logically grouped inside the class.

🧠 Easy memory trick

Think:

Instance method:

"I need to know which chai object I'm working with."

chai.prepare()

→ needs self.

Static method:

"Give me some data and I'll do a job. I don't care about any particular object."

ChaiUtilities.clean_ingredients(raw)

→ no self.

So in your example, @staticmethod is appropriate because clean_ingredients() only works with the text you give it; it doesn't need any information stored inside a ChaiUtilities object.

'''