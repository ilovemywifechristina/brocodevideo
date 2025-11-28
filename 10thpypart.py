#logical operators = Evaluate  multiple conditions (or, and, not)
#or = at least one condition must be true
#and = both conditions must be true
#not = inverts the condition (not false, not True)

#or ex.
#The if statment will be printed only if one or more conditions were true

#temp = 25
#is_raining = True
#if temp > 35 or temp < 0 or is_raining:
#    print("the outdoor event is canceled")
#else:
#    print("the outdoor event is still scheduled")

#and ex.
#both conditions need to be true to print
#temp = 20
#is_sunny = True

#if temp >= 28 and is_sunny:
#    print("it is hot outside")
#    print("it is sunny")
#elif temp<= 0 and is_sunny:
#    print("it is cold outside")
#    print("it is sunny")
#elif 28 > temp > 0 and is_sunny:
#    print("it is warm outside")
#    print("it is sunny")

#not ex.
temp = 10
is_sunny = True
if temp >= 28 and is_sunny:
    print("it is hot outside")
    print("it is sunny")
elif temp <= 0 and is_sunny:
    print("it is cold outside")
    print("it is sunny")
elif 28 > temp > 0 and is_sunny:
    print("it is warm outside")
    print("it is sunny")
elif temp >= 28 and not is_sunny:
    print("it is hot outside")
    print("it is cloudy")
elif temp<= 0 and not is_sunny:
    print("it is cold outside")
    print("it is cloudy")
elif 28 > temp > 0 and not is_sunny:
    print("it is warm outside")
    print("it is cloudy")