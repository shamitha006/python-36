num=input("Enter two numbers to be added separated by a space")
nos=num.split()
Sum=0
add=list()
for i in nos:
    j=int(i)
    add.append(j)
Sum=sum(add,0)
print("%d + %d = %d"%(add[0],add[1],Sum))
