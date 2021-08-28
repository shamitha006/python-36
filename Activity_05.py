s=input("Enter 5 numbers separated by spaces")
nos=list()
num=list()
Sum=0
nos=s.split(" ")
for i in nos:
    j=int(i)
    num.append(j)
Sum=sum(num,0)
print("Sum of all the numbers is =",Sum)
