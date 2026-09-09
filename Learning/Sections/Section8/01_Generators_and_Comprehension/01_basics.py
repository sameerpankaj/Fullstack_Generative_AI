#Generators

#the only diffrence between function and generator is how you provide a value
#in functions we use return, but in generators we use yield keyword
def service_chai():
    yield 'Cup 1: Masala Chai'
    yield 'Cup 2: Ginger Chai'
    yield 'Cup 3: Elaichi Chai'

stall = service_chai()

# for cup in stall:
#     print(cup)

#regular function
def get_chai_list():
    return ['Cup1', 'Cup 2', 'Cup 3']


#generator function
def get_chai_gen():
    yield 'Cup 1'
    yield 'Cup 2'
    yield 'Cup 3'

chai = get_chai_gen()
print(next(chai))
print(next(chai))
print(next(chai))
#print(next(chai)) : this gives error


'''

Yes. This is an important Python concept. The easiest way to understand it is:

return gives you the result and ends the function.
yield gives you one result at a time and pauses the function.

1. Normal function with return
def numbers():
    return [1, 2, 3, 4, 5]

result = numbers()

print(result)

Output:

[1, 2, 3, 4, 5]

The function runs and creates the entire list, then return sends it back.

Once it reaches:

return [1, 2, 3, 4, 5]

the function is finished.

2. Generator function with yield

Now:

def numbers():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

If you do:

result = numbers()

print(result)

you don't get a list. You get a generator object.

<generator object numbers at ...>

To get the values:

for number in numbers():
    print(number)

Output:

1
2
3
4
5
3. The biggest difference: yield pauses

Consider:

def numbers():
    print("Start")
    yield 1

    print("Middle")
    yield 2

    print("End")
    yield 3

Now:

gen = numbers()

Nothing inside the function has actually executed yet.

Then:

print(next(gen))

Output:

Start
1

The function pauses at yield 1.

Then:

print(next(gen))

Output:

Middle
2

It continues from where it stopped, reaches yield 2, and pauses again.

Then:

print(next(gen))

Output:

End
3

So you can visualize it like this:

yield 1
   ↓
PAUSE
   ↓
next()
   ↓
yield 2
   ↓
PAUSE
   ↓
next()
   ↓
yield 3
   ↓
PAUSE
4. return vs yield
return
def test():
    return 10
    return 20
    return 30

Only 10 is ever returned.

Once Python sees:

return 10

the function ends.

yield
def test():
    yield 10
    yield 20
    yield 30

You can get:

10
20
30

one at a time.

5. Why do we need generators?

The biggest reason is memory efficiency.

Imagine you need numbers from 1 to 1 billion.

A normal approach might create a huge list:

def numbers():
    return list(range(1, 1_000_000_001))

That requires storing all those numbers in memory.

A generator can do:

def numbers():
    for i in range(1, 1_000_000_001):
        yield i

Now Python produces:

1
2
3
4
...

one value at a time.

It doesn't need to keep the entire result list in memory.

6. A real-world analogy

Think of a restaurant.

return 🍽️

You order:

"Give me all 5 dishes."

The kitchen prepares all 5 and gives them to you:

🍕 🍔 🍟 🌮 🍰

That's similar to:

return [pizza, burger, fries, taco, cake]
yield 🍽️

Instead, the kitchen gives you one dish:

🍕

Then later:

🍔

Then:

🍟

The kitchen doesn't need to prepare everything at once.

That's similar to:

yield pizza
yield burger
yield fries
7. One very important difference

A normal function:

def square_numbers():
    return [1, 4, 9, 16, 25]

When you call:

numbers = square_numbers()

numbers is a list:

[1, 4, 9, 16, 25]

But:

def square_numbers():
    yield 1
    yield 4
    yield 9
    yield 16
    yield 25

Calling:

numbers = square_numbers()

gives you a generator.

You can consume it:

for number in numbers:
    print(number)
8. You can use next()

Generators are iterators, so you can ask for the next value:

def numbers():
    yield 10
    yield 20
    yield 30

gen = numbers()

print(next(gen))
print(next(gen))
print(next(gen))

Output:

10
20
30

If you call:

next(gen)

again, there are no more values, so Python raises:

StopIteration

A for loop handles this automatically.

9. Can a generator use return?

Yes!

def test():
    yield 1
    yield 2
    return

The generator gives:

1
2

and then finishes.

You can also technically do:

def test():
    yield 1
    return "Finished"

The "Finished" becomes the value associated with the final StopIteration, rather than another yielded item.

🧠 The key idea to remember
Normal function
def function():
    return value

Call → calculate → return → function ends

Generator
def generator():
    yield value

Call → create generator → next() → produce value → pause → next() → continue

⭐ A1-level Python analogy

Since you're learning Python, remember this simple sentence:

return = "Here is the answer. I'm finished."

yield = "Here is one answer. I'll continue later."

And the biggest practical reason for yield is:

Generators are useful when you want to process large amounts of data one item at a time without storing everything in memory.

'''