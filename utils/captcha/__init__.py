import os
import requests
from dotenv import load_dotenv

load_dotenv()


def verify_hcaptcha(captcha_response, remote_addr):
    if not captcha_response:
        return False

    secret_key = os.environ.get("HCAPTCHA_SECRET_KEY")
    data = {
        "secret": secret_key,
        "response": captcha_response,
        "remoteip": remote_addr,
    }
    response = requests.post("https://hcaptcha.com/siteverify", data=data)
    result = response.json()

    return result.get("success", False)
