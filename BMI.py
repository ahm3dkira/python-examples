def BMI(kg, m):
    bmi = kg/(m*m)
    # print(bmi)
    if bmi < 0:
        return "Invalid"
    elif bmi <= 18.4:
        return "You are underweight"
    elif bmi <= 24.9:
        return "You are healthy"
    elif bmi <= 29.9:
        return "You are overweight"
    elif bmi <= 34.9:
        return "You are severely overweight"
    elif bmi <= 39.9:
        return "You are obese"
    else:
        return "You are severely obese"

kg = float(input("Enter your weight in kg: "))
m = float(input("Enter your height in m: "))

print(BMI(kg, m))
