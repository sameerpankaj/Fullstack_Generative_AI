# #Method Resolutoin Order(MRO)

# class A:
#     label = 'A: Base Class'

# class B(A):
#     label = 'B: Masala blend'

# class C(A):
#     label = 'C: Herbal blend'

# class D(B,C): #order of inheritance matters, here firs class B is called, so the output will be the lable of class B
#     pass

# cup = D()
# print(cup.label)


# ============================================================
# METHOD RESOLUTION ORDER (MRO)
# ============================================================


class A:
    # A is the base/parent class.

    label = 'A: Base Class'
    # A has a class attribute called label.


class B(A):
    # B inherits from A.

    label = 'B: Masala blend'
    # B defines its own label.
    #
    # This means B's label takes priority over A's label
    # when Python is looking through a B object.


class C(A):
    # C also inherits from A.

    label = 'C: Herbal blend'
    # C also defines its own label.


class D(B, C):
    # D inherits from TWO classes:
    #
    # B comes first
    # C comes second
    #
    # This is called MULTIPLE INHERITANCE.
    #
    # The order (B, C) is important because Python uses
    # this order when searching for attributes and methods.

    pass
    # pass means:
    # "There is nothing else to define inside D."
    #
    # D will inherit from B and C.


cup = D()
# Create an object of class D.
#
# cup is now a D object.


print(cup.label)
# Python needs to find "label".
#
# It searches according to D's MRO.
#
# MRO:
# D → B → C → A → object
#
# D does not have label.
# B DOES have label.
#
# Therefore Python stops at B.
#
# Output:
# B: Masala blend


'''
Output
B: Masala blend
2. What is MRO?

MRO stands for:

Method Resolution Order

It is the order Python follows when it searches for a method or attribute.

For example:

print(cup.label)

Python asks:

"Where can I find label?"

Because cup is a D object, Python follows the MRO of D.

For your classes, the important order is:

D → B → C → A → object

Python searches from left to right.

3. Why does B win?

Look at:

class D(B, C):
    pass

You have written:

B first
C second

Both B and C have a label:

class B(A):
    label = 'B: Masala blend'

and:

class C(A):
    label = 'C: Herbal blend'

So when Python executes:

cup.label

it searches:

D
↓
Does D have label? ❌

B
↓
Does B have label? ✅

STOP!

Therefore:

B: Masala blend
4. What about class A?

You might wonder:

"A also has label, so why isn't A used?"

Because Python already found label in B.

Python doesn't continue searching once it finds the required attribute.

The search is:

D
 ↓
B  ← FOUND label ✅
 ↓
C  ← NOT CHECKED
 ↓
A  ← NOT CHECKED

So A never gets a chance in this particular lookup.

5. Why is C after B?

Because you wrote:

class D(B, C):

The order matters.

If you instead wrote:

class D(C, B):
    pass

then the search would prioritize C.

The MRO would be:

D → C → B → A → object

Therefore:

cup = D()
print(cup.label)

would produce:

C: Herbal blend

So your understanding that the first parent listed has priority here is correct.

6. Let's visualize the inheritance

Your classes look like this:

             A
            / \
           /   \
          B     C
           \   /
            \ /
             D

B and C both inherit from A.

Then D inherits from both B and C.

This is called diamond inheritance because of the shape:

             A
            / \
           B   C
            \ /
             D

This is one of the situations where MRO becomes particularly important.

7. What does pass do?

You have:

class D(B, C):
    pass

pass basically means:

"Don't add anything new here."

For example, you could have written:

class D(B, C):
    pass

because you don't need to define anything inside D.

But D still gets access to things from its parent classes.

So:

cup = D()

creates a D object that can access:

D
↓
B
↓
C
↓
A

according to the MRO.

8. You can actually see the MRO

Python gives you a built-in way to see it:

print(D.mro())

You would get something similar to:

[
    <class '__main__.D'>,
    <class '__main__.B'>,
    <class '__main__.C'>,
    <class '__main__.A'>,
    <class 'object'>
]

You can also use:

print(D.__mro__)

Both show the Method Resolution Order.

For learning, you can think of it simply as:

D → B → C → A → object
9. Why is object at the end?

Every normal Python class ultimately inherits from Python's built-in:

object

So even though you didn't write:

class A(object):

Python effectively treats A as ultimately derived from object.

Therefore the complete MRO ends with:

object

For now, you mainly need to remember:

D → B → C → A → object
10. Let's change the labels to understand it better

Imagine:

class A:
    label = 'A'


class B(A):
    label = 'B'


class C(A):
    label = 'C'


class D(B, C):
    pass

Now:

cup = D()

print(cup.label)

Python searches:

D → B → C → A

and finds:

B

So:

B

is printed.

11. What if D had its own label?

Suppose:

class D(B, C):
    label = 'D'

Now the search becomes:

D
↓
label found! ✅

So:

print(cup.label)

would output:

D

The search would never reach B or C.

This gives us an important rule:

Python starts with the object's class and follows the MRO until it finds the requested attribute/method.

12. What if B didn't have label?

Suppose:

class B(A):
    pass

Then:

class C(A):
    label = 'C: Herbal blend'

Now:

cup = D()
print(cup.label)

The search would be:

D
↓
B       ❌ no label
↓
C       ✅ label found

Output:

C: Herbal blend

So Python doesn't simply say:

"B is first, therefore B wins."

More accurately:

Python searches the MRO from left to right and uses the first class that actually provides the requested attribute or method.

That's a very important distinction.

13. Your example step-by-step

When you write:

cup = D()

you create:

cup
 ↓
D object

Then:

print(cup.label)

Python essentially asks:

Step 1

Does D have label?

D → ❌
Step 2

Does B have label?

B → ✅

So Python gets:

'B: Masala blend'

and prints it.

It does not continue to C or A.

⭐ The key concept to remember

Your code:

class D(B, C):

creates an MRO roughly like:

D
 ↓
B   ← first priority
 ↓
C   ← second priority
 ↓
A
 ↓
object

Therefore:

cup.label

means:

"Start at D and follow its MRO until you find label."

Since B has label, the result is:

B: Masala blend
🧠 Easy memory trick

Think of MRO as Python asking:

"Where should I look first, second, third...?"

For:

class D(B, C):

Python starts:

D → B → C → A → object
     ↑
   first parent

So the inheritance order matters, but the deeper rule is first matching attribute/method in the MRO wins.

'''