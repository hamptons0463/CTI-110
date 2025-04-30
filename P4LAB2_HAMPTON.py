## Stephanie Hampton
## 03/19/2025
## p4LAB2
## times tables with + Numbahs

## Create the variable to control while loop (which says y/n for whole progam)

run_again = "y"

while run_again != "n":
    # get user input
    user_num = int(input("Enter a number to retrieve the associated table: "))

    if user_num < 0: # neg not supported
        print ("Negative numbers are not supported.")

    else: # user_num is 0 or greater
        for x in range(1,13):
            print (f"{user_num} * {x} = {user_num*x}")

    run_again = input("Would you like to run again? y/n ")

