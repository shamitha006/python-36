s=input("Enter 5 numbers separated by spaces")
nos=list()
sum=0
nos=s.split(" ")
for i in nos:
    i=int(i)
    sum+=i
print("Sum of the numbers is= ",sum)
