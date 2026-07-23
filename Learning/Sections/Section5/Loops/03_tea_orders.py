'''
You receive a list of names for chai orders.

The goal is to print out the order queue.

Task:

Use a list of names.

Print: 'Order ready for [name]'


'''

#use of for and in

# Create a list containing the names of customers who placed orders
orders = ['hitesh', 'Aman', 'Becky', 'Carlos']

# Loop through each name in the orders list
for name in orders:

    # Print a message indicating that the order is ready
    # for the current customer
    print(f'Order ready for {name}')


    '''
    
    Explanation
orders = ['hitesh', 'Aman', 'Becky', 'Carlos']
Creates a list named orders.
The list contains four customer names.
for name in orders:
Iterates through each element in the orders list.
During each iteration, the variable name stores one customer's name.
print(f'Order ready for {name}')
Uses an f-string to insert the current customer's name into the message.
How the Loop Works
Iteration	name Value	Output
1	hitesh	Order ready for hitesh
2	Aman	Order ready for Aman
3	Becky	Order ready for Becky
4	Carlos	Order ready for Carlos
Output
Order ready for hitesh
Order ready for Aman
Order ready for Becky
Order ready for Carlos

Key Point: Unlike range(), which generates a sequence of numbers, this for loop iterates directly over the elements of a list. On each iteration, name is assigned the next item in the orders list.
    
    
    '''