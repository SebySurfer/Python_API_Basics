from fastapi import FastAPI, HTTPException

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
def get_item(an_item_id: int) -> str: #Really the 'an_item_id' or using 'id' is just a conventional way to name it (good practice). You can also name it 'Var', or whatever you like
    item = itemsList[an_item_id]
    return item

#Note: You are only using reference to the actual memory of your program


# Lesson 2: Raising Errors
# Whenever we encoutner errors, a lot of times it is logical to understand why an error occured (Ex: using str instead of int)
# But its not very useful to see that the response doesnt specify why, leaving users question what went wrong
# So we need to see how to rasise very useful errr messages, so that when your developing the app, you can debug it and figure out what went wrong.

# How to configure these errors:
# There's a universal set of http response codes that you can use and everybody will understand
# Link: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
# We will import 'HTTPException' from FastAPI

#Lets replicate the same get request from the previous api, but with the error exception implemented

# Terminal:
# curl -X GET http://127.0.0.1:8000/myErrorExample/INTEGER
@app.get("/myErrorExample/{index}")
def get_item(index: int) -> str:
    if index < len(itemsList): #If you pass an integer lower than the total length, its truthy, if not its falsy
        return itemsList[index]
    else:
        raise HTTPException(status_code=404, detail=f"Item {index} is too big senpai") # HTTPException has the strict field 'status_code' implemented, and has an optional field 'detail' to display your own message
        #The exception code you can find in the universal glossary,
        # where you can find the standard that meets the criteria which will result in error






