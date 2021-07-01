n=input("enter str")
b=[]
i=0
a=""
while i<len(n):
    if n[i]=="":
        b.append(a)
        a=""
    else:
        a=a+n[i]
    i=i+1
if a:
    b.append(a)
print(b)