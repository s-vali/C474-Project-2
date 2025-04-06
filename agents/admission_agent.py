from langchain.prompts import PromptTemplate
from langchain_ollama.llms import OllamaLLM
from config.settings import *
from utils.knowledge_integration import fetch_wikipedia_summary

'''Admission Agent'''

# Instantiate llm using longchain
llm = OllamaLLM(model=MODEL) # can replace with any model

# Define the template for the LLMs prompt and description of its role
template = """
You are an assistant to answer questions about the admission process to Concordia University's Computer Science program. 
Context: {context} 
Question: {input} 
Answer: Let's think step by step.
"""

# Instantiate the prompt
prompt = PromptTemplate(input_variables=["input", "context"], template=template)

# Chain everything together
# ... here we can also chain context
admission_chain = prompt | llm

# Return LLM server response based on user query input
def handle_admission_query(query: str, context: []) -> str: # for now, context="None yet."
    print(f"this is admission_agent --> query: '{query}', context: '{context}'")

    # Try fetching additional context from Wikipedia
    external_context = fetch_wikipedia_summary(query)
    combined_context = f"{context}\n\n{external_context}" if external_context else context

    return admission_chain.invoke({"input": query, "context": combined_context}) # field matches the input_variable defined in the PromptTemplate