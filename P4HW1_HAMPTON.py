# P4HW1
# Stephanie Hampton
# 03/29/2025
# takes grade scores, drop the lowest and then determine letter grade
# psudocode: i also used the psuedocode you provided in p4HW1_Pseudocode.py
'''
'Create an empty list out of loop so it doesn't get rewritten
Num_scores → get input from the user (how many scores to enter)
For score in range(num_score): ##in python
Get one score from user → put in variable and int/float
Grade = int(input(f”Enter score # {score + 1})) ## will fix it so it goes 1-7

## need to not allow a neg or grade higher then 100 into the list
	While Loop - grade is invalid they get trapped into a nested loop
	While grade < 0 OR  grade > 100 ## have to reiterate the variable in the or. 
	Display to user that grade is invalid
	Allow user to re-enter. A valid input would break the while loop
## in loop add grades entered in loop to the empty list

	SCORE = a range of values. Remember starts at zero, and is not inclusive. You have 7 values itll start at 0 - 6 (7 values)

##drop lowest grade
	(min(grades_list)
	Remove min from list
'''

print()
print("-=-=-=-=-")
print()

# asking how many scores you want to enter
num_scores = int(input("How many scores do you want to enter? "))
print()

# empty list
scores_list = []

# asking for the # of scores to inout into the scores_list

for each in range(num_scores):
    score = float(input(f"Enter score #{each+1}: "))
    # see if score hit criteria should be between 0 and 100
    while score < 0 or score > 100:
        print() 
        print("INVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        score = float(input(f"Enter score #{each+1} again: "))
    scores_list.append(score)
    
# print scores_list to ensure correct
# print(f"{scores_list}")


# drop the lowest grade
lowest = min(scores_list)
scores_list.remove(lowest)

# get updated lowest score as well as max/sum/avg
low = min(scores_list)
high = max(scores_list)
total = sum(scores_list)
avg = total/ len(scores_list)

# determine letter grade for average

if avg >= 90:
    grade = 'A'
else:
    if avg >= 80:
        grade = 'B'
    else:
        if avg >= 70:
            grade = 'C'
        else:
            if avg >= 60:
                grade = 'D'
            else:
                grade = 'F'

#Display low grade/high grade/sum/avg

print()
print('------------Results------------')
print(f"{'Lowest Score: ':>16}{lowest:.1f}")
print(f"{'Modified List: ':>16}{scores_list}")
print(f"{'Scores Average: ':>16}{avg:.2f}")
print(f"{'Grade: ':>16}{grade}")

print('-------------------------------')
print()


