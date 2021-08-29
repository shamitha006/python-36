def input_no():
    x=int(input("Enter the number:"))
    return x
def check(x):
    count=0
    for i in range(1,x+1):
        if(x%i==0):
            count+=1
        else:
            continue
    if(count==2):
        print("{0} is a prime number".format(x))
    else:
        print("{0} is not a prime number".format(x))
def main():
    a=input_no()
    check(a)
main()
