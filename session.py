from uuid import uuid4 
from dotenv import load_dotenv 
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from uuid import uuid4
from agent import quiz_agent

load_dotenv()

APP_NAME = "MCQ Quiz"
USER_ID = "manash_nepal"
SESSION_ID = str(uuid4())

def initialize():
    session_service = InMemorySessionService()

    session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID
    )

    runner = Runner(
        app_name=APP_NAME,
        agent=quiz_agent,
        session_service=session_service
    )

    return runner


