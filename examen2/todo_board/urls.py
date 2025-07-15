from django.urls import path
from . import views


app_name = 'todo_board'

urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add, name="add"),
    path("update/<int:todo_id>/", views.update, name="update"),
    path("delete/<int:todo_id>/", views.delete, name="delete"),
    path("list/all_id/", views.list_all_id, name="list_all_id"),
    path("list/all_id_title/", views.list_all_id_title, name="list_all_id_title"),
    path("list/not_done/", views.list_not_done, name="list_not_done"),
    path("list/done/", views.list_done, name="list_done"),
    path("list/all_id_user/", views.list_all_id_user, name="list_all_id_user"),
    path("list/done_id_user/", views.list_done_id_user, name="list_done_id_user"),
    path("list/not_done_id_user/", views.list_not_done_id_user, name="list_not_done_id_user"),

]
