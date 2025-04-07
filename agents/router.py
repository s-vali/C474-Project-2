from agents.general_agent import handle_general_query
from agents.ai_agent import handle_ai_query
from agents.admission_agent import handle_admission_query

'''Routing to relevant agent'''

def route_query(query: str, context: []):
    """
    Handle routing to relevant agent to answer user's input

    :param query: user input
    :param context: chat history and query context
    :return: relevant agent response
    """

    temp_str = query.lower()
    if "admission" in temp_str or "concordia" in temp_str or "computer science" in temp_str:
        return handle_admission_query(query, context) # return agent's response
    elif "ai" in temp_str or "artificial intelligence" in temp_str:
        return handle_ai_query(query, context)
    else:
        return handle_general_query(query, context)