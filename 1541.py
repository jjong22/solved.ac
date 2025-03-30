import re

expr = input()
new_string = ""

first_sig = 0

for char in expr:
    if char == "-":
        if first_sig == 0:
            new_string += char
            new_string += "("
            first_sig = 1
        else:
            new_string += ")"
            new_string += char
            new_string += "("
    else:
        new_string += char
        
if first_sig == 1:
    new_string += ")"
        
new_string = re.sub(r'\b0+', '', new_string)
new_string = re.sub(r'([+-])0+', r'\1', new_string)
print(eval(new_string))
