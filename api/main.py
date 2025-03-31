from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from agents.router import route_query

app = FastAPI()

# Define the request body model
class ChatRequest(BaseModel):
    message: str

# Define route API endpoint
@app.get("/")
def read_root():
    return {"message": "Multi-Agent Chatbot System is running."}

# Multi-Agent chat endpoint
@app.post("/chat")
def chat_endpoint(request: ChatRequest): # this tells FastAPI to expect a JSON body with a "message" field for user input
    user_message = request.message # extract user input
    response = route_query(query=user_message, context="None yet.") # route to relevant agent
    return {"response": response} # return response to endpoint

# Run the file to open SwaggerUI and query the agents
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)