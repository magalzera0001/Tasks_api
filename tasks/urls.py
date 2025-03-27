from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tasks/', views.tasks, name='tasks'),
    path('login/', views.user_login, name="login"),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout')
]