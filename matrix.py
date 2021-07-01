list=[[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]]
i=0
a=[]
while i<=len(list):
    b=[list[0][i],list[1][i],list[2][i]]
    a.append(b)
    i=i+1
print(a)