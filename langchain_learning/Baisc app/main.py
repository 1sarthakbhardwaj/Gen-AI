from dotenv import load_dotenv
import os
# mainimports
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


# load Groq API key

load_dotenv()

# Initialize Groq Model
groq_api_key = os.getenv('GROQ_API_KEY')
model = ChatGroq(model="llama-3.1-70b-versatile")

# Prompt template to ask questions
prompt_template = ChatPromptTemplate.from_messages([
    ("system","Answer the user's question:"),
    ("user","{question}"),
])

# Output Parser to extract the answer 
parser = StrOutputParser()

def get_answer(question: str) -> str:
    chain = prompt_template | model | parser
    result = chain.invoke({"question": question})
    return result

