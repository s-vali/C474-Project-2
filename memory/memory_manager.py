from langchain.memory import ConversationBufferMemory

'''Chatbot conversation memory'''

# Initialize memory for multi-turn conversations
memory = ConversationBufferMemory(return_messages=True)