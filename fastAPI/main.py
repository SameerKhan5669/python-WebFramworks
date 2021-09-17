from fastapi import FastAPI

# Creating a fast api instance
app = FastAPI()


# this function handles all requests to the route "/"
@app.get("/")
async def root():
    return {"message": "Hello World"}

# To run: $uvicorn main:app --reload;   