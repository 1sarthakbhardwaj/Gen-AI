# app.py
import gradio as gr
from chatbot import chatbot_conversation

# Define the function that Gradio will call
def respond_to_user(user_message, history, thread_id):
    # Get the bot's response from the chatbot backend
    response = chatbot_conversation(user_message, thread_id)
    
    # Update the history with both the user's message and bot's response
    history.append((user_message, response))
    
    # Return the updated conversation history and thread ID
    return history, thread_id

# Create the Gradio interface
def create_interface():
    with gr.Blocks() as demo:
        # Title
        gr.Markdown("# LangChain Chatbot with Groq API")

        # Thread ID to maintain conversation context
        thread_id = gr.State("unique_thread_id")

        # Input text box for user message
        user_message = gr.Textbox(placeholder="Enter your message...", label="Your Message")

        # Display the conversation log
        chatbot_output = gr.Chatbot(label="Conversation")

        # Button to submit the user message
        submit_btn = gr.Button("Submit")

        # Clear button to reset the conversation
        clear_btn = gr.Button("Clear Conversation")

        # Event handler for submitting the message
        submit_btn.click(respond_to_user, inputs=[user_message, chatbot_output, thread_id], outputs=[chatbot_output, thread_id])

        # Event handler for clearing the conversation
        clear_btn.click(lambda: None, None, chatbot_output, queue=False)

    return demo

if __name__ == "__main__":
    # Launch the Gradio app with public sharing enabled
    create_interface().launch(share=True)
