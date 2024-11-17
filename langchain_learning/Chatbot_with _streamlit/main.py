import streamlit as st
import os
# import groq from Groq
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

def main():
    st.title("Chat with any model in groq")
    st.sidebar.title("select an llm")
    model = st.sidebar.selectbox(
        'Choose a model',
        ['mixtral-8x7b-32768', 'llama2-70b-4096']
    )

    conversational_memory_length = st.sidebar.slider(
        'Conversational memory length', 1, 10, value=5
        )
    
    memory = ConversationBufferWindowMemory(k=conversational_memory_length)

    # adding column for user prompt
    user_question = st.text_area("Ask a question")

    # manage session state
    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []
    else:
        for message in st.session_state['chat_history']:
            if 'human' in message and 'AI' in message:
                memory.save_context({"input": message['human']}, {"output": message['AI']})
            
    groq_chat = ChatGroq(model_name=model)

    conversation = ConversationChain(
        llm=groq_chat,
        memory=memory
    )

    if user_question:
        response = conversation(user_question)
        message = {"human": user_question, "AI": response['response']}
        st.session_state['chat_history'].append(message)
        st.write("ChatBot", response['response'])



if __name__ == "__main__":
    main()