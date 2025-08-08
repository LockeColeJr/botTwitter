import os
from google import genai
from google.genai import types
import json

def generate_post(prompt):
    try:
        with open("keys.json", "r") as f:
            keys = json.load(f)
        client = genai.Client(
            api_key=keys["gemini"],
        )

        model = "gemini-2.0-flash"
        contents = [
            types.Content(
                role="user",
                parts=[
                    types.Part.from_text(text=prompt),
                ],
            ),
        ]
        generate_content_config = types.GenerateContentConfig(
            temperature=1.4,
        )

        response = ""
        for chunk in client.models.generate_content_stream(
            model=model,
            contents=contents,
            config=generate_content_config,
        ):
            response += chunk.text
        return response.strip()
    except:
        return "Não foi possível gerar."