#now we are gonna be teachers, because we are gonna to grade exams

#we can star ask to the user type the level of the grade

excelent = " greater than or equal to 8"
approved = " greater than or equal to 6"
failed = " less than or equal to 5"

#then it's necesary to ask to the user his grade and his name with the command input: 
grade=int(input("please type your grade: "))
name=input( "Please type your full name: ")

#now with the commands if, elif and else, we define the grading ranges
if (grade>=8):
    print("your grade it's EXCELENT .Congratulation",name,":)")
elif (grade>=6):
    print("your grade it's good",name,"congratulation you were approved")
else:
    print(" you are FILED",name,".I guess you must to study more hard the next year, i'm sorry :(")

