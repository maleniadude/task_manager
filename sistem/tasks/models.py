from datetime import date
import uuid
from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError
from django.utils.timezone import now

class Category(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True, default="cualquiera")

    def __str__(self):
        return self.name

class Task(models.Model):
    STATUS_CHOICES = [
        ('pending_tasks', 'Pendiente'),
        ('in_progress_tasks', 'En Progreso'),
        ('completed_tasks', 'Completada'),
    ]

    title = models.CharField(max_length=200, default="")
    subtitle = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    estado = models.CharField( max_length=50, choices=STATUS_CHOICES, default='pending_tasks')
    fecha_ven = models.DateField(blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    category = models.ManyToManyField(Category, blank=True)
    post_date = models.DateTimeField(default=now)
    update = models.DateTimeField(default=now)
    image_frontpage = models.ImageField(null=True, blank=True, default="image_default.jpg")

    def __str__(self):
        return self.title

    def clean(self):
        if self.fecha_ven and self.fecha_ven < date.today():
            raise ValidationError("La fecha de vencimiento no puede ser en el pasado.")

    class Meta:
        verbose_name = "Tarea"
        verbose_name_plural = "Tareas"
        ordering = ['-post_date']