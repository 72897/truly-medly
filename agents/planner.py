from llm.gemini_client import call_llm
from utils.json_parser import extract_json

SYSTEM_PROMPT = """
You are a Planner Agent.

Convert the user task into a step-by-step execution plan.

Return ONLY valid JSON.
No markdown.
No explanation.

Format:

{
  "steps": [
    {
      "id": 1,
      "tool": "GitHubTool | WeatherTool",
      "action": "description",
      "input": {}
    }
  ]
}
"""

def create_plan(task: str) -> dict:
    output = call_llm(SYSTEM_PROMPT, task)
    return extract_json(output)
