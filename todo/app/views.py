from .models import ToDoItem
from rest_framework.views import APIView
from datetime import datetime
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class CreateToDoItemView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    # create todo item
    def post(self, request):
        data = request.data
        title = data.get("title")
        description = data.get("description")
        dueDate = data.get("dueDate")
        if not (title and description and dueDate):
            return Response({"error_message": "Some of mandatory fields title, description, dueDate are missing"}, status=status.HTTP_400_BAD_REQUEST)
        todo_status  = data.get("status")
        if todo_status and todo_status in ToDoItem.ToDoStatus.choices:
            return Response({"error_message": "Status not in Enum(OPEN, WORKING, DONE, OVERDUE)"}, status=status.HTTP_404_NOT_FOUND)
        todo_data=  {
            "title": title,
            "description": description,
            "tag": data.get("tag", ""),
            "dueDate": dueDate,
            "status": todo_status,
            "createdAt": datetime.now()
        }
        
        todo_item = ToDoItem.objects.create(**todo_data)
        
        return Response({"message": "todo item created successfully", "id": str(todo_item.todo_id)}, status=status.HTTP_200_OK)
     
class ReadToDoItemView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    #get todo item
    def get(self, request, id):
        todo_item = ToDoItem.objects.filter(todo_id=id).values()
        if len(todo_item)!=0:
            return Response({"message": "todo item fetched successfully", "data": todo_item}, status=status.HTTP_200_OK)
        else:
            return Response({"error_message": "Todo item not found with given id"}, status=status.HTTP_404_NOT_FOUND)
 
 
class ReadToDoItemsView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]   
    
    # read all todo items
    def get(self, request):
        todo_items = ToDoItem.objects.all().values()
        return Response({"message": "todo items fetched successfully", "items": todo_items}, status=status.HTTP_200_OK)

class UpdateToDoItemView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    # update todo item
    def post(Self, request, id):
        data = request.data
        todo_item = ToDoItem.objects.get(todo_id=id)
        if not todo_item:
            return Response({"error_message": "Todo item not found with given id"}, status=status.HTTP_404_NOT_FOUND)
        else:
            todo_status  = data.get("status")
            if todo_status and todo_status in ToDoItem.ToDoStatus.choices:
                return Response({"error_message": "Status not in Enum(OPEN, WORKING, DONE, OVERDUE)"}, status=status.HTTP_404_NOT_FOUND)
            todo_item.title = data.get("title", todo_item.title)
            todo_item.description = data.get("description", todo_item.description)
            todo_item.status = data.get("status", todo_item.status)
            todo_item.dueDate = data.get("dueDate", todo_item.dueDate)
            todo_item.save()
            return Response({"message": "todo item updated successfully"}, status=status.HTTP_200_OK)


class DeleteToDoItemView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]      
    
    # delete todo item
    def put(self, request, id):
        todo_item = ToDoItem.objects.get(todo_id=id)
        if not todo_item:
            return Response({"error_message": "Todo item not found with given id"}, status=status.HTTP_404_NOT_FOUND)
        else:
            todo_item.delete()
            return Response({"message": "todo item delted successfully"}, status=status.HTTP_200_OK)
            