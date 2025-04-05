'''
from fastapi import FastAPI, HTTPException
from langchain.memory import ConversationBufferMemory
from agents.router import route_query

# Initialize FastAPI app
app = FastAPI()

# Initialize memory for multi-turn conversations
memory = ConversationBufferMemory(return_messages=True)

# Main chatbot logic
@app.post("/chat")
def chat(input_text: str):
    """
    Handles multi-turn conversations with context awareness.
    :param input_text: User's input text.
    :return: Chatbot's response.
    """
    try:
        # Retrieve conversation history to provide context
        conversation_history = memory.load_memory_variables(inputs={}).get("history", [])

        # Route the query to the appropriate agent
        response = route_query(query=input_text, context=conversation_history)

        # Store the conversation in memory
        memory.save_context({"input": input_text}, {"output": response})

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
'''