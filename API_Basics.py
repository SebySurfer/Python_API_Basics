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


from fastapi import FastAPI

app = FastAPI()



