num=input("Enter two numbers to be added separated by a space")
nos=num.split()
Sum=0
add=list(map(lambda x:int(x),nos))
Sum=sum(add)
print(f"{add[0]}+{add[1]}={Sum}")
