from django.views.generic.base import TemplateView
from datetime import date, timedelta
from django.shortcuts import redirect, render
from .forms import TaskForm
from tasks.models import Category, Task
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.http import Http404


class RegisterView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'Registration/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = User.objects.get(username=username)
        from django.contrib.auth import login
        login(self.request, user)
        return response
    
class CustomLoginView(LoginView):
    template_name = 'Registration/login.html'

    def get_success_url(self):
        return reverse_lazy('dashboard')

class Dashboard(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_tasks = Task.objects.filter(usuario=self.request.user)
        context['total_tareas'] = user_tasks.count()
        context['pendientes'] = user_tasks.filter(estado='P').count()
        context['en_proceso'] = user_tasks.filter(estado='E').count()
        context['completadas'] = user_tasks.filter(estado='C').count()
        context['proximas_vencer'] = user_tasks.filter(
            fecha_ven__range=[date.today(), date.today() + timedelta(days=3)]
        )
        return context

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = '/tasks/'

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)
  
class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'task_list.html'

    def get_queryset(self):
        queryset = Task.objects.filter(usuario=self.request.user)

        category = self.request.GET.get('category')
        if category:
            queryset = queryset.filter(categorys__id=category)

        search_query = self.request.GET.get('q')
        if search_query:
            queryset = queryset.filter(titulo__icontains=search_query)

        return queryset
        
class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'task.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        if not queryset.exists():
            raise Http404("No se encontró la tarea.")
        return queryset
    
class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = '__all__'
    template_name = 'task_update.html'
    def edit(request, task_id):
        task = Task.objects.get(id=task_id)

        if request.method == 'POST':
            task.title = request.POST.get('title')
            task.description = request.POST.get('description')
            task.fecha_ven = request.POST.get('fecha_ven')
            task.estado = request.POST.get('estado')
            category_ids = request.POST.getlist('categories')

            task.category.set(category_ids)
            task.save()
            return redirect('dashboard')

        categories = Category.objects.all()

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'task_confirm_delete.html'
    success_url = reverse_lazy('task_list')