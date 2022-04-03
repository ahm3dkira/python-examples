# get 3 number as input from user and print the numbers, the sum and the average, the biggest

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))

print("The numbers are:", num1, num2, num3)
print("The sum is:", num1 + num2 + num3)
print("The average is:", (num1 + num2 + num3) / 3)
print("The biggest number is:", max(num1, num2, num3))
