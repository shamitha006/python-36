num=input("Enter two numbers to be added separated by a space")
nos=num.split()
sum=0
add=list()
for i in nos:
    j=int(i)
    add.append(j)
    sum+=j
print("%d + %d = %d"%(add[0],add[1],sum))
