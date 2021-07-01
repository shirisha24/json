
# list1=["hello","take"]
# list2=["dear","sir"]
# i=0
# j=0
# a=[]
# b=[]
# while i<len(list1):
#     # c=list1[i]+list2[j]
#     # d=list2[i]+list1[j]
#     c=list2[i]+list1[i]
#     d=list1[i]+list2[i]

#     a.append(c)
#     b.append(d)
#     i=i+1
# print(a)
# print(b)

list1=["hello","take"]
list2=["dear","sir"]
i=0
j=0
a=[]
while i<len(list1):
    c=list1[i]+list2[j]+list1[j]+list2[i]
    a.append(c)
    i=i+1
    j=j+1
print(a)









