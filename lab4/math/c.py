import math

n = int(input("Input number of sides: "))
a = int(input("Input the length of a side: "))

perimeter = n * a
apothem = a / (2 * math.tan(math.pi / n))
s = (perimeter * apothem) / 2

print("The area of the polygon is:", int(s))