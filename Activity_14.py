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
    return count
def output(count):
    if(count==2):
        print("It is a prime number")
    else:
        print("It is not a prime number")
def main():
    a=input_no()
    count=check(a)
    output(count)
main()
