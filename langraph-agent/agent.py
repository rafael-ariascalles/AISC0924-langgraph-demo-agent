from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import create_react_agent

model = ChatOpenAI(model="gpt-4o")
tools = [TavilySearchResults(max_results=5)]
graph = create_react_agent(model, tools)