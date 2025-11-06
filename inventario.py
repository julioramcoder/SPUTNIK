# Step 1; the firs that we need to do it's call the variables to get a good uderstanding about the code 
#variables 
name = "string"  
price = "float"
quantity = "int"

#List of products that we have at inventory yet
products = ["soap", "salt", "honey"]

#It's necesary let it clair how many time the system it going to ask him the user type a name of product in this specific case with the variable

attempts=0

#Now the user need to knows if he has x product in his invetory using the command while and attempts. the loop just repeat 4 times 
while attempts < 4:
    name_of_products = input("plese type the name of the product: ")

    if name_of_products in products:
        print("still you have this product in invenrory: ")
    else:
        print("it's necessary to buy and making a inventory.\n")
        break #with this command we just puting one stop the loop when there is not the product 
    attempts +=1  

#Because we had not more than 3 products in our stock is necesary to buy more products and making is inventory
#Just we need to ask the next


print("plase type the next necesary information.\n")
   
name = input("Prodcut name: ") 

#Because we cannot to allow it either in quantity or price type something diferenct to a numerber
#With the next code "imput" we can ask to our customer type the information about the new product
while True:
    try:
        quantity = int(input("Quantity: ")) #It's necesary put the command "int" because we are talking about a number
        if quantity > 0: 
            break #if the valor it's correct you can get out from the loop
        else:
            print("Please just type a positive number ")
    except: 
        print("incorrect information:  please type a number") 
#Here we are gonna do the next; basically we have to saying "code don't worry it's not necesary to you break, try to do this, and if you get a problem, you have this other opcion"
#And we used try and except
while True: 
    try:             
        price = float(input("Price: "))
        if price > 0:
          break #if the valor it's correct you can get out from the loop
        else: 
             print("Please just type a correct information ") 
    except: 
        print("incorrect information:  please type a number") 
        
code = input("Inventory code: ")
description = input("Description: ")
supplier = input("Supplier: ") 

#Now it's necesary also to save this information, for that we are gonna crear a dictionary 
New_product = {
    "name": name, 
    "quantity": quantity, 
    "price": price,
    "code": code,
    "description": description,
    "supplier": supplier, 
}
#Now we can watch our save informatio 
print("\n Products added successfully\n")
print("Hello julio, Here is your product information: \n")
"print(New_product)"

#The next information we can see the most important for our customer, because he could to see the name of product, price per unit, quantity, subtotal, taxes and finally the total price
"print(price*quantity)"

print("Name of product: ", name) #The command "print" it work to show us in our screen important information 
print("Price per unit :",price,"Colombian Pesos")
print("Quantity: ", quantity,)
print("--------------------------------------------")
print("The subtotal is: ", (price*quantity))
print("The taxes are included in the next price, and are of: ", (price*quantity)*.19 )
print("THE TOTAL IS: ", (price*quantity)+((price*quantity)*.19), "Colombian pesos")
print("\nNowaday we have finished, if you need something more, i am here for you, good bye")

#The last code allow us to knows if: first we have yet stock from wherever stuff, also if the customer doesn't have stock the next
#it's the code it gonna ask him to customer all the necesary information to making inventory
#Finally the code it's gonna give him to customer a list with all information including the total price 
