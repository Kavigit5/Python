#reading input from keyboard

name = input("Enter User Name")
age = int(input("Enter age"))
new_age = 100 - age
new_year = (2014-age)+100

print("you will turn 100 in the year " + str(new_year))

num = input("Enter any number")
i = 1
while i <= int(num):
   print(3 * ("You will turn 100 years old in " + str(new_age) + " Years \n"))
   i += 1
