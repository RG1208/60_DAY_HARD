todos=[]

def add_todo():
    task= input("Enter the task: ")
    todos.append({"task":task,"done":False })
    print("Todo Added Successfully")

def view_todo():
    for idx,todo in enumerate(todos, start=1):
        status = "Complete" if todo["done"] else "Incomplete"
        print(f"{idx}. {todo["task"]}, [{status}]")

def delete_todo():
    view_todo()

    if not todos:
        print("Todo not available")

    number = int(input("Enter the task you want to delete: "))

    if 1<= number <= len(todos):
        removed = todos.pop(number-1)
        print(f"Task removed {removed}")
    else:
        print("Invalid Choice")

def mark_done():
    if not todos:
        print("Todos not available")
    
    number = int(input("Enter the task number you want to mark as done: "))

    if 1<= number <= len(todos):
        todos[number-1]["done"] = True
        print("Marked as Done")
    else:
        print("Invalid Choice")



def main():
    while True:

        print("Enter the choice you want to select")
        print("1. Add a Task")
        print("2. View All Todo")
        print("3. Delete a Todo")
        print("4. Mark as Done")
        print("5. Exit")

        choice = int(input("Enter the choice \n"))

        if choice == 1:
            add_todo()
            print(f"Task Added")

        elif choice == 2:
            view_todo()

        elif choice == 3:
            delete_todo()
            print("Todo Deleted")

        elif choice == 4:
            mark_done()

        elif choice == 5:
            break

        else:
            print("Inavalid choice")
            
main()