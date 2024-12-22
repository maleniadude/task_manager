from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Task, Category

admin.site.register(Task)

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'estado', 'fecha_ven', 'usuario')
    list_filter = ('estado', 'usuario', 'fecha_ven')
    search_fields = ('title',)

admin.site.register(Category)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
