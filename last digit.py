n=int(input("enter num"))
if n%10==5:
    print(5,"last is present")
else:
    print(5,"not present")


# another model last
n=int(input("enter num"))
a=n
while n>0:
    b=a%10
    n=n//10
if b==7:
    print("last is present")
else:
    print("no")

# middle is present

n=int(input("enter num"))
a=n
while n>0:
    b=a//10
    c=b%10
    n=n//10
if c==3:
    print(c,"middle is present")

else:
    print("no")

