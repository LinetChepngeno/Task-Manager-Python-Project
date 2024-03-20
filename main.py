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