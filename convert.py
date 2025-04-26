#-------------------------------------------------------
# Convert all the characters in uppercase and lowercase 
# and eliminate duplicate letters from a sequence.
#-------------------------------------------------------

# 1st Method:

sequence = input('enter your word:')

unique_chars = ""
for char in sequence:
    if char not in unique_chars:
        unique_chars += char

uppercase = ""
for char in unique_chars:
    uppercase += char.upper()  

lowercase = ""
for char in unique_chars:
    lowercase += char.lower()  

#-------------------------------------------------------
# Print results
print("Original sequence:", sequence)
print("Unique characters:", unique_chars)
print("Uppercase:", uppercase)
print("Lowercase:", lowercase)

#-------------------------------------------------------
# 2nd Method:
def change_cases(s):
    return str(s).upper(), str(s).lower()


chrars = input('enter your word:')


result = map(change_cases, chrars)


print(set(result))