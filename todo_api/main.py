# imports
from fastapi import FastAPI,HTTPException
from .tasks import task
from pydantic import BaseModel,Field
from typing import Annotated,Optional,Literal

app=FastAPI()


current_id=1
# pydantic model
class Taskresponse(BaseModel):
    id:int
    task_title:str
    status:str
    
class Taskcreate(BaseModel):
    title:str=Field(...,min_length=1,description="enter title")
    description:Optional[str]=Field(None,description="enter description")

# endpoints

# load 
@app.get('/view')
def view_data():
    return {'tasks':task}

@app.get('/view/{task_id}')
def get_id_task(task_id:int):
    if task_id not in task:
        raise HTTPException(status_code=404,detail='task not found')
    
    return {'task':task[task_id]}

# create

@app.post('/tasks')
def create_task(task_create:Taskcreate): 
    global current_id   
    task_id=current_id
    current_id+=1
    task[task_id]={
        'title':task_create.title,
        'description':task_create.description,
        'status':'pending'
    }
    
    return {
        'task_id':task_id,
        **task[task_id]
    }
    
# delete
@app.delete('/tasks/{task_id}')
def delete_task(task_id:int):
    
    if task_id not in task:
        raise HTTPException(status_code=404,detail="id not found")
    
    deleted_task=task[task_id]
    del task[task_id]
    
    return {
        'message':'deleted successfully',
        'task':deleted_task
    }

# update
class TaskUpdate(BaseModel):
    title:Optional[str]=None
    status:Optional[Literal['pending','completed']]=None
    description:Optional[str]=None
    
@app.patch('/tasks/{task_id}')
def update_task(task_id:int,update_task:TaskUpdate):
    
    if task_id not in task:
        raise HTTPException(status_code=404,detail="id not found")
    
    existing_task=task[task_id]
    update_data=update_task.model_dump(exclude_unset=True)
    
    existing_task.update(update_data)
    
    return {
        'id':task_id,
        **task[task_id]
    }
        
    