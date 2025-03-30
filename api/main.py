from fastapi import FastAPI
from pydantic import BaseModel
from agents.general_agent import handle_general_query
import uvicorn

app = FastAPI()

# Define the request body model
class ChatRequest(BaseModel):
    message: str

@app.get("/")
def read_root():
    return {"message": "Multi-Agent Chatbot is running."}

@app.post("/chat")
def chat_endpoint(request: ChatRequest): # this tells FastAPI to expect a JSON body with a "message" field
    user_message = request.message
    response = handle_general_query(user_message)
    return {"response": response}

# Run the file to open SwaggerUI and query the LLMs
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)