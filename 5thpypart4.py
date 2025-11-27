#we need the math module
#we are making a circumference calculator, the formula for circumference is 2 times pi times radius
import math

radius = float(input("enter the radius of a circle: "))

circumference = 2 * math.pi * radius

print(f"the circumference is: {circumference}cm.")
print(f"or the circumference rounded is: {round(circumference, 2)}cm.")



