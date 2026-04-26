# TODO-API

A simple backend API built using FastAPI that supports full CRUD (Create, Read, Update, Delete) operations for managing tasks.

##🚀 Features
-Create a new task
-Get all tasks
-Get a task by ID
-Update task (partial update using PATCH)
-Delete a task

##🛠️ Tech Stack
-Python
-FastAPI
-Uvicorn

##📌 API Endpoints
- Create Task
POST /tasks
-Get All Tasks
GET /tasks
-Get Task by ID
GET /tasks/{task_id}
-Update Task
PATCH /tasks/{task_id}
-Delete Task
DELETE /tasks/{task_id}

##⚠️ Note
-Data is stored in-memory (Python dictionary)
-Data will reset when the server restarts
