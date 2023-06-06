
# Algobulls todo app

  

Assignment -- [assignment](https://drive.google.com/file/d/1JMxYASdnw08jt9yAKzEWqUKOQ6z0gzQg/view?usp=sharing)

  

## Prerequisites

- Django
- RestApi
- Sql

  

## Requirements

  

- Create a Todo app to create/update/read todo items

- Timestamp should not be editable

- Admin interface

  

## Approach

-- Created a django prject 
![directory_structure](https://photos.app.goo.gl/Ni9VQL3uDDp9macUA)
-- Created model ToDoItem :
		1. title -- string
		2. description-- text
		3. status -- enum(OPEN, WORKING, OVERDUE, DONE)
		4. dueDate -- dateTime
		5. createdAt -- created date
## API's
-- Created Views for :
    1. create todo item -- API -- `POST - https://abhilash1289.pythonanywhere.com/todo_item/create/` 
	this API returns todo_id for using in further API's
    2. read todo item -- API -- `GET- https://abhilash1289.pythonanywhere.com/todo_item/read/{todo_id}`
	this API returns 200 for valid id with json of todoitem else 404 not found
    3. read all todo items -- API -- `GET- https://abhilash1289.pythonanywhere.com/todo_item/read/`
	this API return 200 and list of all todoitems
    4. update todo item -- API -- `POST- https://abhilash1289.pythonanywhere.com/todo_item/update/{todo_id}`
    this API updates the todo_item for the given id
    5. delete todo item -- API -- `POST- https://abhilash1289.pythonanywhere.com/todo_item/delete/{todo_id}`
    this API deletes todo_item for valid id else returns 404 not found

## Admin Interface
Added basic authentication for all the API's and also created a admin interface
website for admin interface -- `https://abhilash1289.pythonanywhere.com/admin`
Super User credentials:
usename: abhilash
password: Abhi1289lash

## Postman Collection
Postmancollection: `https://api.postman.com/collections/6843786-a6873290-0f44-46e6-8ad9-f20acbe76ae5?access_key=PMAT-01H2954AB2CDSJC06R60H6DV8C`
You can import this collection to test all the API's
