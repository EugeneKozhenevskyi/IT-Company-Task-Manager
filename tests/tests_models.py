from datetime import date

from django.test import TestCase
from employee.models import Position
from django.contrib.auth import get_user_model
from task.models import TaskType, Task
from task.models import Tag

User = get_user_model()


class PositionModelTest(TestCase):
    def setUp(self):
        self.position = Position.objects.create(name="Developer")

    def test_create_position(self):
        self.assertEqual(self.position.name, "Developer")
        self.assertEqual(str(self.position), "Developer")

    def test_position_ordering(self):
        Position.objects.create(name="Manager")
        positions = Position.objects.all()
        self.assertEqual(positions[0].name, "Developer")
        self.assertEqual(positions[1].name, "Manager")


class EmployeeModelTest(TestCase):
    def setUp(self):
        self.position = Position.objects.create(name="Developer")
        self.user = User.objects.create_user(
            username="Stasyan",
            email="stasik@gmail.com",
            password="Stastest123*",
            first_name="Stanislav",
            last_name="Cshovich",
            position=self.position
        )

    def test_create_employee(self):
        self.assertEqual(self.user.username, "Stasyan")
        self.assertEqual(self.user.email, "stasik@gmail.com")
        self.assertEqual(self.user.first_name, "Stanislav")
        self.assertEqual(self.user.last_name, "Cshovich")
        self.assertEqual(self.user.position.name, "Developer")

    def test_employee_ordering(self):
        position_manager = Position.objects.create(name="Manager")
        user2 = User.objects.create_user(username="user2", position=position_manager)
        employees = User.objects.all()
        self.assertEqual(employees[0].username, "Stasyan")
        self.assertEqual(employees[1].username, "user2")


class TaskTypeModelTest(TestCase):
    def setUp(self):
        self.task_type = TaskType.objects.create(name="Bug")

    def test_create_task_type(self):
        self.assertEqual(self.task_type.name, "Bug")
        self.assertEqual(str(self.task_type), "Bug")

    def test_task_type_ordering(self):
        TaskType.objects.create(name="Feature")
        task_types = TaskType.objects.all()
        self.assertEqual(task_types[0].name, "Bug")
        self.assertEqual(task_types[1].name, "Feature")

class TagModelTest(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(name="Urgent")

    def test_create_tag(self):
        self.assertEqual(self.tag.name, "Urgent")
        self.assertEqual(str(self.tag), "Urgent")

    def test_tag_ordering(self):
        Tag.objects.create(name="Low")
        tags = Tag.objects.all()
        self.assertEqual(tags[0].name, "Low")
        self.assertEqual(tags[1].name, "Urgent")

class TaskModelTest(TestCase):
    def setUp(self):
        self.task_type = TaskType.objects.create(name="Bug")
        self.tag = Tag.objects.create(name="Urgent")
        self.position = Position.objects.create(name="Developer")
        self.user = User.objects.create_user(
            username="Stasyan",
            email="stasik@gmail.com",
            password="Stastest123*",
            first_name="Stanislav",
            last_name="Cshovich",
            position=self.position
        )
        self.task = Task.objects.create(
            name="Fix Bug",
            description="Fix the critical bug",
            deadline=date(2024, 6, 30),
            is_completed=False,
            priority=2,
            task_type=self.task_type,
        )
        self.task.assignees.add(self.user)
        self.task.tags.add(self.tag)

    def test_create_task(self):
        self.assertEqual(self.task.name, "Fix Bug")
        self.assertEqual(self.task.description, "Fix the critical bug")
        self.assertEqual(self.task.deadline, date(2024, 6, 30))
        self.assertFalse(self.task.is_completed)
        self.assertEqual(self.task.priority, 2)
        self.assertEqual(self.task.task_type.name, "Bug")
        self.assertIn(self.user, self.task.assignees.all())
        self.assertIn(self.tag, self.task.tags.all())
        self.assertEqual(str(self.task), "Fix Bug")

    def test_task_ordering(self):
        task2 = Task.objects.create(
            name="Develop Feature",
            description="Develop new feature",
            deadline=date(2024, 6, 25),
            is_completed=False,
            priority=1,
            task_type=self.task_type,
        )
        tasks = Task.objects.all()
        self.assertEqual(tasks[0].name, "Develop Feature")
        self.assertEqual(tasks[1].name, "Fix Bug")
