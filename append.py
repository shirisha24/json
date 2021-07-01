a=["hello","take"]
b=["dear","sir"]
i=0
list1=[]
while i<len(a):
    j=0
    while j<len(b):
        c=a[i]+b[j]
        list1.append(c)
        j=j+1
    i=i+1
print(list1)
        