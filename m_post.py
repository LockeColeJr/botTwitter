import json
import requests
from requests_oauthlib import OAuth1
import os

def post_tweet(post, watermark=False):
    try:
        with open("keys.json", "r") as f:
            keys = json.load(f)

        auth = OAuth1(
            keys["x-api-key"],
            keys["x-api-secret"],
            keys["x-access-token"],
            keys["x-access-secret"]
        )

        url = "https://api.twitter.com/2/tweets"

        payload = {
            "text": post
        }

        response = requests.post(url, auth=auth, json=payload)

        if watermark:
            files = {'media' : open('binance.png', 'rb')}
            requests.post(url, auth=auth, files = files)

        return response.status_code, response.text
    except:
        return "Erro."
