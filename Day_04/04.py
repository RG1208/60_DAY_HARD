students={}

while True:
    print("Enter your choice:")
    print("1. Add a student and marks")
    print("2. View All Students")
    print("3. Update Marks for a particular student")
    print("4. Exit \n")

    choice = int(input("Enter your choice (1,2,3,4): \n"))

    if choice == 1:
        name = input(" \nEnter Student's Name: ")
        marks = input("Enter Marks: ")
        students[name]=marks
        print("Student Added Successfully \n")

    elif choice == 2:
        for name,marks in students.items():
            print(f"\nName: {name}, Marks: {marks}\n")

    elif choice == 3:
        name = input("\n Enter student's name: ") 
        if name in students:
            marks=input("Enter updated marks: ")
            students[name]=marks
            print("Updation Successfull \n")
        else:
            print("\nStudent not found\n")
    
    elif choice == 4:
        print("\nExiting the program\n")
        break

    else:
        print("\nInvalid number\n")







