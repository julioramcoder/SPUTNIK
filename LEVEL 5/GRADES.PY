#now we are gonna build a system from grade
#first we are gonna ask those guys their name and grade

Student1 = input("Can you please type your name: ")
Gr1 = int(input("Can you please type your grade: "))

Student2 = input("Can you please type your name: ")
Gr2 = int(input("Can you please type your grade: "))

Student3 = input("Can you please type your name: ")
Gr3 = int(input("Can you please type your grade: "))

Student4 = input("Can you please type your name: ")
Gr4 = int(input("Can you please type your grade: "))

Student5 = input("Can you please type your name: ")
Gr5 = int(input("Can you please type your grade: "))

Student6 = input("Can you please type your name: ")
Gr6 = int(input("Can you please type your grade: "))

Student7 = input("Can you please type your name: ")
Gr7 = int(input("Can you please type your grade: "))

#now we are gonna to fix up those information in a list
GRADES = [Gr1,Gr2,Gr3,Gr4,Gr5,Gr6,Gr7]
STUDENTS = [Student1,Student2,Student3,Student4,Student5,Student6,Student7]

#we can star ask to the user type the level of the grade
excelent = " greater than or equal to 8"
approved = " greater than or equal to 6"
failed = " less than or equal to 5"


#now with the commands for, if, elif and else, we define the grading ranges

for julio in range (len(GRADES)): #Basically len read all the items into the list and returns them.
    grade = GRADES[julio] #Julio is the iterator function that iterates through the values ​​and returns them
    student = STUDENTS[julio]# so since that is already defined, we have to make it clear to Python that Julio will iterate through the values ​​of grade and name at the same time
#at the end we can ask to code to show us what happen, using if, elif and else and print the results
    if grade>=8:
        print("your grade it's EXCELENT .Congratulation",student,":)")
    elif grade>=6:
        print("your grade it's good",student,"congratulation you were approved")
    else:
        print(" you are FILED",student,".I guess you must to study more hard the next year, i'm sorry :(")