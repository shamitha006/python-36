s=input("Enter 5 numbers separated by spaces")
nos=list()
Sum=0
nos=s.split(" ")
res=map(lambda x:int(x),nos)
num=list(res)
Sum=sum(num,0)
print("Sum of all the numbers is =",Sum)
