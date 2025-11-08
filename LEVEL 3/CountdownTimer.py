#we need to build a countdown timer with while

#always we are goona to ask to our user the origin information like this
OriginNumber = int(input("Can you please type the origin number for the countdown time?: "))
#at the same time, we need to ask the user up to which number they want to the countdown to go
finishNumber= int(input("can you please type the finish number for the countdown time?: "))
while OriginNumber >= -(-finishNumber) : #here we put like this, because python need to know if the user type a negative number o positive number
    print(OriginNumber) #here, just we must print the origin number up to the finish number
    OriginNumber = OriginNumber - 1  #with this we let it the  orden to python about the "range" about the count 