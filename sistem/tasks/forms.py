from django.forms import ModelForm
from django import forms
from .models import Task

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = fields = ['title', 'subtitle', 'description', 'content', 'fecha_ven', 'estado', 'completed', 'image_frontpage', 'category']