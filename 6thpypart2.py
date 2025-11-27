#ask a user if they would like some food
response = input("would you like food? (Y/N): ")
#if you use one equal sign then it would think "if" is y instead of if "if" equals y
if response == "y":
    print("have some food! ")
elif response == "n":
    print("no food for you! ")
else:
    print("not a valid answer! ")

