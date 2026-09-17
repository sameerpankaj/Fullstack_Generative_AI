# #attribute shadowing
# class Chai:
#     temperature = 'hot'
#     strength = 'Strong'


# cutting = Chai()
# print(cutting.temperature)

# cutting.temperature = 'Mild'
# cutting.cup = 'small'
# print('After Changing ' ,cutting.temperature)
# print('Cup size is ' ,cutting.cup)
# print('Direct look into the class ', Chai.temperature)

# del cutting.temperature
# del cutting.cup

# print(cutting.temperature)
# print(cutting.cup)
# Create a class called Chai
class Chai:

    # Class attribute
    temperature = 'hot'

    # Another class attribute
    strength = 'Strong'


# Create an object (instance) of Chai
cutting = Chai()


# The object doesn't have its own temperature yet,
# so Python gets temperature from the class
print(cutting.temperature)


# Create an instance attribute called temperature
# This shadows the class attribute
cutting.temperature = 'Mild'


# Create a new instance attribute called cup
cutting.cup = 'small'


# Now Python finds cutting.temperature first
print('After Changing', cutting.temperature)

# cup belongs directly to the cutting object
print('Cup size is', cutting.cup)


# The class attribute has NOT changed
print('Direct look into the class', Chai.temperature)


# Delete the object's own temperature attribute
del cutting.temperature


# Delete the object's cup attribute
del cutting.cup


# Now cutting no longer has its own temperature,
# so Python looks at the class again
print(cutting.temperature)


# cup was an instance attribute and there is no cup
# attribute in the Chai class
print(cutting.cup)



'''
First: the class attributes
class Chai:
    temperature = 'hot'
    strength = 'Strong'

We have two class attributes:

Chai
 ├── temperature = 'hot'
 └── strength = 'Strong'

They belong to the class Chai.

3. Create the object
cutting = Chai()

Now we have an object:

Chai (class)
       ↓
   cutting (object)

At this point, cutting doesn't have its own temperature.

So when you write:

print(cutting.temperature)

Python looks for temperature.

Python searches:
cutting
   ↓
Does cutting have temperature?
   ↓
NO
   ↓
Look in Chai
   ↓
temperature = 'hot'

Output:

hot
4. Attribute shadowing ⭐

Now:

cutting.temperature = 'Mild'

This does not change:

Chai.temperature

Instead, it creates a new attribute specifically inside cutting.

Now we have:

Chai
 └── temperature = 'hot'

cutting
 └── temperature = 'Mild'

There are now two different temperature attributes.

5. Why is this called shadowing?

When you do:

cutting.temperature

Python finds:

cutting.temperature = 'Mild'

before it gets to:

Chai.temperature = 'hot'

So the object's value hides/shadows the class value.

That's why:

print(cutting.temperature)

gives:

Mild

But:

print(Chai.temperature)

still gives:

hot
⭐ Remember:

Instance attribute → shadows → class attribute

6. Creating cup

Now:

cutting.cup = 'small'

There is no cup in the class.

So this simply creates an attribute on the object:

cutting
 ├── temperature = Mild
 └── cup = small

Therefore:

print(cutting.cup)

outputs:

small
7. The class has NOT changed

This line:

print('Direct look into the class', Chai.temperature)

outputs:

Direct look into the class hot

Why?

Because:

cutting.temperature = 'Mild'

only changed the object.

It did not change:

Chai.temperature

So:

Chai.temperature → hot
cutting.temperature → Mild
8. What does del cutting.temperature do?

Now:

del cutting.temperature

This deletes the instance attribute:

cutting.temperature

It does NOT delete:

Chai.temperature

So after deletion:

Chai
 └── temperature = hot

cutting
 └── temperature → doesn't exist anymore

Now if you do:

print(cutting.temperature)

Python searches:

cutting
   ↓
temperature?
   ↓
NO
   ↓
Chai
   ↓
temperature = hot

Therefore:

hot

This is a very useful concept.

9. What happens to cup?

You also did:

del cutting.cup

That completely removes the cup attribute from cutting.

Then:

print(cutting.cup)

Python searches:

cutting
   ↓
cup?
   ↓
NO
   ↓
Chai
   ↓
cup?
   ↓
NO

So Python raises:

AttributeError

Something like:

AttributeError: 'Chai' object has no attribute 'cup'

⚠️ Therefore, your last line will cause an error.

⭐ Complete flow

Initially:

Chai
 ├── temperature = hot
 └── strength = Strong

cutting
 └── nothing of its own

After:

cutting.temperature = 'Mild'
cutting.cup = 'small'

we have:

Chai
 ├── temperature = hot
 └── strength = Strong

cutting
 ├── temperature = Mild  ← shadows class attribute
 └── cup = small

After:

del cutting.temperature
del cutting.cup

we have:

Chai
 ├── temperature = hot
 └── strength = Strong

cutting
 └── nothing of its own

Therefore:

cutting.temperature

→ hot ✅

But:

cutting.cup

→ AttributeError ❌

🧠 One simple rule to remember

When you write:

object.attribute

Python basically looks:

1️⃣ Check the object
       ↓
2️⃣ If not found, check the class
       ↓
3️⃣ If still not found → AttributeError

So attribute shadowing happens when:

Chai.temperature = 'hot'

cutting.temperature = 'Mild'

The object has its own temperature, so Mild shadows hot.

'''