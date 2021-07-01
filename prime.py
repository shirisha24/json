n=int(input("enter num"))
i=1
c=0
while i<=n:
    if n%2==0:
        i=i+1
    c=c+1
if c==2:
    print("pm")
else:
    print("not pm")