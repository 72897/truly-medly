


import json
import re

def extract_json(text: str):
    """
    Extract valid JSON from LLM responses.
    Handles markdown, extra text, and formatting.
    """

    if not text:
        raise ValueError("LLM returned empty response")

   
    text = re.sub(r"```json", "", text)
    text = re.sub(r"```", "", text)

    
    match = re.search(r"\{.*\}", text, re.DOTALL)

    if not match:
        raise ValueError("No JSON found in LLM response")

    json_text = match.group(0)

    return json.loads(json_text)
