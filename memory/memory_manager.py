from langchain.memory import ConversationBufferMemory

# Initialize memory for multi-turn conversations
memory = ConversationBufferMemory(return_messages=True)