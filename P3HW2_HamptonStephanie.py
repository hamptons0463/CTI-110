### P3HW2
### 03/10/2025
### Stephanie Hampton
### Complicated program about wages

"""
Asks the user to enter name of employee
Ask user to enter number of hours the employee worked this week
Ask user to enter employee's pay rate
Evaluate if employee has worked overtime (more than 40 hours). If yes, calculate the amount owed to employee for overtime hours
The employee should receive 1.5 times their normal pay rate for any overtime hours worked.
Calculate amount employee should be paid for regular hours worked.
Display gross pay (total amount that should be paid to employee)
The program is to display the following (Employee name, pay rate, number of hours worked, overtime hours, overtime pay, pay for regular hours and gross pay).
Once finished, submit the finished code file through the assignment link in this folder.

PsudeoWudo Code:

Variables: 

employee_name
hours_worked
pay_rate
pay_for_hours #total pay for less then 40
overtime_hours 
pay_for_overtime #total pay for overtime worked greater then 40
gross_pay
reg pay

Input

Input String employee_name 
Input Float hours_worked
Input Float pay_rate

Display Employee Name:

in strip
Display hours_worked
Display pay_rate
Display overtime_hours 
Display over_time_pay = ( * 1.5)
Display pay_for_hours = (hours worked * pay_rate)


"""

## get input from user

print()

employee_name = input("Enter employee's name: ")
total_hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

print ("---"*12)

## Math

##overtime is worked
if total_hours_worked > 40:
    overtime_hours = total_hours_worked - 40
    overtime_hourly = pay_rate * 1.5
    overtime_pay = overtime_hours * overtime_hourly
    hourly_pay = pay_rate * 40
    gross_pay = hourly_pay + overtime_pay

    
##no overtime
else:
    overtime_hours = 0
    overtime_hourly = pay_rate * 1.5
    overtime_pay = overtime_hours * overtime_hourly
    hourly_pay = total_hours_worked * pay_rate
    gross_pay = hourly_pay + overtime_pay

## affirming what was typed
## print(f"{'Lowest Grade: ':>18}{"":<5}{min(grades)}")

print (f"{'Employee name:      '}{(employee_name)}")
print ()

print (f"{'Hours Worked':<20}{'Pay Rate':<20}{'OverTime':<20}{'OverTime Pay':<20}{'RegHour Pay':<20}{'Gross Pay':<20}")
print ("---"*40)

#total_hours_worked + pay_rate + overtime_hours + overtime_pay + hourly_pay + gross_pay

print(f"{total_hours_worked:<20.1f}{pay_rate:<20.2f}{overtime_hours:<20.1f}{overtime_pay:<20.2f}${hourly_pay:<20.2f}${gross_pay:<20.2f}")

print()
       


    
    