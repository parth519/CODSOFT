#To-Do List command-line application which allows users to create, update and track their list

def main():
    tasks = []  #This empty list will hold the tasks

    while True:
        print("\n- - - - To-Do List - - - -")  #Displaying a menu with four options
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Mark Task as Done")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print()
            n_tasks = int(input("How many task you want to add: "))
            
            for i in range(n_tasks):
                task = input("Enter the task: ")
                tasks.append({"task": task, "done": False})
                print("Task added!")

        elif choice == '2':   #loop to go through each task and show its number, description, and whether it’s done or not.
            print("\nTasks:")
            for index, task in enumerate(tasks):
                status = "Done" if task["done"] else "Not Done"
                print(f"{index + 1}. {task['task']} - {status}")

        elif choice == '3':  #To change the status of task as done
            task_index = int(input("Enter the task number to mark as done: ")) - 1
            if 0 <= task_index < len(tasks):
                tasks[task_index]["done"] = True
                print("Task marked as done!")
            else:
                print("Invalid task number.")

        elif choice == '4':  #To break-out of To-Do list
            print("\nExited from the To-Do List.\n")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()