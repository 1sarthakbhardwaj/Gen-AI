# import llm 
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()


# load the llm and its API key
os.envorn["GROQ_API_KEY"] = os.getenv('GROQ_API_KEY')
llm = ChatGroq(model="llama3-8b-8192")
