bmr= 0
tdee = 0
Gender = str(input("Are you Male or Female? "))
age = int(input("How old are you? "))
height_in_feet = int(input("How tall are you in feet?  " ))
height_in_inches = int(input("How tall are you in inches?  "))
weight = int(input("How much do you weigh in pounds? "))

cm =(height_in_feet * 30.48) + (height_in_inches * 2.54)
kg = weight * 0.453592


if Gender == "Male": 
    bmr = (10 * kg) + (6.25 * cm) - (5 * age) + 5 
else: 
    BMR = (10 * kg) + (6.25 * cm) - (5 * age) - 161 

print('----------------------------------')
print("Your Base Metabolic rate is ", + bmr)
print('----------------------------------')
print()
print('----------------------------------')
print('ACTIVITY LEVEL')
print('----------------------------------')
activity_level = {1 : 'Sedentary (little to no exercise + work a desk job) ',
                  2 :'Lightly Active : (light exercise 1-3 days / week)' ,
                  3: 'Moderately Active : (moderate exercise 3-5 days / week)',
                  4: 'Very Active : (heavy exercise 6-7 days / week)',
                  5: 'Extremely Active: (very heavy exercise, hard labor job, training 2x / day)'}

for i in activity_level:
    print(i, ':', activity_level[i])
print()
choice = int(input("Enter the correspinding number for the activity level that defines you most: "))
print()

while not 1 <= choice <= 5:
    print('----------------------------------')
    print('ACTIVITY LEVEL')
    print('----------------------------------')
    for i in activity_level:
        print(i, ':', activity_level[i])
    print()
    choice = int(input("Enter the correspinding number for the activity level that defines you most: "))

if choice == 1: 
    tdee = bmr * 1.2
elif choice == 2: 
     tdee = bmr * 1.375
elif choice == 3:
     tdee = bmr * 1.55
elif choice == 4:
     tdee = bmr * 1.725
elif choice == 5: 
     tdee = bmr * 1.9

print()
print('----------------------------------')
print("Your Total Daily Energy Expenditure is ", + tdee)