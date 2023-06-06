from django.contrib import admin
from .models import ToDoItem

class ToDoAdmin(admin.ModelAdmin):
    model = ToDoItem
    exclude = ['createdAt']

admin.site.register(ToDoItem, ToDoAdmin)