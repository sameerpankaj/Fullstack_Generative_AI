#real and floating point numbers#
import sys
from fractions import Fraction
from decimal import Decimal as D

ideal_temp = 95.5 
current_temp = 95.49999999999999
diffrence = ideal_temp - current_temp

print(f'ideal temp {ideal_temp}')
print(f'current temp {current_temp}')
print(f'Differnece temp {diffrence:.14f}')
# print(sys.float_info)