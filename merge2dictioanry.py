# write 2 demos dictioanry 
dict1 = {'a':10, 'b':20, 'c':30}
dict2 = {'d':100, 'e':200, 'f':300}
# merge 2 dicts
dict3 = {**dict1, **dict2}
# merge 2 dicts with other way
dict4 = dict1
for key in dict2:
    dict4[key] = dict2[key]
# merge 2 dicts with other way
dict5 = dict1
dict5.update(dict2)

print(dict3)
print(dict4)
print(dict5)

