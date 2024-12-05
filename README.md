# Technical Interviewer Chatbot

This repository contains a chatbot designed to simulate a technical interview. The chatbot leverages the **Groq API** for language model processing, **LangChain** for managing prompts and conversation history, and **Streamlit** for the frontend interface. A virtual environment is used to manage dependencies, and the `requirements.txt` file provides an easy way to set up the necessary packages.

---

## Features

- **Groq API**: Utilizes Groq's advanced language models for generating interview questions, processing user responses, and providing feedback.
- **LangChain**: 
  - Manages the conversation flow and integrates memory using `LangChainCommunity` and `LangChainCore`.
  - Ensures that the chatbot retains context across multiple turns of the conversation.
- **Streamlit Frontend**: Provides an interactive web-based interface for users to engage with the chatbot.
- **Conversation Memory**: Retains message history across interactions using `StreamlitChatMessageHistory`.
- **Virtual Environment**: Ensures dependencies are isolated and managed effectively.

---

## Installation and Setup

### Prerequisites

1. **Python 3.9+**: Make sure Python is installed on your system. You can download it from [python.org](https://www.python.org/).
2. **Virtual Environment**: Recommended to avoid polluting your global Python environment.
3. **API Keys**: Create a `.env` file in the root of the project and include the following keys:
   ```env
   LANGCHAIN_TRACING_V2=your_langchain_tracing_v2_key
   LANGCHAIN_API_KEY=your_langchain_api_key
   GROQ_API_KEY=your_groq_api_key

