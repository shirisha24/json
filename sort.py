n=int(input("enter num"))
rev=0
i=0
b=[]
while i<n:
    a=n%10
    rev=(rev*10)+a
    n=n//10
    b.append(a)
    b.sort()
print(b)
