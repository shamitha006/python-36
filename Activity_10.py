def main():
    a,b=input_numbers()
    summation=add(a,b)
    display(a,b,summation)
def input_numbers():
    a,b=input("Enter the numbers").split()
    a,b=[int(a),int(b)]
    return a,b
def add(x,y):
    summation=x+y
    return summation
def display(x,y,sum):
    print("The sum of {0} and {1} is {2}".format(x,y,sum))

main()
