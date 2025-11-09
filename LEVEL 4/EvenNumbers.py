#we need to ask the numbers that the user need to separate
numbers = input("please user, type the x number randoms: ")

#input take the numbers that we input or the user, the problem here is that since now we have 2 string not number, it's the reason that we need to cut 1 string and several string, like this 

lista = numbers.split(",")

#here we are gonna to become the string in number individuals
LIST = [int (julio) for julio in (lista)]

#Here it's the most important part, because we are gonna use something call list comprehension, and it mean for each new item in this case LIST it a conditional will be fulfilled
EvenNumbers = [ n for n in LIST if n%2 == 0]
#and the end just show them the result with the command print 
print(LIST)
print (EvenNumbers)