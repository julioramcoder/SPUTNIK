#We are gonna build a loop 

#We need to make a sum, so ask 2 numbers the user using input 
num1=int(input("Can you please type first number: "))
num2=int(input("Can you please type second number: "))

#whit the command while we make the next condition
while num1 !=0 and num2 != 0: #while num1 and num2 are diferent to cero it should print the result and again ask 2 number
    print("your result guys is",num1+num2)
    num1=int(input("Can you please type first number: ")) 
    num2=int(input("Can you please type second number: "))
#but if the user type a cero, the program it will closed using the command print 
print("ERROR, did you type 0, the program closed")
