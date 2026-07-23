
#online tea store
#Use ternary operators

# Take the order amount from the user and convert it into a floating-point number
order_amount = float(input('Enter the amount in rupees: '))

# Use a ternary operator:
# If the order amount is greater than 300, delivery fee is 0 (free delivery)
# Otherwise, delivery fee is 30 rupees
delivery_fees = 0 if order_amount > 300 else 30

# Display the calculated delivery fee
print(f'Delivery fees is: {delivery_fees}')

# if order_amount > 300:
#     print('Delievery is free')
# else:
#     print('the order amount is not more than 300: Delievery cose is 30 rupees')



