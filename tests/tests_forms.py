from django.test import TestCase
from employee.forms import EmployeeCreateForm
from employee.models import Position


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
            "position": position.id,
        }
        form = EmployeeCreateForm(data=form_data)
        self.assertTrue(form.is_valid())

        cleaned_data = form.cleaned_data
        self.assertEqual(cleaned_data["username"], form_data["username"])
        self.assertEqual(cleaned_data["email"], form_data["email"])
        self.assertEqual(cleaned_data["first_name"], form_data["first_name"])
        self.assertEqual(cleaned_data["last_name"], form_data["last_name"])
        self.assertEqual(cleaned_data["position"], position)
