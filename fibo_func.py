x = int(input("Enter a number: "))

t1 = 0
t2 = 1
t3 = 0
if x <= 1:
    print(x)
else:
    for i in range(x):
        print(t3)
        t3 = t1 + t2
        t1 = t2
        t2 = t3
