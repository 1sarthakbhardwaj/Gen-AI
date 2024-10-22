# chatbot.py
import os
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set Groq API key from the environment variable
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

# Initialize Groq LLM model (Llama3-8b)
model = ChatGroq(model="llama3-8b-8192")

# Define a new state graph to handle the chatbot flow
workflow = StateGraph(state_schema=MessagesState)

# Define the function that will call the Groq model
def call_model(state: MessagesState):
    response = model.invoke(state["messages"])
    return {"messages": response}

# Add the model call node to the workflow graph
workflow.add_edge(START, "model")
workflow.add_node("model", call_model)

# Set up in-memory message persistence using LangGraph's memory saver
memory = MemorySaver()
app = workflow.compile(checkpointer=memory)

# Function to handle user input and invoke the workflow
def chatbot_conversation(user_message: str, thread_id: str):
    # Build the conversation history
    input_messages = [HumanMessage(content=user_message)]
    
    # Define the config for maintaining thread-based conversation
    config = {"configurable": {"thread_id": thread_id}}
    
    # Call the app (workflow) and return the last message
    output = app.invoke({"messages": input_messages}, config)
    return output["messages"][-1].content
