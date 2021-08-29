import math
def input_no():
    x=int(input("Enter the number:"))
    return x
def check_for_prime(x):
    flag=True
    for i in range(2,int(math.sqrt(x))):
        if(x%i==0):
            flag=False
            break
        else:
            continue
    return flag
def result(flag):
    if(flag==True):
        print("It is a prime number")
    else:
        print("It is not a prime number")
def main():
    a=input_no()
    flag=check_for_prime(a)
    result(flag)
main()

