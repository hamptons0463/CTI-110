# Stephanie Hampton
# 02/17/2024
# P2LAB1
# Homework

##Variables
##radius/PI/diameter/circumfrance/area

##imports math for pi
import math 

radius=float(input("What is the radius of the circle? "))
diameter= 2*radius
circumference= 2*math.pi*radius
area= math.pi*radius**2

#cosmetic spacing
print()

print(f"The diameter of the cicle is {diameter:.1f}")
print()
print(f"The circumference of the circle is {circumference:.2f}")
print()
print(f"The area of the circle is {area:.3f}")
print()