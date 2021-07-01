n=int(input("enter num"))
if n%5==0 and n%11==0:
    print("both")
elif n%5==0:
    print("5")
elif n%11==0:
    print("11")
else:
    print("none")