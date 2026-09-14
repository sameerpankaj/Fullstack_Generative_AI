#send generators

# def chai_customer():
#     print('Welcome! What chai would you like?')
#     order = yield
#     while True:
#         print(f'Preparing: {order}')
#         order = yield

# tea_stall = chai_customer()
# next(tea_stall) #starting point of the generator

# tea_stall.send('Masala Chai')

# tea_stall.send('Lemon Chai')

def chai_customer():
    # Define a generator function called chai_customer().
    # Because this function contains 'yield', Python treats it as a generator.

    print('Welcome! What chai would you like?')
    # Display a welcome message when the generator starts running.

    order = yield
    # Pause the generator and wait for a value to be sent using .send().
    # The value received from .send() will be stored in the variable 'order'.

    while True:
        # Start an infinite loop so the generator can continuously accept orders.

        print(f'Preparing: {order}')
        # Display the current chai order.
        # The f-string inserts the value of 'order' into the message.

        order = yield
        # Pause the generator again and wait for the next chai order.
        # The next value sent using .send() will be stored in 'order'.


tea_stall = chai_customer()
# Create a generator object from the chai_customer() generator function.
# The function does NOT start running yet.


next(tea_stall)
# Start/resume the generator for the first time.
# It prints the welcome message and then pauses at 'yield'.


tea_stall.send('Masala Chai')
# Send 'Masala Chai' into the paused yield.
# This value becomes the value of 'order'.
# The generator then prints: Preparing: Masala Chai
# After that, it pauses again at the next 'yield'.


tea_stall.send('Lemon Chai')
# Send 'Lemon Chai' into the next paused yield.
# This value becomes the new value of 'order'.
# The generator then prints: Preparing: Lemon Chai
# After that, it pauses again and waits for another order.


'''
2. Now let's understand the program

Think of the program as a chai shop that stays open and waits for orders.

The basic flow is:

Start shop → wait for order → prepare order → wait → prepare next order → wait...

Step 1: Define the generator
def chai_customer():

This creates a function called chai_customer.

But this isn't an ordinary function because it contains:

yield

Therefore, Python makes it a generator function.

Step 2: Welcome message
print('Welcome! What chai would you like?')

When the generator actually starts running, it prints:

Welcome! What chai would you like?
Step 3: First yield
order = yield

This is the most important line.

yield means:

Pause here and wait for a value.

The generator is now waiting for someone to send it an order.

At this point:

Generator
    ↓
WAITING FOR ORDER
3. Creating the generator
tea_stall = chai_customer()

This creates the generator object.

A very important point:

The function does NOT run yet.

So this line:

tea_stall = chai_customer()

doesn't print:

Welcome! What chai would you like?

It only creates the generator.

You can think of it as:

"Create my chai shop, but don't open it yet."

4. Starting the generator
next(tea_stall)

Now we actually start the generator.

Python enters:

def chai_customer():

Then executes:

print('Welcome! What chai would you like?')

Output:

Welcome! What chai would you like?

Then Python reaches:

order = yield

and pauses.

So now:

Welcome! What chai would you like?

        ↓

     WAITING
5. Sending the first order

Now we execute:

tea_stall.send('Masala Chai')

This sends:

Masala Chai

into the paused yield.

Remember this line:

order = yield

The value sent by .send() becomes order.

So effectively:

order = 'Masala Chai'

Now Python continues running.

6. The while True

The program reaches:

while True:

This means:

Keep doing this forever.

Then:

print(f'Preparing: {order}')

Since:

order = 'Masala Chai'

Python prints:

Preparing: Masala Chai
7. Then it waits again

After printing, we reach:

order = yield

Again, the generator pauses.

So the state is now:

Preparing: Masala Chai

        ↓

     WAITING
8. Sending the second order

Now we execute:

tea_stall.send('Lemon Chai')

The generator was paused at:

order = yield

So:

order = 'Lemon Chai'

Then it continues to:

print(f'Preparing: {order}')

Output:

Preparing: Lemon Chai

Then it reaches:

order = yield

and pauses again.

9. The complete execution

Your program produces:

Welcome! What chai would you like?
Preparing: Masala Chai
Preparing: Lemon Chai

And after that, the generator is still alive and waiting for another order.

For example, you could write:

tea_stall.send('Ginger Chai')

and it would produce:

Preparing: Ginger Chai

Then:

tea_stall.send('Elaichi Chai')

produces:

Preparing: Elaichi Chai
10. The most important concept: yield + .send()

This is the key idea you should remember:

order = yield

means:

Pause here and wait for someone to send me a value.

And:

tea_stall.send('Masala Chai')

means:

Send this value into the paused generator.

So you can think of it like this:

             yield
               ↓
          WAITING...
               ↑
               |
      send("Masala Chai")
               |
               ↓
       order = "Masala Chai"

Then:

Preparing: Masala Chai
               ↓
             yield
               ↓
          WAITING...
               ↑
               |
      send("Lemon Chai")
               |
               ↓
       order = "Lemon Chai"
⭐ One sentence to remember

yield pauses the generator, and .send(value) resumes it by giving a value to that yield.

'''