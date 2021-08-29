import math
def getdata():
    l,b,h=input("Enter the length, breadth and height").split(" ")
    l,b,h=[float(l),float(b),float(h)]
    return l,b,h
def calculate(l,b,h): 
    k=(l**2)+(b**2)+(h**2)
    vol=((b**2)*(h**2))/(k**(1/2))
    r=((3*vol)/(4*math.pi))**(1/3)
    return vol,r
def output(vol,r):
    print("{0:.3f}".format(vol))
    print("{0:.3f}".format(r))
def main():
    l,b,h=getdata()
    vol,r=calculate(l,b,h)
    output(vol,r)
main()
