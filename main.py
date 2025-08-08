import m_generatePost
import m_post
import re
import time
import random
import server

server.keep_alive()

def should_retry(post):
    if not post:
        return True
    post_lower = post.lower()
    return "sorry" in post_lower or "i can't" in post_lower

def post_flow():
    prompt = "Generate a short, impactful tweet with emojis about Binance code FIBP84UZ, encouraging people to use it. Include at least 3 relevant hashtags. Do not use markdown or bold formatting."
    post = m_generatePost.generate_post(prompt)

    if should_retry(post):
        return

    if post and post != "Erro ao gerar.":
        post = re.sub(r'\*\*|__', '', post)
        status_code, response_text = m_post.post_tweet(post, watermark=True)
        if status_code == 201:
            print(post)
        elif status_code == 429:
            print("Muitas requisições.")
        else:
            print(response_text)
    else:
        print(post)

while True:
    post_flow()
    sleep_time = random.randint(1800, 7200)
    time.sleep(sleep_time)