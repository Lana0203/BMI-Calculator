# BMI Calculator with User Input
def bmi_cal(height_m, weight_kg):
    bmi = weight_kg / height_m ** 2
    print("\nBMI: " + str(round(bmi, 1)) + "\n---------")
    if bmi < 18.5:
        return "You are within the underweight range."
    elif 18.5 < bmi < 25:
        return "You are within the healthy weight range."
    elif 25 < bmi < 30:
        return "You are within the overweight range."
    elif bmi > 30:
        return "You are within the obesity range."


try:
    h = float(input('[+] Please enter your height in meters: '))
    w = int(input('[+] Please enter your weight in kilograms: '))
    result = bmi_cal(h, w)
    print(str(result))
except:
    print('[-] Oops! something went wrong. Please enter numbers only. ')
