#name = input("enter your full name: ")
#length or "len" function = gives us the length of a string or how many characters there is including spaces
#result = len(name)
#print(result)

# "name." gives access to different methods like the find method
#the find method will give the postion of any given characters
#when using the find method, it will give you the space it is in
#in "hello dude", the space or " " is in space 5, the h is space zero, then e is 1, 2, 3, 4, 5. 5 is the space

#this find method will find the first occurence
#name = input("enter your full name: ")
#result = name.find(" ")

#print(result)

#this find method will find the last one
#name = input("enter your full name: ")
#the r in rfind means reverse
#so if i input bro code in this then it will point out the last "o"
#result = name.rfind("o")

#print(result)
#if you look for a character that isnt in the input the output will be a -1

#name = input("enter your full name: ")
#capitalize will make the first letter in a string uppercase
#only the first letter of the first word if there is 2 or more
#name = name.capitalize()

#print(name)

#upper will make all letters in a string uppercase
#name = input("enter your full name: ")
#name = name.upper()
#print(name)

#lower does the opposite of lower
#name = input("enter your full name: ")
#name = name.lower()
#print(name)

#this will result in a boolean or true/false
#true would mean there is digits or numbers, but only digits, if it contains letters and digits then it is false
#name = input("enter your full name: ")
#result = name.isdigit()
#print(result)

#will give true or false, true if a string only has letters, so it will be false if it contains a space or numbers
#name = input("enter your full name: ")
#name = name.isalpha()
#print(name)

#count method just counts how many a certain character is in a string
#phone_number = input("enter your phone #: ")
#result = phone_number.count("-")
#print(result)

#replace method = replace any character with another
phone_number = input("enter your phone #: ")
phone_number = phone_number.replace("-", "")
print(phone_number)