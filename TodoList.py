# A simple command-line To-Do list application

class ToDoList:
    def __init__(self):
        self.tasks = []  # Store tasks as a list of dictionaries

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f'Added task: "{task}"')

    def update_task(self, index, new_task=None, completed=None):
        if 0 <= index < len(self.tasks):
            if new_task:
                self.tasks[index]['task'] = new_task
            if completed is not None:
                self.tasks[index]['completed'] = completed
            print(f'Task {index} updated.')
        else:
            print(f'Task {index} does not exist.')

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            print(f'Removed task: "{removed_task["task"]}"')
        else:
            print(f'Task {index} does not exist.')

    def list_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        for idx, task in enumerate(self.tasks, 1):
            status = "Completed" if task['completed'] else "Pending"
            print(f"{idx}. {task['task']} - {status}")

# Command-line menu to interact with the app
def menu():
    todo_list = ToDoList()

    while True:
        print("\n--- To-Do List ---")
        print("1. Add Task")
        print("2. Update Task")
        print("3. Remove Task")
        print("4. List All Tasks")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task description: ")
            todo_list.add_task(task)
        elif choice == '2':
            index = int(input("Enter the task number to update: ")) - 1
            new_task = input("Enter new description (leave blank to keep): ")
            status = input("Is the task completed? (y/n): ")
            todo_list.update_task(index, new_task if new_task else None, status.lower() == 'y')
        elif choice == '3':
            index = int(input("Enter the task number to remove: ")) - 1
            todo_list.remove_task(index)
        elif choice == '4':
            todo_list.list_tasks()
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid option, please try again.")

# Run the application
if __name__ == "__main__":
    menu()
