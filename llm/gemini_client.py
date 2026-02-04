import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

def call_llm(system_prompt: str, user_prompt: str) -> str:
    prompt = f"""
{system_prompt}

User Input:
{user_prompt}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text
