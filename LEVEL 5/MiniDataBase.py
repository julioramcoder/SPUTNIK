#we need to ask the user his name and  What type of money withdrawal will it be, Nequi or Bancolombia?, using the command input 
InformationBasic = input("Please type your name:.\n ")
BankBase = input ("What type of money withdrawal will it be, (nequi or bancolombia)?:.\n  ").strip().lower()


#The user chooses Nequi with the while command
while BankBase == 'nequi':
#The int command asks for the account number and the amount to be withdrawn
    NumberAccount = int(input(".\nPlease type your number account: "))
    while NumberAccount <= 0: #We are again setting a condition so that the user cannot enter negative numbers
        print("ERROR, THE THE VALUES TYPED ARE INCORRECT, TYPE AGAIN") #If that's the case, it throws an error and asks again
        NumberAccount = int(input(".\nPlease type your number account: "))
    break  #The break statement is used to give the order that the first conditional statement should only be repeated once
CASH = float(input(".\nPlease "+ InformationBasic + " type how much money do you want withdraw from ATM today?: "))

#Next, we will outline the billing policies and give you the option to choose whether or not to continue
print(".\nDear " , InformationBasic,  " we want to tell you that Because the amount to be withdrawn is so high, the bank will charge 2 percentage of the amount to be withdrawn.\n")
WarningInfo = input("Do you want cotinue with this process? (yes/no): .\n")

#calculations of the amounts to be collected
ChargePercentage = (CASH*2)/100
NewValor = CASH - ChargePercentage

#Here we'll see what happens if the user chooses yes or no regarding the charge
if WarningInfo == 'yes':
    print("Dear",InformationBasic,"This is the percentage for the banck" ,ChargePercentage," Colombian pesos.\n" )
    print("Dear",InformationBasic, "This is the total amount to to withdrawn after the surcharge: ",NewValor,"Colombian Pesos .\n")
else:
    print("We are very sorry",InformationBasic, "but the withdrawal cannot proceed, if you wish, you can contact the bank directly")
print ("Dear",InformationBasic,"Your money is being counted and we'll be handing it over to you shortly, it was a pleasure assisting you today, you'll be able to withdraw your money in just a few seconds.")

"----------------------------------------------------------------------------------------------------------------------------------------------------------------------------"
#Since we give the customer two bank options, we should add a second code, but since it's the same interface, we simply copy the code

while BankBase == 'bancolombia':
#The int command asks for the account number and the amount to be withdrawn
    NumberAccount2 = int(input(".\nPlease type your number account: "))
    while NumberAccount2 <= 0: #We are again setting a condition so that the user cannot enter negative numbers
        print("ERROR, THE THE VALUES TYPED ARE INCORRECT, TYPE AGAIN") #If that's the case, it throws an error and asks again
        NumberAccount2 = int(input(".\nPlease type your number account: "))
CASH2 = float(input(".\nPlease "+ InformationBasic + " type how much money do you want withdraw from ATM today?: "))

#Next, we will outline the billing policies and give you the option to choose whether or not to continue
print(".\nDear " , InformationBasic,  " we want to tell you that Because the amount to be withdrawn is so high, the bank will charge 2 percentage of the amount to be withdrawn.\n")
WarningInfo2 = input("Do you want cotinue with this process? (yes/no): .\n")

#calculations of the amounts to be collected
ChargePercentage2 = (CASH2*2)/100
NewValor2 = CASH2 - ChargePercentage2

#Here we'll see what happens if the user chooses yes or no regarding the charge
if WarningInfo2 == 'yes':
    print("Dear",InformationBasic,"This is the percentage for the banck" ,ChargePercentage2," Colombian pesos.\n" )
    print("Dear",InformationBasic, "This is the total amount to to withdrawn after the surcharge: ",NewValor2,"Colombian Pesos .\n")
else:
    print("We are very sorry",InformationBasic, "but the withdrawal cannot proceed, if you wish, you can contact the bank directly")
print ("Dear",InformationBasic,"Your money is being counted and we'll be handing it over to you shortly, it was a pleasure assisting you today, you'll be able to withdraw your money in just a few seconds.")

