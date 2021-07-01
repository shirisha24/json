n=int(input("enter num"))
n1=int(input("enter num"))
n2=int(input("enter num"))
if n>n1 and n2<n:
    print("n is max")
elif n1>n2 and n<n1:
    print("n1 is max")
elif n2>n and n1<n2:
    print("n2 is max")
else:
    pass