##P1HW1
##Stephanie Hampton
##02/10/2025
##P1HW1
##Using Python's input and print functions, you will create a program that shows output similar to below.

''' '''

##title

print ("-----Calculating Exponents----")

print ("")
print ("")

##defining variables as int (no decimals)

base_value = int(input("Enter an integer as a base value: "))
exponent = int(input("Enter an integer as the exponent: "))

print ("")
print ("")


raised_value = base_value ** exponent

#print statement:
#blank raise to the power of blank is answer !!

print (base_value, "raised to the power of", exponent, "is", raised_value,"!!")

###spacing

print ("")
print ("")

##
##addition/subtraction
##
##allow user to enter a starting integer,
##an integer to add, to subtract, and then display with the verbage
##"num1 + num2 - num3 is equal to num4"
##

#title
print ("-----Addition and Subtraction----")

print ("")
print ("")

#defining variables

num1 = int(input("Enter a starting integer: ")) #num to be modified
num2 = int(input("Enter an integer to add: ")) #num to be added
num3 = int(input("Enter an integar to subtract: ")) #num to be substracted

num4 = num1 + num2 - num3 #answer to equation

#spacing
print ("")
print ("")

#print num4 with verbage
print (num1, "+", num2, "-", num3, "is equal to", num4)