# replace last el in tuple with new value (100)
list1 = [(10,20,40),(40,50,60),(70,80,90)]
list2 = []
print(list1)
for x in list1:
    listx = list(x)
    listx[2] = 100
    list2.append(tuple(listx))
print(list2)
