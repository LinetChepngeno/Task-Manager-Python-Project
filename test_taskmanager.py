import unittest
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Models.user import User
from Models.task import Task
from Models.project import Project

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        # Create an in-memory SQLite database for testing
        self.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def tearDown(self):
        self.session.close()

    def test_user_crud(self):
        # Test creating a user
        user = User.create(self.session, "Test User")
        self.assertEqual(user.name, "Test User")

        # Test updating a user
        new_name = "Updated User"
        user.update(self.session, new_name)
        self.assertEqual(user.name, new_name)

        # Test deleting a user
        user_id = user.id
        User.delete(self.session, user_id)
        self.assertIsNone(User.find_by_id(self.session, user_id))

    def test_project_crud(self):
        # Create a user for testing project operations
        user = User.create(self.session, "Test User")

        # Test creating a project
        project = Project.create(self.session, "Test Project", user.id)
        self.assertEqual(project.name, "Test Project")
        self.assertEqual(project.user_id, user.id)

        # Test updating a project
        new_name = "Updated Project"
        new_user = User.create(self.session, "New User")
        project.update(self.session, new_name, new_user.id)
        self.assertEqual(project.name, new_name)
        self.assertEqual(project.user_id, new_user.id)

        # Test deleting a project
        project_id = project.id
        Project.delete(self.session, project_id)
        self.assertIsNone(Project.find_by_id(self.session, project_id))

    def test_task_crud(self):
        # Create a user and project for testing task operations
        user = User.create(self.session, "Test User")
        project = Project.create(self.session, "Test Project", user.id)

        # Test creating a task
        task = Task.create(self.session, "Test Task", project.id)
        self.assertEqual(task.description, "Test Task")
        self.assertEqual(task.project_id, project.id)

        # Test updating a task
        new_description = "Updated Task"
        new_project = Project.create(self.session, "New Project", user.id)
        task.update(self.session, new_description, new_project.id)
        self.assertEqual(task.description, new_description)
        self.assertEqual(task.project_id, new_project.id)

        # Test deleting a task
        task_id = task.id
        Task.delete(self.session, task_id)
        self.assertIsNone(Task.find_by_id(self.session, task_id))

if __name__ == '__main__':
    unittest.main()