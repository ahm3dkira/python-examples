# recursive fibonacci
def fibo_rec(n):
    if n < 2:
        return n
    else:
        return fibo_rec(n-1) + fibo_rec(n-2)

n = int(input("Enter number: "))
print(fibo_rec(n))
