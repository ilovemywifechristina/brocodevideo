#python weight converter
weight = float(input("enter your weight here: "))
unit = input("kilos or pounds? (K or L): ")

if unit == "K":
    weight = weight * 2.205
    unit = "lbs"
    print(f"your weight is: {round(weight, 1)} {unit}")
elif unit == "L":
    weight = weight / 2.205
    unit = "kgs"
    print(f"your weight is: {round(weight, 1)} {unit}")
else:
    print(f"{unit} was not valid")
