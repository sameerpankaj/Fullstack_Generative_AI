# class Chai:
#     origin = 'India'#property


# print(Chai.origin)

# Chai.is_hot = True
# print(Chai.is_hot)

# #creating objects from class Chai
# masala = Chai() #this object will have all the properties of class Chai
# print(f'Masala {masala.origin}')
# print(f'Masala {masala.is_hot}')

# masala.is_hot = False

# print('Class: ', Chai.is_hot)
# print(f'Masala {masala.is_hot}')
# masala.flavor = 'Masala'
# print(masala.flavor)

# Create a class called Chai
class Chai:

    # Class attribute / property
    # This belongs to the Chai class
    origin = 'India'


# Access the class attribute directly through the class
print(Chai.origin)


# Add another class attribute
Chai.is_hot = True

# Access the class attribute
print(Chai.is_hot)


# Create an object (instance) from the Chai class
masala = Chai()


# The object can access the class attribute
print(f'Masala {masala.origin}')

# The object can also access this class attribute
print(f'Masala {masala.is_hot}')


# Create/change an attribute specifically for the masala object
masala.is_hot = False


# The class attribute is still True
print('Class:', Chai.is_hot)

# But the masala object's is_hot is now False
print(f'Masala {masala.is_hot}')


# Create a new attribute only for the masala object
masala.flavor = 'Masala'

# Access the object's new attribute
print(masala.flavor)

'''
Output
India
True
Masala India
Masala True
Class: True
Masala False
Masala
2. First important concept: Class attribute
class Chai:
    origin = 'India'

Here:

origin = 'India'

is a class attribute.

Think of it as a property that belongs to the class.

Chai
 └── origin = India

You can access it with:

Chai.origin

Output:

India
3. Adding another class attribute

You can also add an attribute later:

Chai.is_hot = True

Now the class has:

Chai
 ├── origin = India
 └── is_hot = True

Therefore:

print(Chai.is_hot)

gives:

True
4. Creating an object
masala = Chai()

This creates an object/instance of the Chai class.

Think:

             Chai
          (Class)
             │
             │ creates
             ↓
          masala
          (Object)

The object can access the class attributes:

masala.origin

So:

print(masala.origin)

gives:

India

And:

masala.is_hot

gives:

True
5. Very important: masala.is_hot = False

Now we do:

masala.is_hot = False

This is where things become interesting.

You are not changing the class attribute.

You are creating an instance attribute specifically for masala.

Before:

Chai
 └── is_hot = True

masala
 └── no is_hot of its own
      ↓
      uses Chai.is_hot → True

After:

masala.is_hot = False

we have:

Chai
 └── is_hot = True

masala
 └── is_hot = False

So:

print(Chai.is_hot)

gives:

True

But:

print(masala.is_hot)

gives:

False
⭐ Why does this happen?

Python first looks for the attribute inside the object.

When you write:

masala.is_hot

Python checks:

Step 1

Does masala have its own is_hot?

Yes:

masala.is_hot = False

So Python uses:

False

It doesn't need to look at the class.

If masala didn't have its own is_hot, Python would look at the class:

masala
  ↓
Does masala have is_hot?
  ↓
No
  ↓
Look at Chai
  ↓
Chai.is_hot = True
  ↓
True

This is a very important OOP concept.

6. Adding flavor

Finally:

masala.flavor = 'Masala'

This creates a new attribute only for the masala object.

So now:

Chai
 ├── origin = India
 └── is_hot = True

masala
 ├── is_hot = False
 └── flavor = Masala

Notice:

Chai.flavor

doesn't exist.

But:

masala.flavor

does.

Therefore:

print(masala.flavor)

outputs:

Masala
🧠 Class attribute vs Object attribute
Attribute	Belongs to	Example
Class attribute	Class	Chai.origin
Instance attribute	Individual object	masala.flavor
Class attribute accessible through object	Yes	masala.origin
Instance attribute accessible through class	No	Chai.flavor ❌
Think about it like this ☕
             CLASS
             Chai
       ┌─────────────────┐
       │ origin = India   │
       │ is_hot = True    │
       └─────────────────┘
              ↓
           creates
              ↓
          OBJECT
          masala
       ┌─────────────────┐
       │ is_hot = False  │
       │ flavor = Masala │
       └─────────────────┘
⭐ The key rule

Class attributes are shared/default values. Instance attributes belong to one specific object.

So if you create another object:

ginger = Chai()

then:

print(ginger.origin)
print(ginger.is_hot)

will give:

India
True

because ginger doesn't have its own origin or is_hot.

But masala has its own:

masala.is_hot = False

so its value is different.


'''