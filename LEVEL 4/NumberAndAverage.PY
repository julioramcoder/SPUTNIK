#We are gonna to ask to the user type  randoms numbers first

list = (input("User please, type 6 randoms number separated by commas: "))

# input take the numbers that we input or the user, the problem here is that since now we have 2 string not number, it's the reason that we need to cut 1 string and several string, like this 

List = list.split (",")

#here we are gonna to become the string in number individuals
number = [ int (julio) for julio in (List) ]
 #here we are getting the avarage, len count the item that we have in the list
average = sum(number)/len(number)

#at the end just ask to the code show us the result with print
print("your list is: ",number)
print("your average is: ",average)

    