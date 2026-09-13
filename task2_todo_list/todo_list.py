tasks =[]

def menu():
    print("\n--- To Do List ---")
    print("1. Add task")
    print("2. Show all tasks")
    print("3. Mark task as completed")
    print("4. Delete task")
    print("5. Exit")

def add_task():
    task_text = input("Enter task text: ")
    tasks.append({"task": task_text, "done": False})
    print("Task added.")

def show_tasks():
    if not tasks:
        print("Task list is empty.")
        return
    for index, task in enumerate(tasks):
        status = "Done" if task["done"] else "Not done"
        print(f"{index + 1}. {task['task']} [{status}]")

def complete_task():
    show_tasks()
    if not tasks:
        return
    number = int(input("Enter task number to mark as completed: "))
    if 1 <= number <= len(tasks):
        tasks[number - 1]["done"] = True
        print("Task marked as completed.")
    else:
        print("Invalid task number.")

def delete_task():
    show_tasks()
    if not tasks:
        return
    number = int(input("Enter task number to delete: "))
    if 1 <= number <= len(tasks):
        removed = tasks.pop(number - 1)
        print(f"Deleted: {removed['task']}")
    else:
        print("Invalid task number.")

while True:
    menu()
    choice = input("Choose an option (1-5): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")