from django.test import TestCase
from employee.forms import (EmployeeCreateForm,
                            EmployeeUsernameSearchForm)
from employee.models import Position
from datetime import date, timedelta
from task.forms import TaskCreateForm, Task
from task.models import TaskType, Task


class EmployeeFormTest(TestCase):
    def test_employee_creation_form_with_valid_position(self):
        position = Position.objects.create(name="Developer")
        form_data = {
            "username": "Stasyan",
            "email": "stasik@gmail.com",
            "password1": "Stastest123*",
            "password2": "Stastest123*",
            "first_name": "Stanislav",
            "last_name": "Cshovich",
            "position": position,
        }
        form = EmployeeCreateForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)

    def test_employee_search_form_is_valid(self):
        form_data = {
            "username": "Stasyan",
        }
        form = EmployeeUsernameSearchForm(data=form_data)
        self.assertTrue(form.is_valid())


class TaskFormTest(TestCase):
    def setUp(self):
        self.task_data = {
            "name": "Eugene",
            "task_type": TaskType.objects.create(name="TestTask"),
            "priority": 1,
            "description": "Test Task",
            "deadline": date.today() - timedelta(days=1),
        }

    def test_invalid_deadline(self):
        form = TaskCreateForm(data=self.task_data)
        self.assertFalse(form.is_valid())

    def test_valid_deadline(self):
        self.task_data["deadline"] = date.today() + timedelta(1)
        form = TaskCreateForm(data=self.task_data)
        self.assertTrue(form.is_valid())
        form.save()

        self.assertEqual(
            Task.objects.get(id=1).name,
            self.task_data["name"]
        )

