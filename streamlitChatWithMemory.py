# Use: streamlit run streamlitChatWithMemory.py if you're testing this before a StreamLit Cloud deployment

from langchain_community.chat_message_histories import StreamlitChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_groq import ChatGroq
import streamlit as st


st.set_page_config(page_title="Technical Interview Chatbot", page_icon="📖")
st.title("Technical Interview Chatbot")

"""
This is a chatbot designed to simulate a technical interview for Computer/Data Scientists or any adjacent fields. 
This provides you with a less stressful opportunity to prepare for a real technical interview. 
You are welcome to practice behavioral and technical questions.
"""

GROQ_API_KEY = st.secrets["GROQ_API_KEY"]


# Set up memory
msgs = StreamlitChatMessageHistory(key="langchain_messages")

if len(msgs.messages) == 0:
    msgs.add_ai_message("Hello, I will be conducting your interveiw today. Can you tell me what field you're applying for? You can also give me a job description and/or questions that you would like practice with!")


# Set up the LangChain, passing in Message History
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an expert in the field of Computer Science. You give technical interviews to software engineers, programmers, and intern applicants. Your mission is to ask relevant questions about their experience and technical questions to the applicant. After you can offer feedback about their response. First have them clarify what position they are applying for so you can better guide the interview."),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{question}"),
    ]
)

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






