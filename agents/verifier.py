from llm.gemini_client import call_llm
from utils.json_parser import extract_json
import json

SYSTEM_PROMPT = """
You are a Verifier Agent.

Validate executor results and return final structured JSON.
Return ONLY JSON.
"""

def verify(task: str, executor_output: list) -> dict:
    prompt = f"""
Task:
{task}

Executor Output:
{json.dumps(executor_output, indent=2)}
"""

    response = call_llm(SYSTEM_PROMPT, prompt)
    return extract_json(response)
