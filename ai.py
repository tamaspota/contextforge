import json
import os
from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


PROJECT_SCHEMA = {
    "type": "object",
    "properties": {
        "project": {"type": "string"},
        "area": {"type": "string"},
        "status": {"type": "string"},
        "priority": {"type": "string"},
        "mode": {"type": "string"},
        "next_step": {"type": "string"},
        "blocker": {"type": "string"},
        "review_cycle": {"type": "string"},
        "note": {"type": "string"},
        "current_state": {"type": "string"},
    },
    "required": [
        "project",
        "area",
        "status",
        "priority",
        "mode",
        "next_step",
        "blocker",
        "review_cycle",
        "note",
        "current_state",
    ],
    "additionalProperties": False,
}


def parse_brain_dump(text):
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=[
            {
                "role": "system",
                "content": (
                    "You convert messy project notes into structured project state. "
                    "Return only valid structured data. "
                    "Use short, practical values."
                ),
            },
            {
                "role": "user",
                "content": text,
            },
        ],
        text={
            "format": {
                "type": "json_schema",
                "name": "project_state",
                "schema": PROJECT_SCHEMA,
                "strict": True,
            }
        },
    )

    return json.loads(response.output_text)
