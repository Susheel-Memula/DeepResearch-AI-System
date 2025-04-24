from tavily import TavilyClient
import os
def research_agent(query):
    api_key = os.getenv("TAVILY_API_KEY")
    if not api_key:
        raise ValueError("TAVILY_API_KEY not found. Please check your .env file.")
    tavily = TavilyClient(api_key=api_key)
    results = tavily.search(query, search_depth="advanced")
    documents = [r["content"] for r in results["results"]]
    return "\n\n".join(documents)
