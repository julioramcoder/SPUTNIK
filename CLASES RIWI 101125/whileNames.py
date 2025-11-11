names = []
name = ""
while name != "":
    name= input("PLEASE TYPE YOUR NAME: ").lower()
    if names > 10:
        break
    names.append (name)
print (names)
    
    