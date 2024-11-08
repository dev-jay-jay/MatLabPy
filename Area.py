import math

length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))
area = length * width
print("The area of the rectangle is", area, 'sq units')

side = int(input("Enter the side of the square: "))
area = side * side
print("The area of the square is", area, 'sq units')

radius = float(input("Enter the radius of the circle: "))
area = math.pi * radius * radius
print("The area of the circle is", area, 'sq units')
