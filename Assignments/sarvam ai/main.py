from src.models.together_llama import query_llama_model

if __name__ == "__main__":
    print("Starting conversation with the LLaMA model.")
    print("Type 'exit' to quit or 'reset' to start a new conversation.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        response = query_llama_model(user_input)
        print("LLaMA Model:", response)
