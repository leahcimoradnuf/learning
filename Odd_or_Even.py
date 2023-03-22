# Ask the user for a number. Depending on whether the number is even or odd, 
# print out an appropriate message to the user.
# 
# Extra 1: also let them know if it's a multiple of 4
# (purpose is to learn modulus)

number = int(input('Hey dumbass, give me a number. Any number! '))
remainder = number % 2

if remainder == 0:
    print('Even.')
    x = number % 4
    if x == 0:
        print("It's also a multiple of 4.")
else:
    print('Odd.')
