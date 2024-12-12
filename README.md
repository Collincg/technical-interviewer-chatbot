# Technical Interviewer Chatbot

You can use the chatbot here [Technical Interview Chatbot](https://egbq4q5zwmmp2ildkdmmde.streamlit.app/)! 

This project is a **Technical Interview Chatbot** designed to simulate a technical interview environment for individuals in the fields of Computer/Data Science and related areas. By using this chatbot, you can practice both behavioral and technical questions in a stress-free setting. The chatbot leverages the **Groq LLM** for language model processing, **LangChain** for managing prompts and conversation history, and **Streamlit** for the frontend interface.

---
### A preview of the StreamLit User Interface:
<img width="754" alt="Screenshot 2024-12-12 at 12 55 47 PM" src="https://github.com/user-attachments/assets/a16bd0b5-d0c6-483d-8b37-7c685bb3e0e8" />

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
- **LangChain** is used to manage conversation flow and memory. See this guide on their website to learn more [Build a Chatbot | 🦜️🔗 LangChain](https://python.langchain.com/docs/tutorials/chatbot/).
- A **GROQ API Key** (or any preferred API key) to use the AI model (this is stored securely using Streamlit secrets).
- Some basic and intuitive **StreamLit** commands are used.

---

## Recommended Setup

1. **Virtual Environment**: Create a virtual environment to manage dependencies:
   ```bash
   python -m venv chatbot_env
   source chatbot_env/bin/activate  # On Windows: chatbot_env\Scripts\activate
   pip install -r requirements.txt
   ```
2. See the `requirements.txt` to setup necessary packages.

2. **GROQ API Key**: visit [GroqCloud](https://console.groq.com/keys) to create and use a free API key in your project.

3. **Deployment**: Deploy the app using StreamLit Cloud for easy access.
   - When creating a new project on StreamLit Cloud, you will see an option to simply connect a GitHub repository and choose the main file. StreamLit will handle the rest!
   - Before clicking "Deploy", make sure to visit the advanced settings:
     
       <img width="885" alt="Screenshot 2024-12-12 at 12 06 32 PM" src="https://github.com/user-attachments/assets/93ab1d61-b2dd-499e-a359-286093f009b3" />
   - Here you will need to enter your API key with the correct format below. "Secrets" is StreamLit's way of securly attaching your API key to your project.
     
       <img width="707" alt="Screenshot 2024-12-12 at 12 08 23 PM" src="https://github.com/user-attachments/assets/cc816f7f-2fb4-4b34-97f2-5e1a12ceae7b" />

   - If StreamLit still can't access the API key after deployment, find advanced settings again on the running website and double check the "Secrets" to ensure your API is present and       correctly formated. 
---

## Code Explanation

The code is organized as follows:

1. **User Interaction**: 
   - Users interact with the chatbot through a Streamlit web interface.
   - A memory component stores the context of the conversation using `StreamlitChatMessageHistory`.

2. **Chat Logic**:
   - The chatbot uses LangChain and GROQ's `llama-3.1-70b-versatile` model to process and generate responses.
   - The interview simulation is guided by a prompt that ensures relevance to the user's chosen field.

3. **See `streamlitChatWithMemory.py` for a deeper understanding**

---

### Contributors

- **Collin Graff**  
  - Role: Lead Developer  
  - Contributions: Concept design, coding, and deployment.

- **David Robert**  
  - Role: Assistant Developer  
  - Contributions: Code improvements, testing, and troubleshooting.
