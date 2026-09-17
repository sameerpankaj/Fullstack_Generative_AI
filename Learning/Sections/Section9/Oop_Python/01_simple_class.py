# #class


# class Chai:
#     pass

# class ChaiTime:
#     pass


# print(type(Chai))

# ginger_tea = Chai()
# print(type(ginger_tea))
# print(type(ginger_tea) is Chai)
# print(type(ginger_tea) is ChaiTime)


# Create a class called Chai
class Chai:
    pass


# Create another class called ChaiTime
class ChaiTime:
    pass


# Print the type of Chai itself
print(type(Chai))


# Create an object (instance) of the Chai class
ginger_tea = Chai()


# Print the type of the ginger_tea object
print(type(ginger_tea))


# Check whether ginger_tea is an object of the Chai class
print(type(ginger_tea) is Chai)


# Check whether ginger_tea is an object of the ChaiTime class
print(type(ginger_tea) is ChaiTime)



'''
Output
<class 'type'>
<class '__main__.Chai'>
True
False
1. What is a class?
class Chai:
    pass

A class is like a blueprint/template.

Think:

Chai = blueprint

It doesn't create a specific cup of tea yet.

pass simply means:

"There is nothing inside this class yet."

2. Another class
class ChaiTime:
    pass

This creates a completely separate class.

Chai       → one class
ChaiTime   → another class

Even though both classes are empty, they are different.

3. What is type(Chai)?
print(type(Chai))

Output:

<class 'type'>

This can initially look confusing.

You might think:

"Shouldn't the type of Chai be Chai?"

No.

Chai is the class itself.

In Python, classes are themselves objects, and the type of a class is normally type.

So:

Chai
  ↓
a class object
  ↓
type = type

Therefore:

type(Chai)

gives:

<class 'type'>
4. Creating an object
ginger_tea = Chai()

This is very important.

You are creating an object/instance from the Chai class.

Think of it like:

Class (blueprint)
       ↓
     Chai
       ↓
     Chai()
       ↓
Object
       ↓
ginger_tea

So:

ginger_tea

is an instance of Chai.

5. type(ginger_tea)
print(type(ginger_tea))

Output:

<class '__main__.Chai'>

This tells you:

ginger_tea is an object created from the Chai class.

So:

type(ginger_tea)

is:

Chai
6. is Chai

Now:

print(type(ginger_tea) is Chai)

We know:

type(ginger_tea)

is:

Chai

Therefore Python is effectively checking:

Chai is Chai

That's True.

Output:

True
7. is ChaiTime

Now:

print(type(ginger_tea) is ChaiTime)

But:

type(ginger_tea)

is Chai.

You're checking:

Chai is ChaiTime

They are different classes.

Therefore:

False
⭐ Remember this

There are three different things here:

class Chai:
    pass
1. Chai

The class/blueprint

2. Chai()

Creates an object

3. ginger_tea

The object/instance

So:

ginger_tea = Chai()

means:

"Create an object from the Chai class and store it in ginger_tea."

And:

type(ginger_tea) is Chai

means:

"Is ginger_tea directly an instance of the Chai class?"

Answer:

True ✅

Whereas:

type(ginger_tea) is ChaiTime

means:

"Is ginger_tea an instance of ChaiTime?"

Answer:

False ❌
Easy analogy ☕
Chai = blueprint for a tea cup

ginger_tea = actual tea cup made using that blueprint

ChaiTime = different blueprint

So:

type(ginger_tea) is Chai

✅ True

type(ginger_tea) is ChaiTime

❌ False

'''