
# Cryptocurrency Chatbot with LLaMA Model Integration

This project is an AI-powered chatbot that leverages the **LLaMA 3.1 8B model from Together AI** to engage in conversations and answer queries about cryptocurrency prices. The chatbot is designed to handle multi-turn conversations, recognize cryptocurrency-related questions, and provide accurate real-time data from the CoinGecko API. It maintains context across interactions, allowing for seamless and coherent conversations.

## Features

- **Multi-Turn Conversation**: Maintains conversation history to provide context-aware responses across multiple interactions.
- **Cryptocurrency Price Fetching**: Detects and responds to cryptocurrency-related queries using the CoinGecko API.
- **Language Translation**: Translates user input to English, ensuring consistent system responses in English.
- **Reset Command**: Users can reset the conversation context with a simple command (`reset`).
- **Caching and Rate Limiting**: Implements caching and rate limiting for API calls to optimize performance and reduce dependency on external services.

## Setup Instructions

Clone the repository and navigate into the project directory:

```bash
git clone https://github.com/yourusername/crypto-chatbot.git
cd crypto-chatbot
```

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: `venv\Scripts\activate`
```

Install the required Python libraries from `requirements.txt`:

```bash
pip install -r requirements.txt
```

Register on [Together AI](https://www.together.ai/) to obtain an API key. Create a `.env` file in the project root directory and add the API key:

```plaintext
TOGETHER_API_KEY=your_actual_api_key_here
```

Run the chatbot:

```bash
python main.py
```

Type 'exit' to quit the application and 'reset' to clear the conversation history and start fresh.

## Project Structure

```plaintext
crypto_agent/
│
├── src/
│   ├── models/
│   │   └── together_llama.py         # Handles LLaMA model integration and conversation flow
│   ├── utils/
│   │   ├── context_manager.py        # Manages conversation context
│   │   ├── crypto_api.py             # Fetches cryptocurrency prices with caching and rate limiting
│   │   └── language_manager.py       # Manages language translation for input messages
│   └── __init__.py                   # Optional; helps Python recognize this as a package
├── data/                             # Placeholder for any data files if needed
├── logs/
│   └── conversation.log              # Log file for conversations and errors
├── .env                              # Stores API keys securely
├── .gitignore                        # Specifies files to exclude from version control
├── README.md                         # Project documentation and usage instructions
└── main.py                           # Main script to run the chatbot
```

## Prompt Engineering Approach

- **Context Management**: The chatbot uses a `ContextManager` to keep track of the conversation history, enabling coherent multi-turn conversations.
- **Translation Consistency**: User messages are translated to English to ensure that all system responses remain in English, regardless of input language.
- **Cryptocurrency Detection**: Regex-based pattern detection is used to recognize and respond to cryptocurrency-related queries without sending unnecessary requests to the model.

## Example Conversations

**Example 1: General Question**

```plaintext
You: What is the capital of France?
LLaMA Model: The capital of France is Paris.
```

**Example 2: Cryptocurrency Price Query**

```plaintext
You: What is the price of Bitcoin?
LLaMA Model: The current price of Bitcoin in USD is 45000.
```

**Example 3: Multi-Turn Conversation**

```plaintext
You: What is the capital of France?
LLaMA Model: The capital of France is Paris.
You: What is the population?
LLaMA Model: The population of Paris is approximately 2.1 million.
```

**Example 4: Reset Command**

```plaintext
You: reset
LLaMA Model: Conversation context has been reset. How can I help you?
```

## Assumptions and Limitations

**Assumptions**

- Users have registered with Together AI and have a valid API key.
- The CoinGecko API is available and does not limit frequent requests.

**Limitations**

- **API Rate Limits**: The application uses caching and rate limiting to manage API requests, but extensive use could still hit limits.
- **Language Translation Accuracy**: While Google Translate is used for language translation, nuances in language might not always be perfectly captured.
- **Context Reset**: The context is reset if the application is restarted, meaning previous conversation history won’t persist between sessions.

## Logs and Troubleshooting

- **Logs**: All conversation history and errors are logged in `logs/conversation.log`.
- **Error Handling**: If errors occur (e.g., issues with API calls), the bot logs these errors and provides helpful feedback to the user.

This README provides a comprehensive guide for setting up, using, and understanding the project structure and flow. Follow these instructions for smooth installation and operation. If you encounter any issues, refer to the logs or documentation for troubleshooting.
