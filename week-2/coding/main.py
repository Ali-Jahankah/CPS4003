# BMI Calculator

weight = float(input('\n Please enter your weight in kilograms: '))
height = float(input('\n Please enter your height in meter: '))
bmi = weight / height ** 2

print(f'Your BMI is {bmi: .2f}')

if bmi<18.5:
    print("Your BMI category is: Underweight")
elif bmi<=24.9:
    print("Your BMI category is: Healthy")
elif bmi <= 29.9:
    print('print("Your BMI category is: Overwieght")')
else:
        print('print("Your BMI category is: Obese")')

#============================================== Learn  loops in Python =================================
count = 0
target = 10

while count < target:
    count +=1
    print(f"count is: {count}")

for index in range(1,11,1):
    print(index)
    
