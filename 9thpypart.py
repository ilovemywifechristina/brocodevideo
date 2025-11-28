unit =  input("Is this temp in celsius or farenheit? C/F: ")
temp = float(input("enter the temp: "))
if unit == "C":
    temp = round((9 * temp) / 5 + 32, 1)
    print (f" the temp in farenheit is: {temp}°F")
elif unit == "F":
  temp = round((temp - 32) * 5 / 9, 1)
  print(f" the temp in celsius is: {temp}°C")
else:
    print(f"unit is an invalid unit of measurement")