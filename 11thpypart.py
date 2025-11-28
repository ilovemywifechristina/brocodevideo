#conditional expressions = a one line shortcut for the if-else statement (aka the ternary operator)
# print or assign one of two values based on a condition
# this is the formula (x if condition else y)

#check to see if it is pos or negative

#num = -5

#print("positive" if num > 0 else print("negative"))

#check to see if its even or odd

#num = 4
#if num % 2 means if the number is divisable by 2
#result = "EVEN" if num % 2 == 0 else "ODD"
#print(result)

#a = -1
#b =7

#max_num = a if a > b else b
#min_num = a if a < b else b
#print(max_num)

#age = 7
#status = "adult" if age > 18 else "kid"
#print (status)
#temp = 10
#weather = "hot" if temp > 20 else "cold"
#print (weather)
user_role = "admin"
access_level = "full access" if user_role == "admin" else "limited access"
print(access_level)