from django import forms
from django.forms import ModelForm
from .models import Task

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'subtitle', 'description', 'content', 'fecha_ven', 'update', 'estado', 'image_frontpage', 'category']

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            widget = field.widget
            # Aplicar clases Bootstrap por defecto
            if not isinstance(widget, forms.CheckboxInput):
                widget.attrs['class'] = 'form-control'
            if isinstance(widget, forms.FileInput):
                widget.attrs['class'] = 'form-control-file'  # para campos de imagen
            widget.attrs['placeholder'] = field.label
