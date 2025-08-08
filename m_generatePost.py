import os
import json
from openai import OpenAI

def generate_post(prompt):
    try:
        with open("keys.json", "r") as f:
            keys = json.load(f)

        client = OpenAI(
            base_url="https://router.huggingface.co/v1",
            api_key=keys["huggingface"],
        )

        completion = client.chat.completions.create(
            model="openai/gpt-oss-20b:novita",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
        )

        return completion.choices[0].message.content
    except:
        return "Erro ao gerar."