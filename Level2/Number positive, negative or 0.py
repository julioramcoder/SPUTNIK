### First step is to request the number to user ###

Number = int(input("Please enter a number:"))

### Second step is make a conditional to define the number ###

if Number > 0:
    print("The number is positive.")
elif Number < 0:
    print("The number is negative")
else:
    print("The number is cero.")