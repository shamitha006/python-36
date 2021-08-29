def input_nos():
    a,b,c=input("Enter the numbers to be compared").split()
    a,b,c=[int(a),int(b),int(c)]
    return a,b,c
def res(a,b,c):
    lar=a
    if b>a:
        lar=b
    elif c>a:
        lar=c
    else:
        lar=a
    return lar
def main():
    x,y,z=input_nos()
    lar=res(x,y,z)
    print("{0} is the greatest number among {1},{2} and {3}".format(lar,x,y,z))
main()
