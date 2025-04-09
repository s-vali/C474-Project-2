from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.schema import Document
from datetime import datetime
from collections import deque

class VectorizedMemory:
    def __init__(self, buffer_size=5):
        self.embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        self.vector_store = Chroma(
            embedding_function=self.embedding,
            collection_name="conversation_memory",
            persist_directory="./chroma_db"
        )
        self.buffer = deque(maxlen=buffer_size * 2)  # Store pairs of input/output

    def save_context(self, input_data: dict, output_data: dict):
        user_input = input_data.get("input", "")
        bot_output = output_data.get("output", "")
        
        # Save to vector store
        user_doc = Document(
            page_content=user_input,
            metadata={"type": "user", "timestamp": datetime.now().isoformat()}
        )
        bot_doc = Document(
            page_content=bot_output,
            metadata={"type": "bot", "timestamp": datetime.now().isoformat()}
        )
        self.vector_store.add_documents([user_doc, bot_doc])
        
        # Save to buffer
        self.buffer.append({"type": "user", "content": user_input})
        self.buffer.append({"type": "bot", "content": bot_output})

    def load_memory_variables(self, inputs: dict) -> dict:
        query = inputs.get("input", "")
        recent_messages = [f"{msg['type']}: {msg['content']}" for msg in self.buffer]
        
        if query:
            # Get relevant context from vector store
            docs = self.vector_store.similarity_search(query, k=3)
            vector_messages = [f"{doc.metadata['type']}: {doc.page_content}" for doc in docs]
            
            # Combine and deduplicate
            combined = list(dict.fromkeys(vector_messages + recent_messages))
            return {"history": "\n".join(combined)}
        
        return {"history": "\n".join(recent_messages)}  
