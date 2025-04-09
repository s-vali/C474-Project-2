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
Relevant external knowledge: {knowledge_base}
Question: {input} 
Answer: Let's think step by step.
"""

# Instantiate the prompt
prompt = PromptTemplate(input_variables=["input", "context", "knowledge_base"], template=template)

# Chain everything together
admission_chain = prompt | llm

# Return LLM server response based on user query input
def handle_admission_query(query: str, context: str) -> str:
    """
    Return LLM response based on user query input for Concordia Admissions
    :param query: user query string
    :param context: chatbot history and query context
    :return: agent's response to query
    """

    print(f"THIS IS ADMISSION_AGENT --> query: '{query}', context: '{context}'")

    # Try fetching additional context from Wikipedia
    knowledge = fetch_wikipedia_summary(query)
    print("KNOWLEDGE: ", knowledge)

    return admission_chain.invoke({"input": query, "context": context, "knowledge_base": knowledge or "None"}) # field matches the input_variable defined in the PromptTemplate