from langchain.prompts import PromptTemplate
#from langchain.llms import Ollama
from langchain_ollama.llms import OllamaLLM
#from langchain_community.llms import Ollama

llm = OllamaLLM(model="mistral")

prompt = PromptTemplate(input_variables=["input"], template="You are a helpful assistant. Answer the following: {input}")

chain = prompt | llm

def handle_general_query(query: str) -> str:
    print(query)
    return chain.invoke(input=query)

