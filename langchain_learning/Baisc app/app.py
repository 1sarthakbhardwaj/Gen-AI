# app.py
import streamlit as st
from main import get_answer

# Streamlit UI elements
st.title("Q&A Bot with LangChain")

# Input field for user's question
question = st.text_input("Enter your question:")

# Button to get the answer
if st.button("Get Answer"):
    if question:
        # Call the get_answer function from main.py
        answer = get_answer(question)
        st.write(f"Answer: {answer}")
    else:
        st.write("Please enter a question.")
