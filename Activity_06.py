li=input("Enter 5 numbers separated by spaces")
li=li.split(" ")
l1=map(lambda x:int(x),li)
res=list(li)
s1=res[0:3]
print("Sliced list=",s1)
res[0::4]=[0,0]
s1[0]=0
s1[2]=0
print("Replaced list1=",res)
print("Replaced list2=",s1)
new=res[-2:]
print(new)
