n=int(input("enter num"))
if n%2==0:
    print(n*100,"even")
else:
    print(n*-1,"odd")

# another model
i=0
a=[]
while i<n:
    n=int(input("enter num"))
    a.append(n)
    if n%2==0:
        print(n*100)
    else:
        print(n*-1)
    i=i+1