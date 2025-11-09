#we are gonna build a little car shoping 

#we are gonna to ask the user basic information 

Name = input("Hey, can you please type your name: ")
Adress = input(".\nHey, can you please type your adress: ")

#now we are gonna suppose that the user already bought several stuff
ShopinList = ["adress", "shots","cap,","pillows"]
question = input("Do you want to buy something more? (yes/no) : " ).strip().lower()

price_per_item  = 10 
    
while question == 'yes': 
        newQuestion = input(".\nwhat more stuff do you want to buy?: ")
        NewShopingList = ShopinList.append(newQuestion)
        print(newQuestion, "i was added in your car")
        question = input(".\nDo you want to buy something more?(yes/no): " ).strip().lower()
print(".\nokay" ,Name, "in this moment you should continue with the pay about your products.\n")
print(Name,"you have your list of shoping here:.\n")
for item in ShopinList:
    print("-",item) 
    
    
item = len(ShopinList)

price_total = (price_per_item * item)
print(".\nhis price to pay it's",price_total,"colombian pesos THANK YOU VERY MUCH, Good bye")
