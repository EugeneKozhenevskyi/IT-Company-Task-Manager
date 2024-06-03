from django import forms
from django.contrib.auth.forms import UserCreationForm

from employee.models import Employee


class EmployeeCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Employee
        fields = UserCreationForm.Meta.fields + (
            "position", "first_name", "last_name", "email"
        )
        widgets = {
            "position": forms.RadioSelect(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].required = True
        self.fields["last_name"].required = True


class EmployeeUpdateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ("first_name", "last_name", "position", "email")


class EmployeeUsernameSearchForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Searching by username",
                "type": "search",
                "id": "exampleInputSearch"
            }
        )
    )
