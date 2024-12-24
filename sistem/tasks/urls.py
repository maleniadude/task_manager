from django.urls import path
from .views import TaskCreate, TaskDeleteView, TaskDetailView, TaskListView, TaskUpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import RegisterView, Dashboard
from tasks import views

urlpatterns = [
    path('dashboard/', Dashboard.as_view(), name='dashboard'),

    path('tasks/', TaskListView.as_view(), name='task_list'),
    path('task/<uuid:pk>/', TaskDetailView.as_view(), name='task'),

    path('tasks/create/', TaskCreate.as_view(), name='task_create'),
    path('tasks/<uuid:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('tasks/<uuid:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),

    path('login/', LoginView.as_view(template_name='Registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/login/'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]

