from fastapi import FastAPI

import random

app = FastAPI()

# Example to use : a To-do list application

# Lesson 1: Routes
# The routes are the links in which you add to your application, and how should it respond based on
# those routes. You can create routes to handle different interactions of the user.

# Note: This is handling HTTP requests

# Example with routes:
# We'll need different routes to ad or view the to-do items on the list


#Our to-do items list:
itemsList = ["APPLE", "SODA"]


@app.get("/")
def root():
    return{"Hello":"World"}


# Terminal:
# curl -X POST -H "Content-Type: application/json" 'http://127.0.0.1:8000/myPostPath?item=x'
@app.post("/myPostPath") #You create a path, with any name you want (doesn't really matter)
def create_item(item: str): #Create a method (by default is async) of any name that the task will preform going to that path
    itemsList.append(item) #Do THIS when path is executed
    return itemsList #return what you prefer to return

# Terminal:
# curl -X GET http://127.0.0.1:8000/myPostPath/INTEGER
@app.get("/myPostPath/{an_item_id}") #Based on the same path to access your list, which is just a best practice (not necessary), then add another path to specify a variable to use for the method
def get_item(an_item_id: int) -> str:
    item = itemsList[an_item_id]
    return item

#Note: You are only using reference to the actual memory of your program





