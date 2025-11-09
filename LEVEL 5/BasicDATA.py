#First, we stipulated the names of each list.
ListOfNames = []

ListOf_Age = []

Listof_SchoolLevel = []

Listof_numbersofcourse = []

ValueOfCredits = 5

#Using the while command, I ask Python to generate a loop with the student's information
while True: 
    Name = input("Welcome student, to continue please type  your full name: ")
    Age = int(input("Also, we need please you type your age: "))
    SchoolLevel = input("Now, please type your level school: ")
    numbersofcourse = int(input("At the end, please type yout number of courses: "))
#And since the information is updatable, then with the append command we can see an updated list
    ListOfNames.append(Name)
    ListOf_Age.append(Age)
    Listof_SchoolLevel.append(SchoolLevel)
    Listof_numbersofcourse.append(numbersofcourse)
#Here we will ask the user if they want to enter more information, and if not, we will use the break command to stop and continue
    again = input(".\n would you like to add other student? (yes or no): ").lower()
    if again != "yes":
        break

#This way we deliver an exact number of credits to the student
Total_ValueOfCredits = ValueOfCredits * sum(Listof_numbersofcourse)

#Finally, with the for command we ask an iterator to enter one of the lists and bring me the lengths or number of spaces in the list
#Then print we print the information within each list
print(".\n INFORMATION FROM OUR STUDENTS" )
for i in range(len(ListOfNames)):
    print('\nName:', ListOfNames[i])
    print('Age:', ListOf_Age[i])
    print('School level:', Listof_SchoolLevel[i])
    print('Number of Courses:', Listof_numbersofcourse[i])
    print('Total Value of Credits:', Total_ValueOfCredits) 
    
    
    