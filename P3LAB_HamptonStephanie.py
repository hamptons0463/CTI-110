## Name: Stephanie Hampton
## Date: 03/03/2025
## P3LAB
## use if/else statements to determine coin combination

##spacing
print()
print("*-*-*-*-*")
print()

### get a float from user for variable money
input_money = float(input("Enter the amout of money as a float: $"))

### change variable money to a whole number
money = int(input_money * 100)

## verify conversion is right

#print()
#print(f"Total Money as whole #:{money}")
#print()

## DOLLAR BILLS
##calculate number of whole dollars from input
## num dollar= money// dollar value (100)
num_dollars = money // 100

##print variable with programming/testing
#print(f"Num dollars:{num_dollars}")

## update money value to reflect dollars bill removed
## 
money = money - (num_dollars * 100)

#print(f"The remaining money after removing the dollar bills are: {money}")

## QUARTERS
##

##how many Quarters = money/25 cents
num_quarters = money // 25
## money = money - quarters
money = money - (num_quarters * 25)
## remainder
#print(f"Num Quarters: {num_quarters}")
#print(f"The remaining money after removing quarters is: {money}")

## DIMES
##

##how many Dimes = money/10 cents
num_dimes = money // 10
## money = money - dimes
money = money - (num_dimes*10)
## remainder
#print(f"Num Quarters: {num_dimes}")
#print(f"The remaining money after removing dimes is: {money}")

## Nickels
##

##how many Nickels = money/5 cents
num_nickels = money // 5
## money = money - Nickels
money = money - (num_nickels*5)
## remainder
#print(f"Num nickels: {num_nickels}")
#print(f"The remaining money after removing nickels is: {money}")

## Pennies
##
## ease for later
num_pennies = money

#print(f"The remaining pennies is: {money}")

## Display coins/dollars needed only if they re used. 
## Ensure grammer is correct
## Other instances on line 20

print()
print()
print(f"Money Inputed: ${input_money:.2f}")
print()

## if money given requires no change. 
if input_money == 0.00:
    print("No change.")

## if negative is input
if input_money < 0.00:
    print("That was not a valid Number. Please try again later.")

## dolla dolla bills
if num_dollars > 0:
    if num_dollars == 1:
        print(f"{num_dollars} Dollar")
    else:
        print(f"{num_dollars} Dollars")


## quarters
if num_quarters > 0:
    if num_quarters == 1:
        print(f"{num_quarters} Quarter")
    else:
        print(f"{num_quarters} Quarters")

## dimes
if num_dimes > 0:
    if num_dimes == 1:
        print(f"{num_dimes} Dime")
    else:
        print(f"{num_dimes} Dimes")


## quarters
if num_pennies > 0:
    if num_pennies == 1:
        print(f"{num_pennies} Penny")
    else:
        print(f"{num_pennies} Pennies")


### ending spacing
print()
print("*-*-*-*-*")
print()