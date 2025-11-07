### Request the student's grade ###
grade = float(input("Enter the student's grade: "))

# Classify the grade
if grade >= 90:
    print("Excellent")
elif 60 <= grade < 90:
    print("Pass")
else:
    print("Fail")