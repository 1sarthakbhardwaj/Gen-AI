import streamlit as st
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain_groq import ChatGroq

# Set page configuration
st.set_page_config(page_title="Groq LLM SaaS Playground", page_icon="🤖", layout="wide")

# Custom CSS to enhance the UI
def set_custom_css():
    st.markdown("""
    <style>
    .main {
        background-color: #f5f7fa;
        padding: 20px;
    }
    .chat-container {
        background-color: #ffffff;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    .user-input {
        font-size: 1.1rem;
        padding: 10px;
        background-color: #e0f7fa;
        border-radius: 8px;
        margin-bottom: 10px;
    }
    .ai-response {
        font-size: 1.1rem;
        padding: 10px;
        background-color: #e8f5e9;
        border-radius: 8px;
        margin-bottom: 10px;
    }
    .sidebar .block-container {
        background-color: #f5f7fa;
    }
    </style>
    """, unsafe_allow_html=True)

set_custom_css()

def main():
    st.title("🤖 Groq LLM SaaS Playground")
    st.sidebar.title("⚙️ Application Settings")
    st.sidebar.markdown("Interact with open-source LLMs using Groq API.")

    # Step 1: Prompt for the API Key
    if 'groq_api_key' not in st.session_state:
        st.session_state['groq_api_key'] = ''
        st.session_state['authenticated'] = False

    # Show the API key input only if not authenticated
    if not st.session_state['authenticated']:
        with st.expander("🔑 Enter Your GROQ API Key to Unlock", expanded=True):
            groq_api_key = st.text_input("GROQ API Key", type="password")
            if st.button("Unlock Application"):
                if groq_api_key:
                    st.session_state['groq_api_key'] = groq_api_key
                    st.session_state['authenticated'] = True
                    st.success("API Key authenticated successfully!")
                    st.rerun()
                else:
                    st.error("Please enter a valid API key.")
        return

    # Step 2: Main Chatbot Interface
    st.sidebar.subheader("🤖 Chat Settings")

    # Model selection with more options
    model = st.sidebar.selectbox(
        'Choose a model',
        ['llama3-8b-8192','gemma-7b-it','gemma2-9b-it',
        'llama3-groq-70b-8192-tool-use-preview','llama3-groq-8b-8192-tool-use-preview',
        'distil-whisper-large-v3-en','llama-3.1-70b-versatile','llama-3.1-8b-instant','llama-3.2-11b-text-preview',
        'llama-3.2-11b-vision-preview','llama-3.2-1b-preview','llama-3.2-3b-preview','llama-3.2-90b-text-preview',
        'llama-3.2-90b-vision-preview','llama-guard-3-8b','llama3-70b-8192','whisper-large-v3','whisper-large-v3-turbo',
        'llava-v1.5-7b-4096-preview','mixtral-8x7b-32768']

    )

    conversational_memory_length = st.sidebar.slider(
        'Conversational Memory Length', 1, 10, value=5
    )
    memory = ConversationBufferWindowMemory(k=conversational_memory_length)

    st.markdown("## 💬 Chat with the Model")
    user_question = st.text_area("📝 Ask a question:", placeholder="Type your query here...")

    # Manage session state for chat history
    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []
    else:
        for message in st.session_state.chat_history:
            memory.save_context({'input':message['human']},{'output':message['AI']})

    # Initialize ChatGroq instance
    try:
        groq_chat = ChatGroq(
            model_name=model,
            groq_api_key=st.session_state['groq_api_key']
        )
        conversation = ConversationChain(llm=groq_chat, memory=memory)

        # Handle user question and display response
        if user_question:
            with st.spinner("Thinking..."):
                response = conversation(user_question)
                message = {"human": user_question, "AI": response['response']}
                st.session_state['chat_history'].append(message)
            
            st.write("🤖 ChatBot:", response['response'])

    except Exception as e:
        st.error(f"An error occurred: {e}")

    # Display chat history
    st.markdown("### 📜 Chat History")
    chat_container = st.container()
    with chat_container:
        for message in st.session_state['chat_history']:
            st.markdown(f"*👤 You*: {message['human']}", unsafe_allow_html=True)
            st.markdown(f"*🤖 AI*: {message['AI']}", unsafe_allow_html=True)

    # Sidebar Buttons
    st.sidebar.markdown("---")
    if st.sidebar.button("Clear Chat History"):
        st.session_state['chat_history'] = []
        st.rerun()

    if st.sidebar.button("Log Out"):
        st.session_state['authenticated'] = False
        st.session_state['groq_api_key'] = ''
        st.session_state['chat_history'] = []
        st.rerun()

if __name__ == "__main__":
    main()