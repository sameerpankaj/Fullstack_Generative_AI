#Infinite generators
def infinite_chai():
    count = 1
    while True:
        yield f'Refill #{count}'
        count += 1


refill = infinite_chai()
user2 = infinite_chai()

for _ in range(3):
    print(next(refill))

for _ in range(6):
    print(next(user2))



'''
def infinite_chai():
    # Create a counter. Every new generator starts counting from 1.
    count = 1

    # This loop can continue forever.
    while True:
        # Give one refill to the caller and pause the function here.
        yield f'Refill #{count}'

        # When next() is called again, continue from here
        # and increase the counter by 1.
        count += 1


# Create the first generator.
# The function does not actually start running yet.
refill = infinite_chai()

# Create a second, completely independent generator.
# It also starts with count = 1 when it eventually runs.
user2 = infinite_chai()


# Ask the 'refill' generator for 3 values.
for _ in range(3):
    print(next(refill))


# Ask the 'user2' generator for 6 values.
for _ in range(6):
    print(next(user2))
Output
Refill #1
Refill #2
Refill #3
Refill #1
Refill #2
Refill #3
Refill #4
Refill #5
Refill #6
2. Now line by line
Line 1
def infinite_chai():

We define a function called infinite_chai.

Because this function contains yield, it is a generator function.

Line 2
count = 1

We create a counter starting at 1.

Lines 3–4
while True:

This means:

Keep repeating forever.

Normally, this would create an infinite loop.

But yield allows the generator to pause instead of continuously running.

Line 5
yield f'Refill #{count}'

This is the most important line.

It produces a value and pauses the generator.

Initially:

count = 1

So:

yield f'Refill #{count}'

produces:

Refill #1

Then the generator pauses.

Line 6
count += 1

When we call next() again, the generator continues from where it paused.

It executes:

count += 1

So:

1 → 2

Then the while True loop repeats and produces:

Refill #2
Now these two lines
refill = infinite_chai()
user2 = infinite_chai()

These create two separate generators.

Think of them as two separate chai counters:

refill → its own count
user2  → its own count

They don't share the same count.

First loop
for _ in range(3):
    print(next(refill))

range(3) means:

0
1
2

So the loop runs 3 times.

First next(refill)
Refill #1
Second next(refill)
Refill #2
Third next(refill)
Refill #3

So:

Refill #1
Refill #2
Refill #3

The important point is that refill remembers its position.

Second loop
for _ in range(6):
    print(next(user2))

Now we're using user2, not refill.

user2 is a completely separate generator.

Therefore its counter starts from:

count = 1

So we get:

Refill #1
Refill #2
Refill #3
Refill #4
Refill #5
Refill #6
🧠 The key idea

Think of:

refill = infinite_chai()
user2 = infinite_chai()

as creating two separate machines:

             infinite_chai()
                   │
          ┌────────┴────────┐
          ↓                 ↓
       refill             user2
       count               count
         1                   1

When you do:

next(refill)

only refill's counter changes.

When you do:

next(user2)

only user2's counter changes.

That's why both can produce Refill #1.

⭐ Remember this:

A generator function is the blueprint.
Each call to the generator function creates a separate generator object with its own state.

And:

yield produces a value, pauses the generator, and remembers where it stopped.

'''