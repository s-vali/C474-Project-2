#from langchain_community.llms import Ollama
#from langchain.llms import Ollama
#from langchain.chains.LLMChain import LLMChain
from langchain.prompts import PromptTemplate
from langchain_ollama.llms import OllamaLLM
from config.settings import *

'''
Also works:
from memory.memory_manager import memory
llm = Ollama(model="mistral")
general_agent = LLMChain(llm=llm, prompt=prompt, memory=memory)
'''

# Instantiate llm using longchain
llm = OllamaLLM(model=MODEL) # can replace with any model

# Define the template for the LLMs prompt and description of its role
template = """
You are a helpful assistant. 
Context: {context} 
Question: {input} 
Answer: Let's think step by step.
"""

# Instantiate the prompt
prompt = PromptTemplate(input_variables=["input", "context"], template=template)

# Chain everything together
# ... here we can also chain context
general_chain = prompt | llm

# Return LLM server response based on user query input
def handle_general_query(query: str, context: str) -> str: # for now, context="None yet."
    print(f"this is general_agent --> query: '{query}', context: '{context}'")
    return general_chain.invoke({"input": query, "context": context}) # field matches the input_variable defined in the PromptTemplate