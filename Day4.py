# To-Do list
# Created by Anjaan
todo_list = []

# function to add task
def add_Task(task):
	todo_list.append(task)

# function to view task
def view_Task():
	if todo_list:
		print("\nTo-Do list\n")
		for index, task in enumerate(todo_list, start=1):
			print(f"{index}. {task}")

# function to remove task
def remove_Task(task_index):
	if 1 <= task_index <= len(todo_list):
		remove_task = todo_list.pop(task_index - 1) 
		print(f"Task {remove_task} from the todo list")
	else:
		print("\nPlease enter a valid number")
		
		
# Main loop
while True:
	try:
		print("\nOption")		
		print("1. Add task")
		print("2. View task")
		print("3. Remove task")
		print("4. Quit")
		
		Opt = int(input("Choose an option from above! >>> "))
	# checking 
		if Opt == 1:
			task = input("Enter a task. >>> ")
			add_Task(task)
		elif Opt == 2:
			view_Task()
		elif Opt == 3:
			task_index = int(input("Enter the index number >>> "))
			remove_Task(task_index)
		elif Opt == 4:
			print("Good Bye sir")
			break
		else:
			print("Please enter a valid value....")
	except ValueError:
		print("Please Enter a valid number...")	
