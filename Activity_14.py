import math
def input_no():
    x=int(input("Enter the number:"))
    return x
def check(x):
    flag=1
    for i in range(2,int(math.sqrt(x))):
        if(x%i==0):
            flag=0
            break
        else:
            continue
    return flag
def output(flag):
    if(flag==1):
        print("It is a prime number")
    else:
        print("It is not a prime number")
def main():
    a=input_no()
    flag=check(a)
    output(flag)
main()
