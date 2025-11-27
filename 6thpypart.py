#if statements
#ex. a user wants to sign up for a credit card but they have to be 18 or older
#make sure to check code because an elif could overwrite the other if it comes first
age = int(input("enter your age"))

if age >= 100:
    print("you are too old to sign up")
elif age >= 18:
    print("you are now signed up")
elif age < 0:
    print("you havent been born yet")
else:
    print("you must be 18 plus to sign up ")