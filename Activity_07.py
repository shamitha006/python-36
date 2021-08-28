num=input("Enter two numbers to be added separated by a space")
nos=num.split()
Sum=0
res=map(lambda x:int(x),nos)
add=list(res)
Sum=sum(add,0)
print("%d + %d = %d"%(add[0],add[1],Sum))
