from dataclasses import field
from pyexpat import model
from tkinter import Widget
from django import forms
from .models import Student


class Add_stu(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('roll', 'name', 'course', 'city')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'roll': forms.NumberInput(attrs={'class': 'form-control'}),
            'course': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
        }
