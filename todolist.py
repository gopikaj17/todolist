tasks = {}

def display_menu():
    print("\nTask Manager")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark as Completed")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    description = input("Enter a new task: ")
    tasks[len(tasks) + 1] = {"description": description, "completed": False}
    print("Task added successfully!")

def view_tasks():
    print("\nTasks:")
    for task_number, task in tasks.items():
        status = "Done" if task["completed"] else "Not done"
        print(f"{task_number}. {task['description']} - Status: {status}")
    input("Press enter to continue...")

def mark_task_as_completed():
    view_tasks()
    task_number = int(input("Enter the task number to mark as completed: "))
    if task_number in tasks:
        tasks[task_number]["completed"] = True
        print("Task marked as completed!")
    else:
        print("Invalid task number.")

def delete_selected_task():
    view_tasks()
    task_number = int(input("Enter the task number to delete: "))
    if task_number in tasks:
        del tasks[task_number]
        print("Task deleted successfully!")
    else:
        print("Invalid task number.")

def run():
    while True:
        display_menu()
        user_choice = input("Enter your choice (1/2/3/4/5): ")

        if user_choice == '1':
            add_task()
        elif user_choice == '2':
            view_tasks()
        elif user_choice == '3':
            mark_task_as_completed()
        elif user_choice == '4':
            delete_selected_task()
        elif user_choice == '5':
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    run()
