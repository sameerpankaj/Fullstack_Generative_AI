# def local_chai():
#     yield 'Masala Chai'
#     yield 'Ginger Chai'


# def imported_chai():
#     yield 'Matcha'
#     yield 'Oolong'

# def full_menu():
#     yield from local_chai()
#     yield from imported_chai()

# for chai in full_menu():
#     print(chai)


# def chai_stall():
#     try:
#         while True:
#             order = yield 'Waiting for chai order'
#     except:
#         print('Stall Closed, No more chai')

# stall = chai_stall()
# print(next(stall))
# stall.close()


def chai_stall():
    # Define a generator function called chai_stall().
    # Because it contains 'yield', calling this function creates a generator.

    try:
        # Start a try block.
        # Python will execute the generator code inside this block.

        while True:
            # Start an infinite loop.
            # The chai stall will continue waiting for orders indefinitely.

            order = yield 'Waiting for chai order'
            # Yield the message 'Waiting for chai order' to whoever is using the generator.
            # Then pause the generator at this point.
            #
            # When the generator is resumed, any value sent using .send()
            # will be stored in the variable 'order'.

    except:
        # If the generator is closed or an exception occurs,
        # execution comes here.

        print('Stall Closed, No more chai')
        # Print a message saying that the chai stall has been closed.


stall = chai_stall()
# Create a generator object called 'stall'.
# The function does NOT start running yet.


print(next(stall))
# Start the generator for the first time.
# It enters the try block and while loop.
# It reaches yield and produces:
# 'Waiting for chai order'
# print() then displays that message.


stall.close()
# Close the generator.
# Python tells the generator to stop.
# This causes the generator to exit the yield point
# and execute the except block.


'''

Let's understand it slowly

The key part is:

order = yield 'Waiting for chai order'

This line is doing two things.

First:

It sends this message outside the generator:

Waiting for chai order
Second:

It pauses the generator.

So think:

chai_stall()
     ↓
Waiting for chai order
     ↓
    PAUSE
3. Creating the generator

You write:

stall = chai_stall()

At this point, nothing inside chai_stall() has executed yet.

The generator has merely been created.

Think of it as:

Create chai stall
       ↓
   NOT STARTED
4. next(stall)

Then:

print(next(stall))

next() starts/resumes the generator.

Python enters:

try:

then:

while True:

then:

order = yield 'Waiting for chai order'

The generator yields:

Waiting for chai order

So next(stall) returns that value.

Then:

print(...)

prints it.

Output:
Waiting for chai order
5. What happens after next(stall)?

This is important.

The generator is now paused here:

order = yield 'Waiting for chai order'
             ↑
          PAUSED

So the state is:

chai_stall
    ↓
while True
    ↓
yield
    ↓
PAUSED ⏸️

It is waiting for something to happen.

6. Now comes .close()

You have:

stall.close()

This tells Python:

"Stop this generator."

Python closes the generator.

Because the generator is currently paused inside the try block, closing it causes a GeneratorExit to be raised at the yield.

Your except: catches that exception:

except:
    print('Stall Closed, No more chai')

Therefore it prints:

Stall Closed, No more chai
7. Complete output

Your program produces:

Waiting for chai order
Stall Closed, No more chai
8. Why do we use while True?

You have:

while True:

Normally this would be an infinite loop.

For example:

while True:
    print("Hello")

would continuously print:

Hello
Hello
Hello
Hello
...

But your generator is different.

You have:

while True:
    order = yield 'Waiting for chai order'

The yield pauses the loop.

So it doesn't continuously run.

It works like:

WAIT
 ↓
yield
 ↓
WAIT
 ↓
resume
 ↓
yield
 ↓
WAIT
9. What happens if we send an order?

You could do:

stall = chai_stall()

print(next(stall))

stall.send('Masala Chai')

The first line:

print(next(stall))

produces:

Waiting for chai order

The generator is paused at:

order = yield 'Waiting for chai order'

Then:

stall.send('Masala Chai')

puts:

Masala Chai

into the yield.

So effectively:

order = 'Masala Chai'

Then the while True continues and reaches the next:

order = yield 'Waiting for chai order'

Again it pauses.

10. Think of it as a real chai stall

Imagine this:

                    CHAI STALL
                       │
                       ↓
              "Waiting for order"
                       │
                       ↓
                    PAUSE
                       │
              Customer orders
                       │
                       ↓
                "Masala Chai"
                       │
                       ↓
                    PAUSE
                       │
              Customer orders
                       │
                       ↓
                 "Ginger Chai"
                       │
                       ↓
                    PAUSE

The generator can keep doing this because of:

while True:

But:

stall.close()

means:

             CHAI STALL
                  ↓
              .close()
                  ↓
             STOP GENERATOR
                  ↓
      "Stall Closed, No more chai"
11. One important correction about except

Your code has:

except:

This catches almost any exception, which is usually too broad in real programs.

For learning, it's okay.

But more specifically, when .close() is called, Python raises:

GeneratorExit

So a clearer version would be:

def chai_stall():
    try:
        while True:
            order = yield 'Waiting for chai order'
    except GeneratorExit:
        print('Stall Closed, No more chai')

Now you're explicitly saying:

"When the generator is closed, handle GeneratorExit."

⭐ The 4 things to remember
next()
next(stall)

Starts/resumes the generator.

yield
yield 'Waiting for chai order'

Produces a value and pauses the generator.

.send()
stall.send('Masala Chai')

Resumes the paused generator and sends a value into yield.

.close()
stall.close()

Stops/closes the generator.

So your generator lifecycle is:

chai_stall()
     ↓
generator created
     ↓
next()
     ↓
yield
     ↓
PAUSE ⏸️
     ↓
send() → resume
     ↓
yield
     ↓
PAUSE ⏸️
     ↓
close()
     ↓
GeneratorExit
     ↓
except
     ↓
Stall Closed
🧠 One sentence to memorize:

next() starts it, yield pauses it, .send() resumes it with a value, and .close() stops it.

'''