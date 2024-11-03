from langchain_community.utilities import GoogleSerperAPIWrapper
import os
from langchain_core.tools import Tool

os.environ["SERPER_API_KEY"] = ""
search = GoogleSerperAPIWrapper()
search_tool = Tool(
        name="Intermediate Answer",
        func=search.run,
        description="Use this tool to search in internet",
    )
