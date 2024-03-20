from sqlalchemy import Column, ForeignKey, Integer, String, Text, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    email = Column(String(120), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    projects = relationship('Project', back_populates='owner')

    def __repr__(self):
        return f'<User(username="{self.username}", email="{self.email}")>'

class Project(Base):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(Text)
    owner_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    owner = relationship('User', back_populates='projects')
    tasks = relationship('Task', back_populates='project')

    def __repr__(self):
        return f'<Project(name="{self.name}", owner="{self.owner.username}")>'

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(Text)
    due_date = Column(DateTime)
    project_id = Column(Integer, ForeignKey('projects.id'), nullable=False)
    project = relationship('Project', back_populates='tasks')

    def __repr__(self):
        return f'<Task(name="{self.name}", project="{self.project.name}")>'