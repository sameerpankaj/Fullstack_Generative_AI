# Boolean

is_boiling = True
stir_count = 5
total_actions = stir_count + is_boiling # Upcasting
print(f'Total actions: {total_actions}')

milk_present = 0 # no milk
print(f'Is here milk {bool(milk_present)}') 
'''in the output, it will print False, becaue the value provided to milk_present is 0, and 0 means False, this bool in the print sectoin
converts milk_present value to bool '''


lactose_frei_milk_present = 1 #1 bottle of lactosefrei milk
print(f'Is here lactosefrei milk {bool(lactose_frei_milk_present)}')
'''in the output, it will print True, becaue the value provided to lactose_frei_milk_present is 1, and 0 means False, this bool in the print sectoin
converts lactose_frei_milk_present value to bool '''

water_hot = True
tea_added = False

can_serve = water_hot and tea_added
print(f'can serve chai? {can_serve}') #output will be false, becaue tea_added is false and to serve chai, both water_hot and tea_added is needed



