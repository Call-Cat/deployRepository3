from django.urls import path
from . import views


urlpatterns = [
    path('index/', views.index, name='index'),
    path('logout_check/', views.logout_check_view, name='logout_check'),
    path('logout/', views.logout_view, name='logout'),
    path('index_view/', views.index_view, name='index_view'),
    path('mypage/', views.mypage_view, name='mypage'),
    path('change_password/', views.change_password, name='change_password'),
    path('new_todo/', views.new_todo, name='new_todo'),
    path('todo<int:todo_id>/', views.todo, name='todo'),
    path('edit_todo/<int:todo_id>/', views.edit_todo, name='edit_todo'),
    path('todo/update/<int:todo_id>/', views.update_todo, name='update_todo'), #edit時に編集した内容をアップデートするためのもの。
    path('delete_todo/<int:todo_id>/', views.delete_todo, name='delete_todo'),
]
