num1=int(input("Please type a integer: "))
num2=int(input("Please type a othe integer: "))


operator = input("Please type a mathematical operation symbol: ")

if (operator == '*'):
    print("his result is: ", num1*num2 )
elif (operator == '/'):
    print("his result is: ", num1/num2)
elif (operator == '-'):
    print("his result is: ", num1-num2)
elif (operator == '+'):
    print("his result is: ", num1+num2)
else:
    print("ERROR the symbol typed is not a mathematical operation symbol. Please type again")
    


