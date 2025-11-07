#It's will be very simple the next process
#First we need to ask him to the user one number with the command input, like this:
number=int(input("please type a integer: "))  

#in this case we need to let something clair, we have to make sonething clear:
#the //(MODULO)// must be cero, because python should to know what is our base and origin about the condition 
if (number%2==0):
    print(number, "is a even number")
else:
    print(number, "is a odd number")