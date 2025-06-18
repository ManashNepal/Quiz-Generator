import streamlit as st 
from quiz_generator import get_quiz
import asyncio 

st.set_page_config(page_title="QUIZ", page_icon=":100:")
st.header("Generate MCQ QUIZ on any topic! :1234:")

user_input = st.text_input("Enter your prompt:")

def run_async(coro):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    return loop.run_until_complete(coro)

if st.button("Generate"):
    with st.spinner("Generating"):
        agent_output = run_async(get_quiz(user_input=user_input))
        st.header("Generated QUIZ:")
        st.write(agent_output)




