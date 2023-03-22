# Take the list below adn write a program that prints out
# all the elements of the list that are less than 5.
#
# Extras
# 1. Instead of printing the elements one by one, make a new
# list that has all the elements less than 5 from this list in it
# and print out this new list.
# 2. Write this in one line of python
# 3. Ask the user for a number and return a list that contains only
# elements from the original list that are smaller than the number
# given by the user.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for i in a:
    if i < 5:
        print(i)

# Extra 1
b = []
for i in a:
    if i < 5:
        b.append(i)
print(b)

# Extra 2
#TODO

# Extra 3
limit = int(input("Enter a number: "))
c = []
for i in a:
    if i < limit:
        c.append(i)
print(c)
