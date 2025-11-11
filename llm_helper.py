from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq

load_dotenv()
GROQ_API_KEY = "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"
llm = ChatGroq(groq_api_key=GROQ_API_KEY,model_name="openai/gpt-oss-safeguard-20b")

if __name__ == "__main__":
    response = llm.invoke("what are the two main ingradients in chai?")

    print(response.content)
