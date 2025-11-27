#calculate the area of a circle
import math

radius = float(input("enter the radius of the circle: "))

area = math.pi * pow(radius, 2)

print(f"the area of the circle is: {round(area, 2)}cm^2")