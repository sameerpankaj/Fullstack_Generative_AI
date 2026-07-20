#Strings
chai_type = 'Ginger Chai'
customer_name = 'Priya'

print(f'Order for {customer_name} : {chai_type} please')

chai_descripttion = 'Aromatic and Bold more'
print(f'First word: {chai_descripttion[0:8]}') #here if we want to print Aromatic, we start from 0 to 8, becaue if we go until 7, it will not count c, so the output will be Aromati
print(f'First word{chai_descripttion [:8]}')#This will have the same output as the previous one [0:8] and[:8] are same



print(f'First word {chai_descripttion[0:7]}')# here we counted from 0 to 7 and in this output c, is not included, so the output will be only Aromati
print(f'every second character; {chai_descripttion[0:8:2]}')# this means until the index 8, it will print every second character, so the output will be aoai

print(f'Last word:{chai_descripttion[12:]}') #this will print all the characters after the from the 12th index

print(f'Last word {chai_descripttion[::-1]}')# output will be 'erom dloB dna citamorA', it will start from the last character in reverse order

label_text = 'Chai Spécial'
encoded_label = label_text.encode('utf-8')
print(f'Non Encoded lable : {label_text}')
print(f'Encoded label: {encoded_label}')
decode_label = encoded_label.decode('utf-8')
print(f'Decoded label {decode_label}')

'''
# Store the type of chai
chai_type = 'Ginger Chai'

# Store the customer's name
customer_name = 'Priya'

# Print the customer's order using an f-string
print(f'Order for {customer_name}: {chai_type} please')

# Store a description of the chai
chai_descripttion = 'Aromatic and Bold more'

# Slice from index 0 up to (but not including) index 8
# Output: Aromatic
print(f'First word: {chai_descripttion[0:8]}')

# Omitting the starting index defaults it to 0
# [:8] is the same as [0:8]
print(f'First word: {chai_descripttion[:8]}')

# Slice from index 0 up to (but not including) index 7
# Output: Aromati (the character at index 7 is not included)
print(f'First word: {chai_descripttion[0:7]}')

# Print every second character from index 0 up to index 8
# Syntax: [start:end:step]
# Output: Aomtc
print(f'Every second character: {chai_descripttion[0:8:2]}')

# Print all characters starting from index 12 to the end of the string
# Output: Bold more
print(f'Last word: {chai_descripttion[12:]}')

# Reverse the entire string using a step of -1
# Syntax: [::-1]
# Output: erom dloB dna citamorA
print(f'Reversed string: {chai_descripttion[::-1]}')

# Store a string containing a Unicode character (é)
label_text = 'Chai Spécial'

# Encode the string into UTF-8 bytes
encoded_label = label_text.encode('utf-8')

# Print the original string
print(f'Non-encoded label: {label_text}')

# Print the encoded bytes
print(f'Encoded label: {encoded_label}')

# Decode the UTF-8 bytes back into a normal string
decode_label = encoded_label.decode('utf-8')

# Print the decoded string
print(f'Decoded label: {decode_label}')

Note: There's one small correction in your original comment:

print(f'Every second character: {chai_descripttion[0:8:2]}')

The output is Aomtc, not aoai.

Here's why:

Aromatic
01234567

Index : 0 1 2 3 4 5 6 7
Chars : A r o m a t i c

Take every 2nd character:
0 -> A
2 -> o
4 -> a
6 -> i

Output: Aoai

Actually, because chai_descripttion is "Aromatic and Bold more" and you're slicing only up to index 8 (exclusive), the slice is "Aromatic" (indices 0–7), and taking every second character gives:

A o a i

So the correct output is Aoai. Your original comment was essentially correct except that the first letter should be uppercase (A) because the original string starts with a capital A.


'''