from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

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
    def create(cls, session, name, user_id):
        project = cls(name=name, user_id=user_id)
        session.add(project)
        session.commit()
        return project

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