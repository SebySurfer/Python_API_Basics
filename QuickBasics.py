from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Example to use : a To-do list application

# Lesson 1: Routes
# The routes are the links in which you add to your application, and how should it respond based on
# those routes. You can create routes to handle different interactions of the user.

# Note: This is handling HTTP requests

# Example with routes:
# We'll need different routes to ad or view the to-do items on the list


#Our to-do items list:
itemsList = []


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


# Lesson 3: Making models: JSON Requests
# Whenever we want to use more complex data structures, instead of just the typical data types, we can pass in JSON formats instead
# So to do this, we can use "Pydantic" models, which allows you to structure your data into more complex ones (being the json format) and also provide additional validation (shows any errors in terminals if not passed in correctly

# class <Name> (Basemodel):
    # <Variable x >: <DataType> = <Default Value>
    # etc...

#Note: Default values are optional, if you dont have one, it is required to pass in a variable or else it will pronounce an error in terminal (being the validation we just talked about)
class ItemObjectName(BaseModel): #You can make any name for the model, i put "ItemObjectName" as an example.
    item_title: str #Necessary to pass value
    check_mark: bool = False #Optional to pass value, and if not, put to False

#When you use a modeled object as part of an agrument within an api, its gong to expect that to be in the JSON payload of the request
@app.post("/myPostPathObject")
def create_object(item: ItemObjectName):
    itemsList.append(item)
    return itemsList
# To send an 'ItemObjectName' data, we need to send the following way in the terminal:
# curl -X POST -H "Content-Type: application/json" -d '{"item_title":"x"}' http://127.0.0.1:8000/myPostPathObject



# Lesson 4: Response models
# For every api, at times we have a function and return a model.
# Sometimes, we want the response (being the return) to be different from the whole model, because:
    # how it'll be used in our front end
    # We only need some parts of data from the model
    # We dont want it to pass sensitive data
    # We dont want it to pass unecessary data
    # etc

# How can we make this modification to our model, without having to change it ? "Response Models"

# You can return a complex or nested data strusture from your funtion,, and FastAPI will reshape it to match the response_model
    # Note: You dont strictly have to use the SAME model, as said, we can create personalized models to be returned
# Using response_model allows you to keep your API responses consistent regardless of how the function’s internal data may evolve.

# Example:
# Suppose you add a sensitive field (e.g., password, internal_id) to the model or return dictionary
# for internal logic; the response_model will ensure that only the intended fields are visible to the client.

# Returning a model directly does not guarantee this level of security and consistency. If you inadvertently include a
# sensitive field in your return statement, it will be sent to the client.

class User(BaseModel):
    username: str
    email: str
    password: str #Sensitive field you dont want to expose

class PublicUser(BaseModel):
    username: str
    email: str
    #No password, only public fields

users = [User(username="john_doe", email="john@example.com", password="secret")]


@app.get("/user", response_model=PublicUser) #Once the return statement is executed, FastAPI will model it to the PublicUser
def get_user():
    return users[0] #It returns a full model that includes a password

# Activity: Try removing the 'PublicUser' and see what happens
