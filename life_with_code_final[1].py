"""
   This is a program that allows you to manage tasks.
      specifically : - to create or paln tasks
                             - to display tasks
                             - to update to tasks
                             - to delete tasks

"""


print(" \n\n     This is my to do list \n ")
Tasks=[]

def create_task():  # used to create a new task
   title = input(" Enter the title of the task : ")
   status = input(" Enter the status of the task (pending / in progress /done!!)")
   time = input(" Enter the time of the task : ")
   Task = {"task ": title, "status ": status ,"time " : time}
   Tasks.append(Task)
   print("Task successfully created 🙏")

def display_tasks():  # used to display tasks
   if len(Tasks) == 0:
       print("There is no tasks to be displayed 👁️")
   else:
       print(f"Tasks : {Tasks}")

def update_task():  # used to update tasks
    task_index = int(input("Enter the task number")) - 1
    if 0 <= task_index < len(Tasks):
        title = input(" Enter the title of the task which needs status update : ")
        new_status = input(" Enter the new status(pending / in progress /done!!)")
        new_time=input(" Enter the the new time  of the task : ")
        Tasks[task_index]['title'] = title
        Tasks[task_index]['status'] = new_status
        Tasks[task_index]['time'] = nee_time
        Task = {"task ": title, "status ": new_status," time  " : new_time}
        Tasks.pop(task_index )
        Tasks.append(Task)
        print("Task successfully updated 🙏")
    else: 
       print("invalid index  😔")
       return
       
def delete_task() :  # used to delete tasks
    task_index = int(input("Enter the task number : ")) - 1
    if 0 <= task_index < len(Tasks):
        del Tasks[task_index]
        print("Task successfully deleted ❌")
    else:
        print("invalid index  😔")
    return
    
while True:
    print("  \n Menu  ")
    print("Enter 1 - to create tasks  p\n")
    print("Enter 2 - to display tasks  \n")
    print("Enter 3 - to update tasks  \n")
    print("Enter 4 - to delete tasks  \n")
    print("Enter 5 - to exit \n")
    response = input(" please enter your choice : \n ")
    if response == '1':
        create_task()
    elif response == '2':
      display_tasks()
    elif response == '3':
       update_task()

    elif response == '4':
        delete_task()
    elif response == '5':
        break
    else:
        print("Invalid choice ⚠️")
        break













































