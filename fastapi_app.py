from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import uvicorn

# Initialize the FastAPI application
app = FastAPI(title="FastAPI Demo")

# Point FastAPI to the same templates directory used by Flask
templates = Jinja2Templates(directory="templates")


# Define the expected JSON request body using a Pydantic model.
# FastAPI automatically validates incoming JSON against this schema
# and generates interactive API docs at /docs.
class GreetRequest(BaseModel):
    name: str = "World"


# 1. GET endpoint: Serves the main HTML page when visiting http://localhost:8000/
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Render the home page for the API demo."""
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"title": "FastAPI Demo"},
    )


# 2. POST endpoint: Accepts a validated GreetRequest JSON body and returns JSON
@app.post("/api/greet")
async def greet(payload: GreetRequest):
    """
    Example POST endpoint. FastAPI automatically parses and validates the
    JSON body into `payload`, and serializes the returned dictionary to JSON.
    """
    return {
        "message": f"Hello, {payload.name}!",
        "received": payload.model_dump(),
    }


if __name__ == "__main__":
    # Run the Uvicorn ASGI server on http://localhost:8000
    uvicorn.run("fastapi_app:app", host="127.0.0.1", port=8000, reload=True)
