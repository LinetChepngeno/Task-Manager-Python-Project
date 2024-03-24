from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from helpers import (
    create_user,
    update_user, 
    delete_user, 
    view_all_users, 
    find_user,
    create_project,
    update_project,
    delete_project,
    view_all_projects,
    find_project,
    view_tasks_for_project,
    create_task,
    update_task,
    delete_task,
    view_all_tasks,
    find_task

)

engine = create_engine('sqlite:///taskmanager.db')

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

if __name__ == "__main__":
    main()