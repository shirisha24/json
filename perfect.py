n=int(input("enter num"))
i=1
sum=0
while i<n:
    if n%i==0:
        sum=sum+i
    i=i+1
if sum==n:
    print(n,"perfect")
else:
    print(n,"not")