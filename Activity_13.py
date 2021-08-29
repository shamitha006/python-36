def input_nos():
    x=int(input("Enter the start number:"))
    y=int(input("Enter the stop number:"))
    return x,y
def check(x,y):
    for i in range(x,y):
        if(i%2!=0):
            print(i,end=", ")
        else:
            continue
def main():
    a,b=input_nos()
    check(a,b)
main()
