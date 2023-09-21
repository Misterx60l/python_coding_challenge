# To-Do list
# Created by Anjaan
todo_list = []

# function to add task in the todo list:
def add_Task(task):
	todo_list.append(task)	

# function to view task in the todo list	
def view_Task():
	if todo_list:
		print("\nTo-Do list\n")
		for index, task in enumerate(todo_list, start=1):
			print(f"{index}. {task}")
	else:
		print("You didn't added task in the To-Do list...")
		
# function to remove task from the todo list	
def remove_Task(task_index):
	if 1 <= task_index <= len(todo_list):
		remove_task = todo_list.pop(task_index)
		print(f"Task {remove_task} removed from the to do list")
	
	else:
		print("Enter a valid index number")
		
# Main Loop
while True:
	print("\nOptions")
	print("1. Add Tasks")
	print("2. View Tasks")
	print("3. Remove Task")
	print("4. Quit")
	
	Opt = int(input("Choose an Options from the above! >>>> "))
	
	if Opt == 1:
		task = input("Enter Your Task >>> ") 
		add_Task(task)
	elif Opt == 2:
		view_Task()
	elif Opt == 3:
		task_index = int(input("Enter the Index number >>> "))
		remove_Task(task_index)
	elif Opt == 4:
		print("Good Bye Sir")
		break
	else:
		print("Please enter a valid option!")
		
		