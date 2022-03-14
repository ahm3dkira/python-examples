# string[ start : end : step ]

string = "0123456789"


print("-- slice by index --")
print(string[4:1])      # does't work
print(string[1:4])

print("-- slice by neg index --")
print(string[-4:-1])
print(string[-1:-4])    # does't work

print("-- step --")
print(string[::2])

