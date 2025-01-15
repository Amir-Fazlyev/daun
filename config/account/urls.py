from django.urls import path
from .views import register_view, login_view, logout_view, index  # Импортируем переименованные функции

urlpatterns = [
    path('register/', register_view, name='register'),  # Используем register_view
    path('login/', login_view, name='login'),          # Используем login_view
    path('logout/', logout_view, name='logout'),
    path('index/', index, name='index'),      # Используем logout_view
]   