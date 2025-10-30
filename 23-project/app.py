tasks = []

def displayMenu(): 
    print("=== task manager ===")
    print("1. add tasks")
    print("2. view tasks")
    print("3. complete task")
    print("4. delete task")
    print("0. exit")
    print("=================")

def add_task():
    title = input("enter task titale")
    tasks.append({"title": title,"completed": False})
    print(f"task: {title} added succesfully")

def view_task():
    if not tasks:
        print("no tasks found")
        return
    
    print("== my tasks ==")
    for index,tasks in enumerate(tasks):
        status = "*/" if tasks["completed"] else ""
        print(f"{index + 1}. [{status}] {tasks["title"]}")

def complete_tasks():
    view_task()
    if not tasks:
      return
    
    try:
        task_number = int(input("enter task number to mark as completed:"))
        if task_number < 1 or task_number > len(tasks):
            print("invalid task number")
            return
            tasks_to_completed = tasks[tasks_number - 1]
            tasks_to_completed['completed'] = True
            print(f"Tasks'{tasks_to_completed["title"]} marked as completed")

    except ValueError:
        print("please enter a valid number")

def delete_task():
    view_task()

    if not tasks:
        return
    
    try:
        tasks_number = int(input("enter tasks number to delete task"))
        if tasks_number < 1 or tasks_number > len(tasks):
            print("invalid task number")
            return
    except ValueError:
        print("enter a valid number")

def main():
        while True:
            displayMenu()
            choice = input("enter your choice 1-4")

            if choice == "1":
                add_task()
            elif choice == "2":
                view_task()
            elif choice == "3":
                complete_tasks()
            elif choice == "4":
                delete_task()
            elif choice == "0":
                print("goodbye")
                break
            else:
                print("invalid tasks, please go with 1-4")

main()