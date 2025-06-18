from google.adk.agents import LlmAgent
from dotenv import load_dotenv
from pydantic import BaseModel, Field

load_dotenv()

class OutputStructure(BaseModel):
    question_1 : str = Field(description="Your question 1 should be in in this line.")
    options_1 : str = Field(description="The options for the question 1 should be in this line with each option having its own line.")
    answer_1 : str = Field(description="You answer to question 1 should be in this line.")

    question_2 : str = Field(description="Your question 2 should be in in this line.")
    options_2 : str = Field(description="The options for the question 2 should be in this line with each option having its own line.")
    answer_2 : str = Field(description="You answer to question 2 should be in this line.")

    question_3 : str = Field(description="Your question 3 should be in in this line.")
    options_3 : str = Field(description="The options for the question 3 should be in this line with each option having its own line.")
    answer_3 : str = Field(description="You answer to question 3 should be in this line.")

    question_4 : str = Field(description="Your question 4 should be in in this line.")
    options_4 : str = Field(description="The options for the question 4 should be in this line with each option having its own line.")
    answer_4 : str = Field(description="You answer to question 4 should be in this line.")

    question_5 : str = Field(description="Your question 5 should be in in this line.")
    options_5 : str = Field(description="The options for the question 5 should be in this line with each option having its own line.")
    answer_5 : str = Field(description="You answer to question 5 should be in this line.")

    question_6 : str = Field(description="Your question 6 should be in in this line.")
    options_6 : str = Field(description="The options for the question 6 should be in this line with each option having its own line.")
    answer_6 : str = Field(description="You answer to question 6 should be in this line.")

    question_7 : str = Field(description="Your question 7 should be in in this line.")
    options_7 : str = Field(description="The options for the question 7 should be in this line with each option having its own line.")
    answer_7 : str = Field(description="You answer to question 7 should be in this line.")

    question_8 : str = Field(description="Your question 8 should be in in this line.")
    options_8 : str = Field(description="The options for the question 8 should be in this line with each option having its own line.")
    answer_8 : str = Field(description="You answer to question 8 should be in this line.")

    question_9 : str = Field(description="Your question 9 should be in in this line.")
    options_9 : str = Field(description="The options for the question 9 should be in this line with each option having its own line.")
    answer_9 : str = Field(description="You answer to question 9 should be in this line.")

    question_10 : str = Field(description="Your question 10 should be in in this line.")
    options_10 : str = Field(description="The options for the question 10 should be in this line with each option having its own line.")
    answer_10 : str = Field(description="You answer to question 10 should be in this line.")

quiz_agent = LlmAgent(
    name="quiz_agent",
    model="gemini-2.5-flash",
    description="Quiz Generator Agent",
    instruction="""
    You are a helpful and intelligent assistant that can generate a Multiple Choice Questions (MCQ) quiz based on the user request.

    IMPORTANT: The quiz must follow **exactly** this format for each question:

    Question #1: [Your question]  
    A) [Option A]  
    B) [Option B]  
    C) [Option C]  
    D) [Option D]  
    Answer: [Correct Option Letter]

    INSTRUCTIONS:
    - Generate exactly 10 questions.
    - Use the numbering format `Question #1:` through `Question #10:`.
    - Each question must be followed by exactly **four options**, one per line, starting with **A)**, **B)**, **C)**, and **D)**.
    - Ensure there is a **line break between each option**, and another line break before the answer.
    - After the options, include the correct answer in the format: `Answer: C` (or A, B, or D as appropriate).
    - Add a **blank line** between each full question block (question + options + answer).
    - DO NOT write any intro, explanation, or notes — output **only the quiz**.
    - DO NOT combine multiple options into a single line.

    EXAMPLE:

    Question #1: What is the capital of France?  
    A) Berlin  
    B) Madrid  
    C) Paris  
    D) Rome  
    Answer: C

    **Always provide the output in given format. Also the answer provided should always be in 'Answer: A' format.
    """,
    output_schema=OutputStructure,
    output_key="quiz"
)