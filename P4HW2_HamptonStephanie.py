### P3HW2
### 03/10/2025
### Stephanie Hampton
### Even more Complicated program about wages

## get input from user

print()

employee_name = str(input("Enter employee's name or 'Done' to terminate: "))
total_employee_entered = int(0)
company_overtime_hours_paid = float(0)
company_reg_hours = float(0)

while employee_name.lower() != "done":
    total_employee_entered = int(total_employee_entered+1)
    total_hours_worked = float(input(f"How many hours did {employee_name} work? "))
    pay_rate = float(input(f"What is {employee_name}'s pay rate? "))

    print()
    print()
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

    print (f"{'Employee name:      '}{(employee_name)}")
    print ()
    print (f"{'Hours Worked':<20}{'Pay Rate':<20}{'OverTime':<20}{'OverTime Pay':<20}{'RegHour Pay':<20}{'Gross Pay':<20}")
    print ("---"*40)
    #total_hours_worked + pay_rate + overtime_hours + overtime_pay + hourly_pay + gross_pay
    print(f"{total_hours_worked:<20.1f}{pay_rate:<20.2f}{overtime_hours:<20.1f}{overtime_pay:<20.2f}${hourly_pay:<20.2f}${gross_pay:<20.2f}")
    print()
    
    company_overtime_hours_paid = company_overtime_hours_paid + overtime_pay
    company_reg_hours = company_reg_hours + hourly_pay

    employee_name = str(input("Enter employee's name or 'Done' to terminate: "))
    print()

#final showing over numbers
print(f"Total number of employee's entered: {total_employee_entered}")
print(f"Total amount paid for overtime: ${company_overtime_hours_paid:<20.2f}")
print(f"Total amount paid for regular hours: ${company_reg_hours:<20.2f}")
print(f"Total amount paid in gross: ${company_overtime_hours_paid + company_reg_hours:<20.2f}")
print()


    
    