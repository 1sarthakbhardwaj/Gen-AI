import logging

# Set up logging
logging.basicConfig(filename='logs/conversation.log', level=logging.INFO, 
                    format='%(asctime)s - %(message)s')

class ContextManager:
    def __init__(self):
        self.history = []

    def add_message(self, role, content):
        self.history.append({"role": role, "content": content})
        # Log each message added
        logging.info(f"Added {role} message: {content}")

    def get_context(self):
        return self.history

    def clear_context(self):
        self.history = []
        logging.info("Conversation context has been reset.")
