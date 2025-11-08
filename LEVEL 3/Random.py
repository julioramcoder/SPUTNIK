# we are gonna to play, we are trying to find a secret number 
#It's necesary to importar (random) that way we are gonna to can show diferent numbers between whever couple numbers add for the user

import random

#ask to the user type 2 radom number
num1=int(input("please type your first number: "))
num2=int(input("please type your second number: "))

#with this command python will show each time a diferent number
randomnumber = random.randint(num1,num2)
#and the end using print, we show it them users 
print(randomnumber)
