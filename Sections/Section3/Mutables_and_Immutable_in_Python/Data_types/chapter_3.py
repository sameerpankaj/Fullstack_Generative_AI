# Integer

black_tea_grams = 14
ginger_grams = 3

total_grams = black_tea_grams + ginger_grams
print(f'Total grams of base tea is {total_grams}')

remaining_tea = black_tea_grams - ginger_grams
print(f'Total grams of remaining tea is {remaining_tea}')

milk_litres = 7
servings = 4
milk_per_serving = milk_litres / servings
print(f'Milk per servings is {milk_per_serving}')

total_tea_bags = 7
pots = 4
bags_per_pot = total_tea_bags // pots
print(f'Whole tea bags per pot: {bags_per_pot}')


total_cardamom_pods = 10
pods_per_cup = 3
leftover_pods = total_cardamom_pods % pods_per_cup
print(f'leftover pods for cardamom: {leftover_pods}')

base_flavour_strength = 2
scale_factor = 3
powerful_flavour = base_flavour_strength ** scale_factor
print(f'Scaled floavour strenght {powerful_flavour}')

#Rarely used
total_tea_leaves_harvested = 1_000_000_000 #this is used to improve redability
print(f'tea leaves {total_tea_leaves_harvested}')


'''
# Store the amount of black tea in grams
black_tea_grams = 14

# Store the amount of ginger in grams
ginger_grams = 3

# Add black tea and ginger to get the total weight
total_grams = black_tea_grams + ginger_grams

# Display the total weight
print(f'Total grams of base tea is {total_grams}')

# Subtract ginger from black tea
remaining_tea = black_tea_grams - ginger_grams

# Display the remaining tea amount
print(f'Total grams of remaining tea is {remaining_tea}')

# Store the total amount of milk in litres
milk_litres = 7

# Store the number of servings
servings = 4

# Divide milk equally among all servings
milk_per_serving = milk_litres / servings

# Display the milk per serving
print(f'Milk per servings is {milk_per_serving}')

# Store the total number of tea bags
total_tea_bags = 7

# Store the number of pots
pots = 4

# Use floor division to get the whole number of tea bags per pot
bags_per_pot = total_tea_bags // pots

# Display the whole tea bags per pot
print(f'Whole tea bags per pot: {bags_per_pot}')

# Store the total number of cardamom pods
total_cardamom_pods = 10

# Store the number of pods needed per cup
pods_per_cup = 3

# Use modulus to find the leftover pods
leftover_pods = total_cardamom_pods % pods_per_cup

# Display the leftover pods
print(f'Leftover pods for cardamom: {leftover_pods}')

# Store the base flavour strength
base_flavour_strength = 2

# Store the scaling factor
scale_factor = 3

# Raise the base flavour strength to the given power
powerful_flavour = base_flavour_strength ** scale_factor

# Display the scaled flavour strength
print(f'Scaled flavour strength {powerful_flavour}')

# Store a large number using underscores for better readability
total_tea_leaves_harvested = 1_000_000_000

# Display the total number of tea leaves harvested
print(f'Tea leaves {total_tea_leaves_harvested}')


'''