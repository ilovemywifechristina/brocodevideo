#exercise
#validate user input
#1. username cant be more than 12 characters long
#2. username cant have spaces
#3. username cant have any numbers

username = input ("enter a username: ")

if len(username) > 12:
    print("your username cant be more than 12 characters")

elif not username.find(" ") == -1:
    print ("your username cant contain spaces")

elif not username.isalpha():
    print("your username cant contain digits")

else:
    print(f"welcome {username}")