### First step is to request the number to user ###

Number = int(input("Please enter a number:"))

### Second step is make a conditional to define if the name is even or odd###

if Number % 2 == 0:
  
  print(f"{Number} Is even number")
else:
  
  print(f"{Number} Is odd numer")