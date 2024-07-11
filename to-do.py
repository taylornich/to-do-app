# mini project 1 task 2
class ToDo:
    def __init__(self):
        self.list = []

        # mini project task 1
    
        print('''Welcome to the To-Do List App!
                    
        Menu:
        1. Add a task
        2. View tasks
        3. Mark a task as complete
        4. Delete a task
        5. Quit''')

    def add_task(self, title="incomplete"):
        self.list.append({"title": title, "complete": False})

    def view_tasks(self):
        if not self.list:
            print("Nothing in to do list.")
        else:
            print("To do:")
            for i in range(len(self.list)):
                task = self.list[i]
                status = "Complete" if task['complete'] else "Incomplete"
                print(f"{i+1}. {task['title']} : {status}")

    def mark_complete(self, task_index):
        if 1 <= task_index <= len(self.list):
            self.list[task_index - 1]['complete'] = True
        else:
            print("Invalid")

    def delete_task(self, task_index):
        if 1 <= task_index <= len(self.list):
            task_to_delete = self.list[task_index - 1]
            self.list.remove(task_to_delete)
        else:
            print("Invalid")

    def quit(self):
        print("You have successfully quit the application.")
        quit()

def main():
    todo_list = ToDo()

    # mini project task 1
    while True:
        #mini project task 4
        try:
        # mini project task 2
            menu_choice = input("Please enter your choice:")

            if menu_choice == "1": 
                title = input("Enter task title:")
                todo_list.add_task(title)
                print("Task added.")

            elif menu_choice == "2":
                todo_list.view_tasks()

            elif menu_choice == "3":
                todo_list.view_tasks()
                task_index = input("Enter index of the task to mark as complete.")
                if task_index.isdigit():
                    task_index = int(task_index)
                    todo_list.mark_complete(task_index)
                    print("Task successfully marked complete.")
                else:
                    print("Input invalid.")

            elif menu_choice == "4":
                todo_list.view_tasks()
                task_index = input("Enter the index of the task to delete:")
                if task_index.isdigit():
                    task_index = int(task_index)
                    todo_list.delete_task(task_index)
                else:
                    print("Invalid input.")

            elif menu_choice == "5":
                todo_list.quit()
            else:
                print("Your choice is invalid, please enter a number 1-5.")
        except ValueError as LikelyInputError:
            print(f"ValueError occurred: {LikelyInputError}")
        except IndexError as PossibleIndexOutOfBounds:
            print(f"IndexError occurred {PossibleIndexOutOfBounds}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        finally:
            pass

if __name__ == "__main__":
    main()


