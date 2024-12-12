# Technical Interviewer Chatbot

This project is a **Technical Interview Chatbot** designed to simulate a technical interview environment for individuals in the fields of Computer/Data Science and related areas. By using this chatbot, you can practice both behavioral and technical questions in a stress-free setting. The chatbot leverages the **Groq API** for language model processing, **LangChain** for managing prompts and conversation history, and **Streamlit** for the frontend interface. You can checkout the website here [Technical Interview Chatbot](https://egbq4q5zwmmp2ildkdmmde.streamlit.app/)! 

---

## Features

- **Groq API**: Utilizes Groq's advanced language models for generating interview questions, processing user responses, and providing feedback.
- **LangChain**: 
  - Manages the conversation flow and integrates memory using `LangChainCommunity` and `LangChainCore`.
  - Ensures that the chatbot retains context across multiple turns of the conversation.
- **Streamlit Frontend**: Provides an interactive web-based interface for users to engage with the chatbot.

---

## Prerequisites

- Basic knowledge of **Python** programming.
- **LangChain** is used to manage conversaiton flow and memory. See this guide on their website to learn more [Build a Chatbot | 🦜️🔗 LangChain](https://python.langchain.com/docs/tutorials/chatbot/).
- A **GROQ API Key** (or any preferred API key) to use the AI model (this is stored securely using Streamlit secrets).
- Some basic and intuitive **StreamLit** commands are used.
- Access to **Streamlit Cloud** for deployment (optional).

---

## Recommended Setup

1. **Virtual Environment**: Create a virtual environment to manage dependencies:
   ```bash
   python -m venv chatbot_env
   source chatbot_env/bin/activate  # On Windows: chatbot_env\Scripts\activate
   pip install -r requirements.txt
   ```
2. See the `requirements.txt` to setup necessary packages.

2. **GROQ API Key**: Store your GROQ API key securely in `secrets.toml` for Streamlit Cloud.

3. **Deployment**: Deploy the app using Streamlit Cloud for easy access.

## Code Explanation

The code is organized as follows:

1. **User Interaction**: 
   - Users interact with the chatbot through a Streamlit web interface.
   - A memory component stores the context of the conversation using `StreamlitChatMessageHistory`.

2. **Chat Logic**:
   - The chatbot uses LangChain and GROQ's `llama-3.1-70b-versatile` model to process and generate responses.
   - The interview simulation is guided by a prompt that ensures relevance to the user's chosen field.

3. **Real-Time Feedback**:
   - The chatbot provides feedback on user responses to help improve interview performance.

## How to Use the Website

1. Visit the deployed website [Insert Website Link Here].
2. Enter the field or job description you're preparing for.
3. Answer the chatbot's questions as if you were in a real interview.
4. Review the feedback provided to refine your answers.

## Screenshots

Below are screenshots of the Streamlit Cloud interface showcasing the app:

### Home Page
![Home Page Screenshot](path/to/homepage_screenshot.png)

### Chat Interface
![Chat Interface Screenshot](path/to/chat_interface_screenshot.png)

---

Feel free to customize this further or let me know if you'd like help refining or expanding on any sections!

