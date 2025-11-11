from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(groq_api_key=os.getenv("GROQ_API_KEY"),model_name="openai/gpt-oss-safeguard-20b")

if __name__ == "__main__":
    response = llm.invoke("what are the two main ingradients in chai?")
    print(response.content)