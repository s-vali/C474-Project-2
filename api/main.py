from agents.router import route_query
from fastapi import FastAPI, HTTPException
from memory.memory_manager import VectorizedMemory

'''Multi Turn Chatbot Conversation'''

# Initialize FastAPI app
app = FastAPI()
memory = VectorizedMemory()

# Main chatbot logic
@app.post("/chat")
def chat(input_text: str):
    try:
        # Get context-aware history
        conversation_history = memory.load_memory_variables(
            {"input": input_text}
        ).get("history", "")
        
        # Route query with formatted history
        response = route_query(
            query=input_text,
            context=conversation_history
        )

        # Store conversation
        memory.save_context(
            {"input": input_text},
            {"output": response}
        )

        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint to retrieve conversation history
@app.get("/history")
def get_history():
    """
    Retrieves the conversation history.
    :return: List of past interactions.
    """
    return {"history": memory.load_memory_variables(inputs={}).get("history", [])}