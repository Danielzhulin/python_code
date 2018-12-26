#!/usr/bin/env python3.7

def gether_info():
    height = float(input("Please input your height?(inches or meters)"))
    weight = float(input("Please input your weight?(pounds or kilograms)"))
    system = input("Are your measurements in metric or imperial systems?").lower().strip()
    return (height, weight, system)

def calculate_bmi(weight, height, system='metric'):
    if system == 'metric':
        bmi = (weight / (height ** 2))
    else:
        bmi = 703*(weight / (height ** 2))
    return bmi

while True:
    height, weight, system = gether_info()
    if system.startswith('i'):
        bmi = calculate_bmi(weight, height, 'imperial')
        print(f"Dear, your BMI is {bmi}")
        break
    elif system.startswith('m'):
        bmi = calculate_bmi(weight, height, 'metric')
        print(f"Dear, your BMI is {bmi}")
        break
    else:
        printf("Error: unknown measurement system, please use: metric or imperial")
