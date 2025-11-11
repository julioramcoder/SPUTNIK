def evenorodd ():
    while True: 
        num1 = int(input("please type your first numer: "))
        num2 = int(input("Please typer your second numer: "))
        
        if num1 % 2 == 0:
            print (num1, "it's a even number")
        else:
            print (num2,"it's a odd number" )     
        
        if num2 % 2 ==0:
            print (num2,"it's a even number")
        else:
            print(num1, "it's a odd number")
        
evenorodd ()