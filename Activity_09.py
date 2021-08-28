import math
l=float(input("Enter the length"))
b=float(input("Enter the breadth"))
h=float(input("Enter the height"))
k=(l**2)+(b**2)+(h**2)
vol=((b**2)*(h**2))/(k**(1/2))
print("{0:.3f}".format(vol))
r=((3*vol)/(4*math.pi))**(1/3)
print("{0:.3f}".format(r))
