from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative_base import declarative_base

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