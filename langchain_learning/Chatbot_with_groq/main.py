from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph

# load_dotenv()
load_dotenv()

model = ChatGroq(model="llama3-8b-8192")

# setting up the Memory and StateGraph

# Define a new state graph
workflow = StateGraph(state_schema=MessagesState)

# Define the function that calls the model


def call_model(state: MessagesState):
    # Pass the entire conversation history to the model
    response = model.invoke(state["messages"])
    return {"messages": response}


# Define the (single) node in the graph\/
#Here, workflow is your StateGraph that manages the conversation flow, and memory is your MemorySaver that keeps track of the conversation history.


workflow.add_edge(START, "model")
workflow.add_node("model", call_model)

# Add memory to persist conversation context
memory = MemorySaver()
app = workflow.compile(checkpointer=memory)


def chat_with_memory():
    # Configuration for memory to track different sessions
    config = {"configurable": {"thread_id": "session1"}}

    print("Chatbot is running. Type 'exit' to stop.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break

        # Wrap the user input in a HumanMessage
        input_messages = [HumanMessage(content=user_input)]

        # Invoke the model with the stored conversation context
        output = app.invoke({"messages": input_messages}, config)
        print(f"Chatbot: {output['messages'][-1].content}")


if __name__ == "__main__":
    chat_with_memory()