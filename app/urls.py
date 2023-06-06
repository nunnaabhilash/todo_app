from django.urls import path
from .views import CreateToDoItemView, ReadToDoItemsView, ReadToDoItemView, UpdateToDoItemView, DeleteToDoItemView
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("todo_item/create/", CreateToDoItemView.as_view()),
    path('todo_item/read/', ReadToDoItemsView.as_view()),
    path('todo_item/read/<str:id>/', ReadToDoItemView.as_view()),
    path('todo_item/update/<str:id>/', UpdateToDoItemView.as_view()),
    path('todo_item/delete/<str:id>/', DeleteToDoItemView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)