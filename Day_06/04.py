name = input("Enter student name: ")
marks = int(input("Enter marks: "))
students={}

def add_student(name,marks):
    students[name]=marks
    print("Student Added Successfully \n")
    return students

print(add_student(name,marks))