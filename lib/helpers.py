from models.task_manager import TaskManager, Task, Project, User


task_manager=TaskManager()

# User CRUD Operations
def create_user(session):
    name = input("Enter the user's name: ")
    user = User.create(session,name)
    print(f"User created: {user}")

def update_user(session):
    user_id = int(input("Enter the user's ID: "))
    user = User.find_by_id(session, user_id)
    if user:
        new_name = input(f"Enter the new name for user '{user.name}': ")
        user.update(session, new_name)
        print(f"User with ID {user_id} has been updated.")
    else:
        print(f"User with ID {user_id} not found.")

def delete_user(session):
    user_id = int(input("Enter the user's ID: "))
    if User.delete(session, user_id):
        print(f"User with ID {user_id} has been deleted.")
    else:
        print(f"User with ID {user_id} not found.")

def view_all_users(session):
    users = User.get_all(session)
    if users:
        for user in users:
            print(user)
    else:
        print("No users found.")

def find_user(session):
    print("1. Find by ID")
    print("2. Find by Name")
    choice = input("Enter your choice: ")

    if choice == "1":
        user_id = int(input("Enter user ID: "))
        user = User.find_by_id(session, user_id)
        if user:
            print(user)
        else:
            print(f"User with ID {user_id} not found.")
    elif choice == "2":
        name = input("Enter user name: ")
        user = User.find_by_name(session, name)
        if user:
            print(user)
        else:
            print(f"No user found with name '{name}'.")
    else:
        print("Invalid choice.")

# Project CRUD Operations
def create_project(session):
    name = input("Enter the project name: ")
    user_id = int(input("Enter the user ID for the project: "))
    user = User.find_by_id(session, user_id)
    if user:
        project = Project.create(session, name, user_id)
        print(f"Project created: {project}")
    else:
        print(f"User with ID {user_id} not found.")

def update_project(session):
    project_id = int(input("Enter the project ID: "))
    project = Project.find_by_id(session, project_id)
    if project:
        new_name = input(f"Enter the new name for project '{project.name}': ")
        new_user_id = int(input("Enter the new user ID for the project: "))
        new_user = User.find_by_id(session, new_user_id)
        if new_user:
            project.update(session, new_name, new_user_id)
            print(f"Project with ID {project_id} has been updated.")
        else:
            print(f"User with ID {new_user_id} not found.")
    else:
        print(f"Project with ID {project_id} not found.")

def delete_project(session):
    project_id = int(input("Enter the project ID: "))
    if Project.delete(session, project_id):
        print(f"Project with ID {project_id} has been deleted.")
    else:
        print(f"Project with ID {project_id} not found.")

def view_all_projects(session):
    projects = Project.get_all(session)
    if projects:
        for project in projects:
            print(project)
    else:
        print("No projects found.")

def find_project(session):
    print("1. Find by ID")
    print("2. Find by Name")
    choice = input("Enter your choice: ")

    if choice == "1":
        project_id = int(input("Enter project ID: "))
        project = Project.find_by_id(session, project_id)
        if project:
            print(project)
        else:
            print(f"Project with ID {project_id} not found.")
    elif choice == "2":
        name = input("Enter project name: ")
        project = Project.find_by_name(session, name)
        if project:
            print(project)
        else:
            print(f"No project found with name '{name}'.")
    else:
        print("Invalid choice.")

def view_tasks_for_project(session):
    project_id = int(input("Enter the project ID: "))
    project = Project.find_by_id(session, project_id)
    if project:
        tasks = project.tasks
        if tasks:
            print(f"Tasks for project '{project.name}':")
            for task in tasks:
                print(task)
        else:
            print(f"No tasks found for project '{project.name}'.")
    else:
        print(f"Project with ID {project_id} not found.")

# Task CRUD Operations
def create_task(session):
    description = input("Enter the task description: ")
    project_id = int(input("Enter the project ID for the task: "))
    project = Project.find_by_id(session, project_id)
    if project:
        task = Task.create(session, description, project_id)
        print(f"Task created: {task}")
    else:
        print(f"Project with ID {project_id} not found.")

def update_task(session):
    task_id = int(input("Enter the task ID: "))
    task = Task.find_by_id(session, task_id)
    if task:
        new_description = input(f"Enter the new description for task '{task.description}': ")
        new_project_id = int(input("Enter the new project ID for the task: "))
        new_project = Project.find_by_id(session, new_project_id)
        if new_project:
            task.update(session, new_description, new_project_id)
            print(f"Task with ID {task_id} has been updated.")
        else:
            print(f"Project with ID {new_project_id} not found.")
    else:
        print(f"Task with ID {task_id} not found.")

def delete_task(session):
    task_id = int(input("Enter the task ID: "))
    if Task.delete(session, task_id):
        print(f"Task with ID {task_id} has been deleted.")
    else:
        print(f"Task with ID {task_id} not found.")

def view_all_tasks(session):
    tasks = Task.get_all(session)
    if tasks:
        for task in tasks:
            print(task)
    else:
        print("No tasks found.")

def find_task(session):
    print("1. Find by ID")
    print("2. Find by Description")
    choice = input("Enter your choice: ")

    if choice == "1":
        task_id = int(input("Enter task ID: "))
        task = Task.find_by_id(session, task_id)
        if task:
            print(task)
        else:
            print(f"Task with ID {task_id} not found.")
    elif choice == "2":
        description = input("Enter task description: ")
        task = Task.find_by_description(session, description)
        if task:
            print(task)
        else:
            print(f"No task found with description '{description}'.")
    else:
        print("Invalid choice.")

