#in this case we aro gonna make to code to compare numbers and show what is greater and less

#ask to the user type 5 numbers, and the code it will classify the numbers
#using the command input
num1=int(input("please type a number: "))
num2=int(input("please type a number: "))
num3=int(input("please type  a number: "))
num4=int(input("please type a number: "))
num5=int(input("please type  a number: "))

#we need a begging point
less= num1
greater = num1

#now we have the numbers, we are gonna classify
# The idea it's like we decied 1 begging poit, we will use that to comparate the next possible numbers
if num2 > greater: 
    greater=num2
if num3 > greater:
     greater=num3
if num4 > greater:
    greater= num4
if num5 > greater:
     greater = num5 
    
#againm we are gonna comparate the next numbers and find the less 

if num2 < less: 
    less = num2
if num3 < greater:
   less= num3 
if num4 < greater:
     less = num4 
if num5 < greater:
    less= num5 
#and the end just we can use a print to print the result 
print("the number more greater is: ", greater)
print("the number more less is: ", less)
