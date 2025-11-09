#we are gonna build a little car shoping 

#we are gonna to ask the user basic information 

Name = input("Hey, can you please type your name: ")
Adress = input(".\nHey, can you please type your adress: ")

#now we are gonna suppose that the user already bought several stuff
ShopinList = ["adress", "shots","cap,","pillows"]
question = input("Do you want to buy something more? (yes/no) : " ).strip().lower() #We use `lower` to convert all text to lowercase and `strip` to separate it

#We'll leave this value defined for the future.
price_per_item  = 10 

#Now we're going to create a continuity loop because in this part, the customer will be asked if they want to continue the purchase or not.
while question == 'yes': 
        newQuestion = input(".\nwhat more stuff do you want to buy?: ")
        ShopinList.append(newQuestion) #with the command .append we allow to see the new list 
        print(newQuestion, "i was added in your car")
        question = input(".\nDo you want to buy something more?(yes/no): " ).strip().lower()

#If you do not continue, then we will end the shopping     
print(".\nokay" ,Name, "in this moment you should continue with the pay about your products.\n")
print(Name,"you have your list of shoping here:.\n")

#here we are going to show the list of stuff
for item in ShopinList:
    print("-",item) 
    
#To calculate the total purchase value, we first create a new variable and tell it with the len command to go through each of the items in the shopping list and return that information to me in a number
item = len(ShopinList)

#Finally, we have defined values, we multiply the number in the list by the product value and print the result
price_total = (price_per_item * item)
print(".\nhis price to pay it's",price_total,"colombian pesos THANK YOU VERY MUCH, Good bye.")
