# Use: streamlit run streamlitChatWithMemory.py

from langchain_community.chat_message_histories import StreamlitChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_groq import ChatGroq


import streamlit as st

import os
from dotenv import load_dotenv

# Carga las variables desde el archivo .env
load_dotenv()

# Ahora puedes acceder a las variables de entorno
LANGCHAIN_TRACING_V2 = os.getenv('LANGCHAIN_TRACING_V2')
LANGCHAIN_API_KEY = os.getenv('LANGCHAIN_API_KEY')
GROQ_API_KEY = os.getenv('GROQ_API_KEY')

st.set_page_config(page_title="StreamlitChatMessageHistory", page_icon="📖")
st.title("📖 StreamlitChatMessageHistory")

"""
A basic example of using StreamlitChatMessageHistory to help LLMChain remember messages in a conversation.
The messages are stored in Session State across re-runs automatically. You can view the contents of Session State
in the expander below. View the
[source code for this app](https://github.com/langchain-ai/streamlit-agent/blob/main/streamlit_agent/basic_memory.py).
"""

# Set up memory
msgs = StreamlitChatMessageHistory(key="langchain_messages")


if len(msgs.messages) == 0:
    msgs.add_ai_message("Hello, I will be conducting your interveiw today. Can you tell me what field you're applying for?")

view_messages = st.expander("View the message contents in session state") # comment this out for message display

# Set up the LangChain, passing in Message History

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an expert in the field of Computer Science. You give technical interviews to software engineers, programmers, and intern applicants. Your mission is to ask relevant questions about their experience and technical questions to the applicant. After you can offer feedback about their response. First have them clarify what position they are applying for so you can better guide the interview."),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{question}"),
    ]
)

#chain = prompt | ChatGroq(api_key=groq_api_key)
# model = ChatGroq(model="llama3-8b-8192", api_key=GROQ_API_KEY)
# model = ChatGroq(model="llama3-groq-70b-8192-tool-use-preview", api_key=GROQ_API_KEY)
model = ChatGroq(model="llama-3.1-70b-versatile", api_key=GROQ_API_KEY)
chain = prompt | model
chain_with_history = RunnableWithMessageHistory(
    chain,
    lambda session_id: msgs,
    input_messages_key="question",
    history_messages_key="history",
)

# Render current messages from StreamlitChatMessageHistory
for msg in msgs.messages:
    st.chat_message(msg.type).write(msg.content)

# If user inputs a new prompt, generate and draw a new response
if prompt := st.chat_input():
    st.chat_message("human").write(prompt)
    # Note: new messages are saved to history automatically by Langchain during run
    config = {"configurable": {"session_id": "any"}}
    response = chain_with_history.invoke({"question": prompt}, config)
    st.chat_message("ai").write(response.content)

# Draw the messages at the end, so newly generated ones show up immediately
# this as well for history
with view_messages:
    """
    Message History initialized with:
    ```python
    msgs = StreamlitChatMessageHistory(key="langchain_messages")
    ```

    Contents of `st.session_state.langchain_messages`:
    """
    view_messages.json(st.session_state.langchain_messages)





