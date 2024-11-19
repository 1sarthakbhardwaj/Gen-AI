import streamlit as st
import os
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
    model = st.sidebar.selectbox(
        'Choose a model',
        ['mixtral-8x7b-32768', 'llama2-70b-4096']
    )

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
