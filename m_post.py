import json
import requests
from requests_oauthlib import OAuth1

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

        media_id = None
        if watermark:
            with open("binance.png", "rb") as image:
                files = {"media": image}
                upload_url = "https://upload.twitter.com/1.1/media/upload.json"
                r = requests.post(upload_url, auth=auth, files=files)
                if r.status_code == 200:
                    media_id = r.json().get("media_id_string")

        url = "https://api.twitter.com/2/tweets"
        payload = {"text": post}
        if media_id:
            payload["media"] = {"media_ids": [media_id]}

        response = requests.post(url, auth=auth, json=payload)
        return response.status_code, response.text
    except:
        return "Erro."
