# program takes 2 imput from user and swap them

x = input("Enter first number: ")
y = input("Enter second number: ")

print("Before swap: ")
print("x = ", x)
print("y = ", y)

temp = x
x = y
y = temp

print("After swap: ")
print("x = ", x)
print("y = ", y)
