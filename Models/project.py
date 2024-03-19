from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    projects = relationship('Project', back_populates='user')

    def __repr__(self):
        return f"User(id={self.id}, name='{self.name}')"

    @classmethod
    def create(cls, session, name):
        user = cls(name=name)
        session.add(user)
        session.commit()
        return user

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