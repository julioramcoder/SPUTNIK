#in this case we should to ask to the user one integer value
#we are gonna using the imput command for to do it

number=int(input("please type a integer value: "))

#now with the command if, elif, and else. We can get 3 conditions
if number>0:
   print("the number typed is postive")
elif number < 0:
    print("the number typed is negative")
else:
    print("the number typed is cero")