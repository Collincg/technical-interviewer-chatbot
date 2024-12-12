# **Guide to `streamlitChatWithMemory.py`**

This script sets up a **Streamlit-based chatbot** for technical interview preparation, leveraging **LangChain** for conversational logic and **Groq LLM** for language model processing. Below is a walkthrough of what each part of the code does.

---

## **1. Importing Dependencies**

```python
from langchain_community.chat_message_histories import StreamlitChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_groq import ChatGroq
import streamlit as st
```

### **Key Libraries**:
- **Streamlit**: Handles the web app interface.
- **LangChain Community & Core**: Used for managing conversation prompts, storing message history, and chaining components.
- **LangChain Groq**: Provides integration with the Groq LLM API.

---

## **2. Streamlit Page Configuration**

```python
st.set_page_config(page_title="Technical Interview Chatbot", page_icon="📖")
st.title("Technical Interview Chatbot")
```

- Configures the Streamlit app's page with a title and icon.
- Displays the app title to users.

---

## **3. Introduction Section**

```python
"""
This is a chatbot designed to simulate a technical interview for Computer/Data Scientists or any adjacent fields. 
This provides you with a less stressful opportunity to prepare for a real technical interview. 
You are welcome to practice behavioral and technical questions.
"""
```

- Provides an introduction to the chatbot's purpose for users.
- Uses triple-quoted strings (`"""`) to add a descriptive block in Streamlit.

---

## **4. API Key Setup**

```python
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
```

- Fetches the **GROQ API Key** from the Streamlit Cloud secrets configuration. 
- The key is required to access the Groq LLM API.

---

## **5. Conversation History Setup**

```python
msgs = StreamlitChatMessageHistory(key="langchain_messages")

if len(msgs.messages) == 0:
    msgs.add_ai_message("Hello, I will be conducting your interveiw today. Can you tell me what field you're applying for? You can also give me a job description and/or questions that you would like practice with!")
```

- **StreamlitChatMessageHistory**: 
  - Stores the conversation history, enabling the chatbot to retain context across user inputs.
  - Messages are tagged as either `human` or `ai` based on who sent them.

- Initializes the conversation with a welcome message if no prior history exists.

---

## **6. Prompt Configuration**

```python
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an expert in the field of Computer Science. You give technical interviews to software engineers, programmers, and intern applicants. Your mission is to ask relevant questions about their experience and technical questions to the applicant. After you can offer feedback about their response. First have them clarify what position they are applying for so you can better guide the interview."),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{question}"),
    ]
)
```

### **What it does**:
- Defines the conversation flow using LangChain's `ChatPromptTemplate`.
- **System Prompt**: Sets the AI's role and behavior (technical interviewer).
- **History Placeholder**: Adds context from prior messages stored in `StreamlitChatMessageHistory`.
- **Human Prompt**: Accepts user input (`{question}`) to customize interactions.

---

## **7. Model Setup**

```python
model = ChatGroq(model="llama-3.1-70b-versatile", api_key=GROQ_API_KEY)
```

- Uses **Groq's `llama-3.1-70b-versatile` model**, which is suitable for conversational and technical Q&A tasks.

---

## **8. Chaining with Memory**

```python
chain_with_history = RunnableWithMessageHistory(
    chain,
    lambda session_id: msgs,
    input_messages_key="question",
    history_messages_key="history",
)
```

### **Purpose**:
- Links the LangChain model (`chain`) with the conversation history stored in `msgs`.
- Ensures that the chatbot retains context from earlier turns in the conversation.

### **Key Parameters**:
- `input_messages_key`: Maps user questions to the input.
- `history_messages_key`: Maps prior messages to provide conversational memory.

---

## **9. Rendering Conversation History**

```python
for msg in msgs.messages:
    st.chat_message(msg.type).write(msg.content)
```

### **Functionality**:
- Iterates through the conversation history (`msgs.messages`) and displays each message in the appropriate format (`human` or `ai`) in the Streamlit interface.

---

## **10. Handling User Input**

```python
if prompt := st.chat_input():
    st.chat_message("human").write(prompt)
    config = {"configurable": {"session_id": "any"}}
    response = chain_with_history.invoke({"question": prompt}, config)
    st.chat_message("ai").write(response.content)
```

### **Steps**:
1. **User Input**: 
   - Uses `st.chat_input()` to capture user messages.
   - Displays the user's input as a `human` message in the interface.

2. **Chain Invocation**:
   - Passes the input (`{question: prompt}`) to the LangChain model.
   - Applies the conversation history and prompt template to generate a response.

3. **AI Response**:
   - Displays the AI's response as a chat bubble (`ai`) in the interface.

---

## **Customizations**

### **Modify Prompts**
Adjust the behavior of the chatbot by editing the `ChatPromptTemplate`:
- Change the **system prompt** to reflect different roles or interview types.
- Add more structured questions in the human prompts for a guided experience.

### **Swap Models**
Use a different model by replacing:
```python
model = ChatGroq(model="your_model_name", api_key=GROQ_API_KEY)
```
---

This guide was written by Collin Graff, and Co-Written by ChatGPT.
