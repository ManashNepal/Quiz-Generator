from google.genai import types
from session import initialize
from session import USER_ID, SESSION_ID

async def get_quiz(user_input):

    user_message = types.Content(
        role="user", parts=[types.Part(text=user_input)]
    )

    runner = initialize()

    agent_output = ""

    for event in runner.run(user_id=USER_ID, session_id=SESSION_ID, new_message=user_message):
        if event.is_final_response():
            if event.content and event.content.parts:
                agent_output = event.content.parts[0].text
    
    return agent_output