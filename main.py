from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import User, Project, Task

engine = create_engine('sqlite:///db/database.db')
Session = sessionmaker(bind=engine)

def main():
    session = Session()

    while True:
        print("\nTask Manager")
        print("1. Manage Users")
        print("2. Manage Projects")
        print("3. Manage Tasks")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            manage_users(session)
        elif choice == "2":
            manage_projects(session)
        elif choice == "3":
            manage_tasks(session)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

    session.close()

def manage_users(session):
    while True:
        print("\nManage Users")
        print("1. Create User")
        print("2. Update User")
        print("3. Delete User")
        print("4. View All Users")
        print("5. Find User")
        print("6. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            create_user(session)
        elif choice == "2":
            update_user(session)
        elif choice == "3":
            delete_user(session)
        elif choice == "4":
            view_all_users(session)
        elif choice == "5":
            find_user(session)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

def manage_projects(session):
    while True:
        print("\nManage Projects")
        print("1. Create Project")
        print("2. Update Project")
        print("3. Delete Project")
        print("4. View All Projects")
        print("5. Find Project")
        print("6. View Tasks for a Project")
        print("7. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            create_project(session)
        elif choice == "2":
            update_project(session)
        elif choice == "3":
            delete_project(session)
        elif choice == "4":
            view_all_projects(session)
        elif choice == "5":
            find_project(session)
        elif choice == "6":
            view_tasks_for_project(session)
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please try again.")

def manage_tasks(session):
    while True:
        print("\nManage Tasks")
        print("1. Create Task")
        print("2. Update Task")
        print("3. Delete Task")
        print("4. View All Tasks")
        print("5. Find Task")
        print("6. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            create_task(session)
        elif choice == "2":
            update_task(session)
        elif choice == "3":
            delete_task(session)
        elif choice == "4":
            view_all_tasks(session)
        elif choice == "5":
            find_task(session)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

# User CRUD Operations
def create_user(session):
    name = input("Enter the user's name: ")
    user = User.create(session, name)
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