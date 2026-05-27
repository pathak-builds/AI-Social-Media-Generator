"""
Combines prompt engineering and LLM generation.
"""

from utils.prompt_builder import build_prompt
from utils.ollama_client import generate_response


def generate_content(topic, platform, tone, length, model):

    prompt = build_prompt(
        topic=topic,
        platform=platform,
        tone=tone,
        length=length
    )

    result = generate_response(
        prompt=prompt,
        model=model
    )

    return result

