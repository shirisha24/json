num1=int(input("enter num"))
num2=int(input("enter num"))
num3=int(input("enter num"))
if num1<num2<num3:
    print("num2 is max")
elif num2<num3<num1:
    print("num3 is max")
elif num3<num1<num2:
    print("num1 is max")