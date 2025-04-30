# P3HW1 DEBUG
# Stephanie Hampton
# 03/10/2025
# debug program for grades.
# This program takes a number grade , determines average and displays letter grade for average.

print()
print("-=-=-=-=-")
print()

# Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
# TO DO: determine lowest, highest , sum and average for grades

low = min(grades)
high = max(grades)
total = sum(grades)
avg = total/ len(grades)

#Display low grade/high grade/sum/avg
print()
print('------------Results------------')
print(f"{'Lowest Grade: ':>18}{'':<5}{min(grades)}")
print(f"{'Highest Grade: ':>18}{'':<5}{max(grades)}")
print(f"{'Sum of Grades: ':>18}{'':<5}{sum(grades):.1f}")
print(f"{'Average: ':>18}{'':<5}{avg:.1f}")

print('-------------------------------')
print()

# determine letter grade for average

if avg >= 90:
    print(f"{'Your grade is A.'}")
else:
    if avg >= 80:
        print(f"{'Your grade is B.'}")
    else:
        if avg >= 70:
            print(f"{'Your grade is C.'}")
        else:
            if avg >= 60:
                print(f"{'Your grade is D.'}")
            else:
                print(f"{'Your grade is F.'}") 

print()




