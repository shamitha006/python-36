import math
def getdata():
    val=input("Enter the length, breadth and height").split(" ")
    val=[float(i) for i in val]
    return val[0],val[1],val[2]
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
