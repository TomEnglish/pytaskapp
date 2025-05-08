


tasklist = []


# Add tasks
def add_task():
    """Prompts the user to add a new task to the tasklist with validation.

    Handles empty input, duplicate tasks (case-sensitive), and tasks
    exceeding 50 characters. Allows cancellation.
    """
    while True:
        task = input("Enter a new task (or type 'cancel' to return to menu): ")
        if task.lower() == 'cancel':
            print("Task addition cancelled.")
            return
        if not task.strip():  # Check for empty or whitespace-only strings
            print("Task cannot be empty. Please enter a valid task.")
        else: # Task is not empty and not 'cancel'
            if len(task) > 50:
                print("Task is too long. Please limit to 50 characters.")
            elif task in tasklist:
                print(f"Task '{task}' already exists. Please enter a different task.")
            else:
                tasklist.append(task)
                print("\nTasks:")
                print(f"Task '{task}' added.")
                break # Exit the loop

# View tasks
def view_tasks():
    """Displays all tasks currently in the tasklist with their numbers.

    If the tasklist is empty, it prints a message indicating so.
    """
    if not tasklist:
        print("No tasks available.") #Alert no tasks
    else:
        print("\nTasks:")
        for index, task in enumerate(tasklist):
             print(f"{index + 1}. {task}")
        #print("-" * 20) # Separator

# Delete tasks
def delete_task():
    """Allows the user to delete a task from the tasklist by its name.

    Displays tasks first. Handles cases where the task is not found.
    """
    view_tasks()
    if not tasklist:
        return # No tasks to delete

    try:
        deletedtask = input("Enter the name of the task to delete: ")
        tasklist.remove(deletedtask)
    except ValueError:
        print("Invalid input. Please enter an existing task") #Alert notfound
    else:
        print(f"Task '{deletedtask}' deleted.")

# Quit the application
def quit_app():
    """Clears the tasklist and exits the application.

    Prints a goodbye message before exiting.
    """
    tasklist.clear()
    print("Exiting the Task Manager. Goodbye!")
    exit()

def main():
    """Runs the main loop of the task manager application.

    Displays the menu options (add, view, delete, quit) and processes
    user selections, calling the appropriate functions.
    """
    # Main loop
    while True:
        print("\nWelcome to the Task Manager!")
        #view_tasks()
        print("Options:")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Delete a task")
        print("4. Quit")
        selection = input("Please select an option (1-4): ")

        if selection == '1':
            add_task()
        elif selection == '2':
            view_tasks()
        elif selection == '3':
            delete_task()
        elif selection == '4':
            quit_app()
        else:
            print("Invalid option. Please enter a number between 1 and 4.")

if __name__ == "__main__": #allows the script to be run as a standalone program
    main()