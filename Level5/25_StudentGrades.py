### Create a variable to store student grades ###

studens = []
grades = []

### Main Menu Loop ###

while True:
   print("\nStudent Grades Management System")
   print("1. Add Student and Grade")
   print("2. View All Students and Grades")
   print("3.serch Student Grade")
   print("4.modify Student Grade")
   print("5. Delete Student")
   print("6. show Average Grade")
   print("7. Exit")
   choice = input("Enter your choice (1-7): ")
   
   ### Option 1: Add Student and Grade ###

   if choice == '1':
       student_name = input("Enter student name: ")
       grade = float(input("Enter student grade: "))
       studens.append(student_name)
       grades.append(grade)
       print(f"Added {student_name} with grade {grade}.")

   ### Option 2: View All Students and Grades ###

   elif choice == '2':
       print("\nList of Students and Grades:")
       for i in range(len(studens)):
           print(f"{studens[i]}: {grades[i]}")

   ### Option 3: Search Student Grade ###

   elif choice == '3':
       search_name = input("Enter the student name to search: ")
       if search_name in studens:
           index = studens.index(search_name)
           print(f"{search_name}'s grade is {grades[index]}.")
       else:
           print(f"{search_name} not found.")

   ### Option 4: Modify Student Grade ###

   elif choice == '4':
       mod_name = input("Enter the student name to modify: ")
       if mod_name in studens:
           index = studens.index(mod_name)
           new_grade = float(input(f"Enter new grade for {mod_name}: "))
           grades[index] = new_grade
           print(f"{mod_name}'s grade has been updated to {new_grade}.")
       else:
           print(f"{mod_name} not found.")

   ### Option 5: Delete Student ###

   elif choice == '5':
       del_name = input("Enter the student name to delete: ")
       if del_name in studens:
           index = studens.index(del_name)
           studens.pop(index)
           grades.pop(index)
           print(f"{del_name} has been deleted.")
       else:
           print(f"{del_name} not found.")

   ### Option 6: Show Average Grade ###

   elif choice == '6':
       if grades:
           average_grade = sum(grades) / len(grades)
           print(f"The average grade is {average_grade:.2f}.")
       else:
           print("No grades available to calculate average.")

   ### Option 7: Exit ###

   elif choice == '7':
       print("Exiting the Student Grades Management System. Goodbye!")
       break
       