
from django.contrib import admin
from django.urls import path
from todo_list_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.todo_view),
    path('todolist/', views.todo_view),
    path('add_todo_item/', views.add_item),
    path('delete_todo_item/<int:i>/', views.delete_item),
]
