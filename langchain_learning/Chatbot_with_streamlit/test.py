import streamlit as st
import os
<<<<<<< HEAD
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain_groq import ChatGroq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def main():
    st.title("Chat with Groq LLM")
    st.sidebar.title("Select an LLM")

    # Model selection
=======
from groq import Groq
import random

from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os 

load_dotenv()

groq_api_key = os.environ['GROQ_API_KEY']

def main():

    st.title("Groq Chat App")

    # Add customization options to the sidebar
    st.sidebar.title('Select an LLM')
>>>>>>> 1f97e2d23df7ef8e011f880358dc67f54efc0e36
    model = st.sidebar.selectbox(
        'Choose a model',
        ['mixtral-8x7b-32768', 'llama2-70b-4096']
    )
<<<<<<< HEAD

    # Conversational memory length selection
    conversational_memory_length = st.sidebar.slider(
        'Conversational Memory Length', 1, 10, value=5
    )

    # Initialize conversation memory
    memory = ConversationBufferWindowMemory(k=conversational_memory_length)

    # Adding column for user input
    user_question = st.text_area("Ask a question:")

    # Manage session state for chat history
    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []

    # Load previous chat history into memory
    for message in st.session_state['chat_history']:
        if 'human' in message and 'AI' in message:
            memory.save_context({"input": message['human']}, {"output": message['AI']})

    try:
        # Initialize Groq chat model
        groq_chat = ChatGroq(model_name=model)

        # Create conversation chain with memory
        conversation = ConversationChain(
            llm=groq_chat,
            memory=memory
        )

        # If user submits a question
        if user_question:
            response = conversation(user_question)
            message = {"human": user_question, "AI": response['response']}
            st.session_state['chat_history'].append(message)
            st.write("🤖 ChatBot:", response['response'])

    except Exception as e:
        st.error(f"An error occurred: {e}")

    # Display chat history
    st.markdown("### Chat History")
    for message in st.session_state['chat_history']:
        st.write(f"👤 **You**: {message['human']}")
        st.write(f"🤖 **AI**: {message['AI']}")

    # Button to clear chat history
    if st.button("Clear Chat History"):
        st.session_state['chat_history'] = []
        st.experimental_rerun()

if __name__ == "__main__":
    main()
=======
    conversational_memory_length = st.sidebar.slider('Conversational memory length:', 1, 10, value = 5)

    memory=ConversationBufferWindowMemory(k=conversational_memory_length)

    user_question = st.text_area("Ask a question:")

    # session state variable
    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []
    else:
        for message in st.session_state['chat_history']:
            if 'human' in message and 'AI' in message:
            memory.save_context({"input": message['human']}, {"output": message['AI']})


    # Initialize Groq Langchain chat object and conversation
    groq_chat = ChatGroq(
            groq_api_key=groq_api_key, 
            model_name=model
    )

    conversation = ConversationChain(
            llm=groq_chat,
            memory=memory
    )

    if user_question:
        response = conversation(user_question)
        message = {'human':user_question,'AI':response['response']}
        st.session_state.chat_history.append(message)
        st.write("Chatbot:", response['response'])

if __name__ == "__main__":
    main()
>>>>>>> 1f97e2d23df7ef8e011f880358dc67f54efc0e36
