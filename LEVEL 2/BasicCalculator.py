#This case we are gonna identify ths typos from mathematical operation symbol 
#firts we ask to the user 2 number with the command input
num1=int(input("Please type a integer: "))
num2=int(input("Please type a othe integer: "))

#then we need to ask with what mathematical operation symbol the user want to work 
operator = input("Please type a mathematical operation symbol: ")

#with the command if, elif and else 
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
    


