def getstr():
    string=input("Enter the string").split(";")
    return string
def convert(string):
    res=list()
    for i in string:
        t=list()
        new=i.split("=")
        t.append(new[0])
        t.append(new[1])
        tuple(t)
        res.append(t)
    return res
def output(res):
    print(res)
def main():
    string=getstr()
    res=convert(string)
    output(res)
main()

