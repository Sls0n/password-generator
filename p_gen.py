import secrets
from time import sleep

# Default Value
Lstrings = "abcdefghijklmnopqrstuvwxyz"

# Starting
print("Welcome to the password generator.")
sleep(1)
print("Reply with Y/N for the following queries.\n")
sleep(1)

# Confirmation

# Normal Symbols
n_symbols_i = input('Include normal symbols? i.e !@#$%   :    ').lower()

if "y" in n_symbols_i:
    n_symbols = "!@#$%"
elif "n" in n_symbols_i:
    n_symbols = "s"

# Ambiguous Symbols
a_symbols_i = input('Include ambiguous symbols? i.e ^&*()_+=-{[}]?/.,.<>   :    ').lower()

if "y" in a_symbols_i:
    a_symbols = "^&*()_+=-{[}]?/.,.<>"
elif "n" in a_symbols_i:
    a_symbols = "s"

# Numbers
numbers_i = input('Include Numbers? i.e 012345  :    ').lower()

if "y" in numbers_i:
    numbers = "0123456789"
elif "n" in numbers_i:
    numbers = "s"

# Uppercase Characters
Ustrings_i = input('Include uppercase characters? i.e ABCDEF  :    ').lower()

if "y" in Ustrings_i:
    Ustrings = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
elif "n" in Ustrings_i:
    Ustrings = "s"

# Password length
sleep(1)
print ('\nProvide input in number/integer. This will be your length of password/key. eg: > 12')
pass_length = int(input('Password Length : '))
if pass_length < 12:
    print("Error! To make your password more secure, please type number more than 12.")
    pass_length = int(input('Password Length : '))


# Main
combined_strings = Ustrings + Lstrings + numbers
combined_symbols = a_symbols + n_symbols + n_symbols
password = ''.join(secrets.choice(combined_strings + combined_symbols) for i in range(pass_length))


sleep(1)
print(f"Here's your password : " + str(password))
