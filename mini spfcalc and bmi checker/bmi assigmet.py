
def adultBMI():
    weight = float(input('WEIGHT (e.g 94.0 kg): '))
    height = float(input('HEIGHT (e.g. 1.78 m): '))
    heightSq = height * height
    bmi = round(weight/heightSq)
    if bmi < 18.5:
        print(f'Your BMI is {bmi}, that means you are underweight.')
     elif bmi >= 18.5 and bmi < 25.0:
        print(f'Your BMI is {bmi}, that means your BMI is normal,please keep fit')
     elif bmi > 25.0 and bmi < 30.0:
        print(f' your bmi is {bmi}, that means you are overweight. please reduce your fat intake and keep fit always')
     elif bmi == 30.0:
        print(f' your bmi is {bmi}, Obesity')
def childrenBMI():
    print('Please meet a Pediatrician for your assessment.')

userPIN = '4321'
username = input('NAME: ')
promptUserPIN = input('PIN: ')
userAge = int(input('AGE: '))
if promptUserPIN == userPIN and userAge >= 18:
    print(f'You are welcome, {username}.')
    adultBMI()

elif userAge < 18:
    childrenBMI()
else:
    print('Sorry you cant use this Application.')

