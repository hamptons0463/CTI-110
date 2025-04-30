
## ## ## ## ## ## ## ##

## Stephanie Hampton
## 02/24/2025
## P2HW2
## Use lists to capture student grades

## ## ## ## ## ## ## ##

print() #cosmetic spacing

## Ask the user for 6 grades
## "Enter grade for module x: "
## number is float

m1Grade = float(input("Enter grade for module 1: "))
m2Grade = float(input("Enter grade for module 2: "))
m3Grade = float(input("Enter grade for module 3: "))
m4Grade = float(input("Enter grade for module 4: "))
m5Grade = float(input("Enter grade for module 5: "))
m6Grade = float(input("Enter grade for module 6: "))

print() ## cosmetic spacing

##Create an empty list, could enter the list variables with []
## [list] {dictionary}

mGrade_list = []

##use the append method to add all grades into the list
## Code looks like this: list,name.append(what to add to the list)
## append() is function, can only append to list tho maybe handy for adding to an existing list

mGrade_list.append(m1Grade)
mGrade_list.append(m2Grade)
mGrade_list.append(m3Grade)
mGrade_list.append(m4Grade)
mGrade_list.append(m5Grade)
mGrade_list.append(m6Grade)

#display results banner
print("------------- Results -------------")
print()

##The lowest grade in the list
#The highest grade in the list
#Sum of grades
##The grades' average

#lowest grade
print(f"{'Lowest Grade:':<20} {min(mGrade_list)}")

#highest grade
print(f"{'Highest Grade:':<20} {max(mGrade_list)}")

#sum of grades
print(f"{'Sum of Grades:':<20} {sum(mGrade_list)}")

#average of grades

mGrade_average = sum(mGrade_list) / len(mGrade_list)

print(f"{'Average:':<20} {mGrade_average:.2f}")

##ending banner
