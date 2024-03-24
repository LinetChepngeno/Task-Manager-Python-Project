from sqlalchemy.orm import sessionmaker
from task_manager import Base, engine, User, Task, Project

Session = sessionmaker(bind=engine)
session=Session()

def seed_database():
    Base.metadata.create_all(engine)
    task_data=[
        {
            "description": "Test Task1",
            "project_id": "1"
        },
         {
            "description": "Test Task2",
            "project_id": "2"
        },
         {
            "description": "Test Task3",
            "project_id": "3"
        }

    ] 
    for task in task_data:
        task_info=Task(**task)
        session.add(task_info)

    user_data=[
        {
            "name": "Test User1"
        },
           {
            "name": "Test User2"
        },
           {
            "name": "Test User3"
        }
    ]
    for user in user_data:
        user_info=User(**user)
        session.add(user_info)

    project_data=[
        {
            "name": "Project X",
            "user_id": 1
        },
          {
            "name": "Project Y",
            "user_id": 2
        },
          {
            "name": "Project Z",
            "user_id": 3
        }
    ]
    for project in project_data:
        project_info=Project(**project)
        session.add(project_info)
    
    session.commit()
    
if __name__ == "__main__":
    seed_database()
    print("Database seeded successfully")