from django.views.generic.base import TemplateView
from django.utils.timezone import now, timedelta
from django.db.models import Q
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
    
class CustomLogoutView(LoginView):
    template_name = 'Registration/logout.html'

    def get_success_url(self):
        return reverse_lazy('login')

class DashboardView(TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        user_tasks = Task.objects.filter(usuario=user)
        context['total_tasks'] = user_tasks.count()

        context['pending_tasks'] = user_tasks.filter(estado='pending_tasks')
        context['pending_tasks_count'] = context['pending_tasks'].count()

        context['in_progress_tasks'] = user_tasks.filter(estado='in_progress_tasks')
        context['in_progress_tasks_count'] = context['in_progress_tasks'].count()

        context['completed_tasks'] = user_tasks.filter(estado='completed_tasks')
        context['completed_tasks_count'] = context['completed_tasks'].count()

        upcoming_deadline = now() + timedelta(days=3)
        context['upcoming_tasks'] = user_tasks.filter(
            fecha_ven__lte=upcoming_deadline, 
            fecha_ven__gte=now()
        )
        context['upcoming_tasks_count'] = context['upcoming_tasks'].count()
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
        user = self.request.user

        category_filter = self.request.GET.get('category', None)
        search_query = self.request.GET.get('q', '')

        queryset = Task.objects.filter(usuario=user)

        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) | 
                Q(description__icontains=search_query)
            )
        
        if category_filter:
            queryset = queryset.filter(category=category_filter)

        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['search_query'] = self.request.GET.get('q', '')
        context['selected_category'] = self.request.GET.get('category', None)
        return context
        
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
    form_class = TaskForm
    template_name = 'task_update.html'
    success_url = '/tasks/'
    
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'task_confirm_delete.html'
    success_url = reverse_lazy('task_list')