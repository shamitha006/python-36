x=int(input("Enter the start number:"))
y=int(input("Enter the stop number:"))
for i in range(x,y):
    if(i%2!=0):
        print(i,end=", ")
    else:
        continue
