tasks = []

while True:
    print("+++welcome to tasker+++")
    print("choose your option")
    print("1.add tasks")
    print("2.delete tasks")
    print("3.view tasks")
    answer = int(input("enter your choice 1-3::"))

    if answer == 1:
        goal = input("enter your task:")
        tasks.append(goal)
        print(tasks)
    elif answer == 2:
        wipe = int(input("which no of task you want to delete:"))
        tasks.pop(wipe)
        print(tasks)
    elif answer == 3:
        print("========currently avalible task right now=======")
        if not tasks:
            print("no tasks avalible")
        else:
            print("your tasks here:")
            for index,tasks in enumerate (tasks):
                print(f"{index} : {tasks}")
                print("__________________________________")
