import streamlit as st 
from quiz_generator import get_quiz
import asyncio 
import json

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
        st.session_state["quiz_data"] = json.loads(agent_output)

        for i in range(1, 11):
            st.session_state.pop(f"q{i}", None)
        
        st.session_state["submitted"] = False

if "quiz_data" in st.session_state:
    data = st.session_state["quiz_data"]

    for i in range(1,11):
        q_key = f"question_{i}"
        o_key = f"options_{i}"
        a_key = f"answer_{i}"

        options_str = data[o_key].split("\n")

        st.subheader(data[q_key])
        st.radio(label = "", options=options_str, key= f"q{i}")

    if not st.session_state.get("submitted", False):
        if st.button("Submit"):
            score = 0

            for i in range(1, 11):
                selected = st.session_state.get(f"q{i}", "")
                if len(data[f"answer_{i}"]) > 1:
                    correct_letter = data[f"answer_{i}"].split(":")[1].strip()
                else:
                    correct_letter = data[f"answer_{i}"]

                selected_letter = selected.split(")")[0].strip()

                if correct_letter == selected_letter:
                    score += 1
                
            
            st.session_state["submitted"] = True
            st.session_state["score"] = score

if st.session_state.get("submitted", False):
    st.success(f"You got {st.session_state['score']}/10.")

    with st.expander("Show Correct Answer"):
        for i in range(1, 11):
            if len(data[f"answer_{i}"]) > 1:
                correct_letter = data[f"answer_{i}"].split(":")[1].strip()
            else:
                correct_letter = data[f"answer_{i}"]
            correct_option = [opt for opt in data[f'options_{i}'] if opt.startswith(correct_letter)][0]
            st.markdown(f"**{data[f'question_{i}']}**\n\nCorrect Answer: {correct_option}")
        
        

        





