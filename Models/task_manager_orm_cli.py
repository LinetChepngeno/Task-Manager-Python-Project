from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

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
    owner_id = Column(Integer, ForeignKey('users.id'))
    owner = relationship('User', back_populates='projects')
    tasks = relationship('Task', back_populates='project')

    def __repr__(self):
        return f"Project(id={self.id}, name='{self.name}', owner_id={self.owner_id})"

    @classmethod
    def create(cls, session, name, owner_id):
        project = cls(name=name, owner_id=owner_id)
        session.add(project)
        session.commit()
        return project

    def update(self, session, name, owner_id):
        self.name = name
        self.owner_id = owner_id
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
    projects = relationship('Project', back_populates='owner', lazy="subquery")

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
    
# Create the database tables
engine = create_engine('sqlite:///taskmanager.db')
Base.metadata.create_all(engine)

# Create a new session
Session = sessionmaker(bind=engine)
session = Session()

#use the session to perform CRUD operations on your models
user = User.create(session, 'test')