#We are gonna to ask to the user type  randoms numbers first
numbers= (input("User please, type 10 randoms number separated by commas: "))
# input take the numbers that we input or the user, the problem here is that since now we have 2 string not number, it's the reason that we need to cut 1 string and several string, like this 
Lista = numbers .split (",")
#here we are gonna to become the string in number individuals
number = [ int (julio) for julio in (Lista) ]

#basically dict.fromkeys it's a special notebook with uniq pages where you can write down 1 number each, if it see something wrong just the ignored it
NewList = list(dict.fromkeys(number))

#we can finally print the answers with print 
print("your list of number is: ", number)
print("Your new list is: ", NewList)
