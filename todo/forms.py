from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Task


class RegisterForm(UserCreationForm):

    email = forms.EmailField()

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
        ]


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task

        fields = [
            "title",
            "description",
            "priority",
            "status",
            "due_date",
        ]

        widgets = {
            "title": forms.TextInput(attrs={
                "class": "w-full border rounded-lg p-3",
                "placeholder": "Task title"
            }),

            "description": forms.Textarea(attrs={
                "class": "w-full border rounded-lg p-3",
                "rows": 4
            }),

            "priority": forms.Select(attrs={
                "class": "w-full border rounded-lg p-3"
            }),

            "status": forms.Select(attrs={
                "class": "w-full border rounded-lg p-3"
            }),

            "due_date": forms.DateInput(attrs={
                "type": "date",
                "class": "w-full border rounded-lg p-3"
            }),
        }