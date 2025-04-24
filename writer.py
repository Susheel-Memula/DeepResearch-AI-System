from langchain_openai import ChatOpenAI
import os
def writer_agent(documents):
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found. Please check your file.")
    llm = ChatOpenAI(api_key=api_key, model_name="gpt-4")
    prompt = f"Summarize the following research:\n\n{documents}"
    summary = llm.invoke(prompt) 
    return summary
