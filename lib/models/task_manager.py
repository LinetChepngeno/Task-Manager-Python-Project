from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///taskmanager.db')
Session = sessionmaker(bind=engine)

Base = declarative_base()

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    description = Column(String)
    project_id = Column(Integer, ForeignKey('projects.id'))

    project = relationship('Project', back_populates='tasks')

    def __repr__(self):
        return f"Task(id={self.id}, description='{self.description}', project_id={self.project_id})"

    @classmethod
    def create(cls, session, description, project_id):
        task = cls(description=description, project_id=project_id)
        session.add(task)
        session.commit()
        return task

    def update(self, session, description, project_id):
        self.description = description
        self.project_id = project_id
        session.commit()

    @classmethod
    def delete(cls, session, task_id):
        task = session.query(cls).get(task_id)
        if task:
            session.delete(task)
            session.commit()
            return True
        return False

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, task_id):
        return session.query(cls).get(task_id)

    @classmethod
    def find_by_description(cls, session, description):
        return session.query(cls).filter(cls.description == description).first()    

class Project(Base):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship('User', back_populates='projects')
    tasks = relationship('Task', back_populates='project')

    def __repr__(self):
        return f"Project(id={self.id}, name='{self.name}', user_id={self.user_id})"

    @classmethod
    def create(cls, session, name,user_id):
        project = cls(name=name, user_id=user_id)
        session.add(project)
        session.commit()
        return project

    def update(self, session, name, user_id):
        self.name = name
        self.user_id = user_id
        session.commit()

    @classmethod
    def delete(cls, session, project_id):
        project = session.query(cls).get(project_id)
        if project:
            session.delete(project)
            session.commit()
            return True
        return False

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, project_id):
        return session.query(cls).get(project_id)

    @classmethod
    def find_by_name(cls, session, name):
        return session.query(cls).filter(cls.name == name).first()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    projects = relationship('Project', back_populates='user', lazy="subquery")

    def __repr__(self):
        return f"User(id={self.id}, name='{self.name}')"

    @classmethod
    def create(cls, session, name):
        user = cls(name=name)
        session.add(user)
        session.commit()
        return user

    def update(self, session, name):
        self.name = name
        session.commit()

    @classmethod
    def delete(cls, session, user_id):
        user = session.query(cls).get(user_id)
        if user:
            session.delete(user)
            session.commit()
            return True
        return False

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, user_id):
        return session.query(cls).get(user_id)

    @classmethod
    def find_by_name(cls, session, name):
        return session.query(cls).filter(cls.name == name).first()
    
class TaskManager:
    def __init__(self):
        self.session = Session()

    def add_project(self, project_name, user_id):
        if not project_name or not user_id:
            print("Error: Project_name and user_id are required!")
            return

        user = self.session.query(User).get(user_id)
        if not user:
            print(f"Error: User with id {user_id} not found!")
            return

        project = Project(name=project_name, user_id=user_id)
        try:
            self.session.add(project)
            self.session.commit()
            print("Project Added Successfully")
        except Exception as e:
            self.session.rollback()
            print(f'Error: {e}')

    def add_user(self, first_name, last_name, email):
        if not first_name or not last_name or not email:
            print("Error: First Name, Last Name, and email are required!")
            return
        
        existing_user = self.session.query(User).filter_by(email=email).first()
        if existing_user:
            print(f"Error: User with email '{email}' already exists.")

        user = User(first_name=first_name, last_name=last_name, email=email)
        
        try:
            self.session.add(user)
            self.session.commit()
            print("User Added Successfully")
        except Exception as e:
            self.session.rollback()
            print(f'Error: {e}')
        
    def assign_user_to_project(self, user_id, project_id):
        user = self.session.get(User, user_id)
        project = self.session.get(Project, project_id) 

        if not user:
            print(f"Error: User with id {user_id} not found!")
            return

        if not project:
            print(f"Error: Project with id {project_id} not found!")
            return

        project.user_id = user_id
        try:
            self.session.commit()
            print("User assigned to the project successfully!")
        except Exception as e:
            self.session.rollback()
            print(f'Error: {e}')

    def get_all_projects(self):
        return self.session.query(Project).all()

    def get_all_tasks(self):
        return self.session.query(Task).all()

    def get_all_users(self):
        return self.session.query(User).all()
    


