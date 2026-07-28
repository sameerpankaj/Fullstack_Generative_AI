'''
```
You want to simulate tea heating.
It starts at 40 degree C and boils at 100 degree C
Task:
  Use a while loop.
  Increase temprature by 15 until it reaches or exceeds 100.
  Print each temprature step.

```


'''

# Initial temperature value is set to 40 degrees
temperature = 40

# The while loop will continue running as long as the temperature is less than 100
while temperature < 100:

    # Print the current temperature using an f-string
    print(f'Current temperature: {temperature}')

    # Increase the temperature by 15 degrees after each loop iteration
    # The following line:
    # temperature = temperature + 15
    # is exactly the same as:
    temperature += 15

# This message will be printed after the loop ends
# The loop stops when temperature becomes 100 or higher
print('Tea is ready to boil')


'''

Step-by-step execution:

Starting value:

temperature = 40
Loop 1:
temperature = 40
40 < 100 → True
Print: Current temperature: 40
Increase temperature by 15 → 55
Loop 2:
temperature = 55
55 < 100 → True
Print: Current temperature: 55
Increase temperature by 15 → 70
Loop 3:
temperature = 70
70 < 100 → True
Print: Current temperature: 70
Increase temperature by 15 → 85
Loop 4:
temperature = 85
85 < 100 → True
Print: Current temperature: 85
Increase temperature by 15 → 100
Loop stops:
temperature = 100
100 < 100 → False

Then:

Tea is ready to boil
Final output:
Current temperature: 40
Current temperature: 55
Current temperature: 70
Current temperature: 85
Tea is ready to boil
Important concept:

temperature += 15 is called a compound assignment operator.

These two statements are identical:

temperature = temperature + 15

and

temperature += 15

Python also has similar shortcuts:

x -= 5   # same as x = x - 5
x *= 2   # same as x = x * 2
x /= 3   # same as x = x / 3
'''
