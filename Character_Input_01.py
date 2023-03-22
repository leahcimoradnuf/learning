# EXERCISE:
# Create a program that asks the user to enter their name and their age. 
# Print out a message addressed to them that tells them the year that they 
# will turn 100 years old. Note: for this exercise, the expectation is that 
# you explicitly write out the year (and therefore be out of date the next year). 


name = input('Hello, enter your name: ')
print('Hi, ', name,'!')
age = input('How old are you? \n')

def one_hundred(age_now):
    current_year = 2023
    year_100 = 100 - int(age_now) + 2023
    return year_100

print('Did you know that in ', one_hundred(age), 'you will be 100 years old?')
