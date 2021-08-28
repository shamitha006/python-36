s=input("Enter 5 numbers separated by spaces")
nos=list()
Sum=0
nos=s.split(" ")
for i in nos:
    Sum+=int(i)
print("Sum of all the numbers is =",Sum)
