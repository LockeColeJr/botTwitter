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
                    types.Part.from_text(text="""Generate a short, impactful tweet with emojis about Binance code FIBP84UZ, encouraging people to use it. Include at least 3 relevant hashtags. Do not use markdown or bold formatting. Use meaningful hashtags and always use #Binance."""),
                ],
            ),
            types.Content(
                role="model",
                parts=[
                    types.Part.from_text(text="""Unlock crypto rewards on Binance! 💰 Use code FIBP84UZ when signing up and start your trading journey today!🚀 Don't miss out! 😉 #BinanceReferral #CryptoDeals #Binance
"""),
                ],
            ),
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
        return "Erro ao gerar."