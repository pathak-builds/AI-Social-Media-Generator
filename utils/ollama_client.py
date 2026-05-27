"""
Handles communication with Ollama.
"""

import ollama


def generate_response(prompt, model="llama3.2"):

    response = ollama.chat(
        model=model,
        messages=[
            {
                "role": "system",
                "content": "You are an expert social media marketing assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]

