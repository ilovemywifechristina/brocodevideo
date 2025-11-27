#variable = a container for a value (string, integer, float,  boolean)
#           a variable behaves as if it was the value it contains

#these are strings = these are characters even the numbers when in quotes
wifes_name = "christina"
drink = "dr pepper"
email = "ilovetini@fake.com"
print (wifes_name)
print (f"i love you {wifes_name}")
print (f"you like {drink}")
print(f"your email is: {email}")
print (" ")

#integers = whole numbers
age = 21
quantity = 3
num_of_drpeppers = 999

print (f" you are {age} years old")
print (f" you are buying {quantity} dr peppers")
print (f" your pantry has {num_of_drpeppers} dr peppers")
print (" ")

#floats = decimal numbers
price = 21.21
gpa = 2.1
distance = 21.21

print(f"the price is {price}")
print(f"your gpa is {gpa}")
print(f"you ran {distance} miles")
print(" ")

#boolean = this can only be true or false
is_student = False
for_sale = True
is_online = False

print(f"are you a student?: {is_student}")

if is_student:
    print("you are a student")
else:
    print ("you are not a student")

if for_sale:
    print("that item is for sale")
else:
    print("that item is not available")

if is_online:
    print("you are online")
else:
    print("you are not online")
print(" ")