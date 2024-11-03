import os
from dotenv import load_dotenv
from tools import search_tool 
from langchain_groq import ChatGroq
from langchain.agents import initialize_agent, AgentType

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
llm = ChatGroq(groq_api_key = groq_api_key, model = "llama-3.2-11b-text-preview")
research_agent = initialize_agent(tools = [search_tool], 
                                llm = llm, 
                                agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,
                                handle_parsing_errors=True,
                                verbose = True)

use_case_agent = initialize_agent(
    tools=[search_tool],
    llm = llm, 
    agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    handle_parsing_errors=True, 
    verbose = True
)
    
resource_collection_agent = initialize_agent(
    tools=[search_tool],
    llm = llm, 
    agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    handle_parsing_errors=True, 
    verbose = True
)


