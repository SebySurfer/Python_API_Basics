# API = allows one piece of software to request data from another and receive a response

# Most APIs interact with data through four main methods, collectively known as CRUD:
    # Create = POST
    # Read = GET
    # Update = PUT/PATCH
    # Delete = DELETE

# By using APIs, you make requests to a server. This is your way of asking the server for data or some action
# The server then processes your request and sends a response.
# This response can tell you if your request was successful by using a status code, or it might include some of the data you've asked for

# JSON (JavaScript Object Notation) = Is the format for structuring data that is mostly used
# Made up of two basic structuresL
    # Objects
    # Arrays

# However, when building APIs, it only means something when its actually accessable online. You're going to need to deploy it, being a hosting platform.

#We will be using the following to create our APIs:
# FastAPI = performance python framework
 # Easy to code
 # Fast to code
 # Ready for production

# Handles all the complex needs of APIs for you:
    # Automatically convert python objects to and from JSON
    # Validate different requests
    # Ensure the correct data is provided

# Run app: uvicorn API_Basics:app --reload

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field #Field allows you to add metadata and customize how fields in your Pydantic models behave
from typing import List, Optional #Optional means that you dont have to pass in the value when you create the mdodel
from uuid import UUID, uuid4  # Stands for "Unique identifier", where it always guarantees a unique ID

app = FastAPI()


# This class will represent the objects that we'll be passing around this API
class Task(BaseModel):
    id: UUID = Field(default_factory=uuid4)  # Generates a new UUID for each instance
    title: str
    description: Optional[str] = None
    completed: bool = False

tasksList = [] #Techncally you would connect this to a real database

# Create
@app.post("/tasks/", response_model=Task)
def create_task(task: Task):
    tasksList.append(task)
    return task

#Read
@app.get("/tasks/", response_model=List[Task])
def read_task():
    return tasksList


#Tip = Doesn't matter if you have the same endpoint, as long as the task request is different

#Read
@app.get("/tasks/{task_id}", response_model=Task)
def read_task(task_id: UUID):
    for task in tasksList:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found stuped")

# Update
@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: UUID, newTask: Task):
    for index, task in enumerate(tasksList):
        if task.id == task_id:
            updated_task = task.copy(update=newTask.dict(exclude_unset=True))
            tasksList[index] = updated_task
            return tasksList
    raise HTTPException(status_code=404, detail="Task not updated cuz not found stuped")

# Delete
@app.delete("/tasks/{task_id}", response_model=Task)
def delete_task(task_id: UUID):
    for index, task in enumerate(tasksList):
        if task.id == task_id:
            tasksList.pop(index)
            return tasksList
    raise HTTPException(status_code=404, detail="Task not deleted cuz not found stuped")
