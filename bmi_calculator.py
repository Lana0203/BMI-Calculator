# BMI Calculator
name1 = "Kevin"
height_m1 = 2
weight_kg1 = 90

name2 = "David"
height_m2 = 1.85
weight_kg2 = 108

name3 = "Maria"
height_m3 = 1.6
weight_kg3 = 40


def bmi_cal(name, height_m, weight_kg):
    bmi = weight_kg / height_m ** 2
    print("BMI: " + str(round(bmi, 1)))
    if bmi < 18.5:
        return name + " is within the underweight range."
    elif 18.5 < bmi < 25:
        return name + " is within a healthy weight range."
    elif 25 < bmi < 30:
        return name + " is within the overweight range."
    elif bmi > 30:
        return name + " is within the obesity range."


result1 = bmi_cal(name1, height_m1, weight_kg1)
print(str(result1 + "\n"))
result2 = bmi_cal(name2, height_m2, weight_kg2)
print(str(result2 + "\n"))
result3 = bmi_cal(name3, height_m3, weight_kg3)
print(str(result3 + "\n"))
