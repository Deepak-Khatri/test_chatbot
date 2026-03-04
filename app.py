import streamlit as st
from lg_backend import chat_bot
from langchain_core.messages import HumanMessage
#st.session_state =dt
config1={'configurable':{'thread_id':'thread1'}}

if 'message_hist' not in st.session_state:
    st.session_state['message_hist']=[]

for message in st.session_state['message_hist']:
    with st.chat_message(message['role']):
        st.text(message['content'])


user_input=st.chat_input("Please type here to chat")
if user_input:
    st.session_state['message_hist'].append({'role':'user','content':user_input})
    with st.chat_message('human'):
        st.text(user_input)
    cb_response=chat_bot.invoke({'messages':[HumanMessage(content=user_input)]},config=config1)
    ai_msg=cb_response['messages'][-1].content
    st.session_state['message_hist'].append({'role':'ai','content':ai_msg})
    with st.chat_message('ai'):
        st.text(ai_msg)
    