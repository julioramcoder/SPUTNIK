# We are gonna build a multiplication table, we are gonna use the command for, like this

#ask to the user to type a x number
Numberx = int(input("can you please type the number you want to see the multiplication for?: ")) 
#then it's necesary to ask also how many time the user want to multiply the x number
multiplication = int(input("how many time do you want to multiply the numberx?: "))
#like this just we need to use the for command and then with print show the multiplication 
for david in range (1,multiplication+1): #here we add +1 because we want to all the range show it completely 
 print(david*Numberx) 
