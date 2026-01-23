todos=[]

def add_todos():
    task=input("Enter a task")
    todos.append({"task":task,"done":False})
    print(f"Task {task} added successfully")

def view_todos():
    if not todos:
        print("Todo not found")
    else:
        for idx,todo in enumerate(todos, start=1):
            status = "Complete" if todo["done"] else "Incomplete"
            print(f"{idx}. {todo['task']} [{status}]")


def delete_todos():
    view_todos()
    if not todos:
        print("Todo not available")
    
    num = int(input("Enter task number to delete: "))

    if 1<=num<=len(todos):
        removed = todos.pop(num - 1)
        print(f"Task deleted: {removed['task']}")
    else:
        print("Invalid number")

def mark_done():
    view_todos()
    if not todos:
        return

    num = int(input("Enter task number to mark done: "))

    if 1 <= num <= len(todos):
        todos[num - 1]["done"] = True
        print("Task marked as done")
    else:
        print("Invalid task number")


def main():
    while True:
        print("Select from choices below \n")
        print("1. Add a task")
        print("2. View Tasks")
        print("3. Delete a Task")
        print("4. Mark as done")
        print("5. Exit")

        choice = int(input("Enter your choice \n"))
        if choice ==1:
            add_todos()
        elif choice ==2:
            view_todos()
        elif choice ==3:
            delete_todos()
        elif choice ==4:
            mark_done()
        elif choice ==5:
            break
        else:
            print("Invalid Choice")

main()