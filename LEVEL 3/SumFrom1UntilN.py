#Now we are gonna ask to user a number "n" and the code it will make a sum until that number

#it's necesary make a varible call sum, because we need to save all the information about the suma here, and could use after
sum = 0

#ask a number n
n=int(input("please type a number n: "))
for julio in range (1,n+1): #we want to count ecxacly until 12,  we means,  if the user type 12, all the number including the number 12 can be count
    sum = sum + julio #here, alright we have a varible saving a information about the sum, so we need to sum that information with the number inside to the varible julio 
    
result= sum
print( "the sum from 1 until",n,"is", result)

    

