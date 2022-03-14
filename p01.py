#  if number is prime print prime else prind bigest number that is divisible by number

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

n = int(input("Enter number: "))
if isPrime(n):
    print("Prime")
else:
    for i in range(n-1, 0, -1):
        if n % i == 0:
            print(i)
            break
