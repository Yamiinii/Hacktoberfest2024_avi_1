tasks = []

def add_task(task):
    tasks.append(task)
    print(f'Task "{task}" added.')

def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f'Task "{task}" removed.')
    else:
        print(f'Task "{task}" not found.')

def view_tasks():
    if tasks:
        print("Your tasks:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
    else:
        print("No tasks available.")

while True:
    print("\nOptions: add, remove, view, exit")
    choice = input("Choose an action: ")

    if choice == "add":
        task = input("Enter the task: ")
        add_task(task)
    elif choice == "remove":
        task = input("Enter the task to remove: ")
        remove_task(task)
    elif choice == "view":
        view_tasks()
    elif choice == "exit":
        break
    else:
        print("Invalid option.")
