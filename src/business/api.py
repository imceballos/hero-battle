from dotenv import load_dotenv
import requests
import os

from typing import Dict, Any

load_dotenv()

def request_info_hero(id: int) -> Dict[str, Any]:
    return requests.get(
        f"https://superheroapi.com/api/2183127771827858/{id}"
    ).json()


def send_simple_message(text_content: str):
	return requests.post(
		os.getenv("URL"),
		auth=("api", os.getenv("AUTH")),
		data={"from": os.getenv("DATA"),
			"to": ["imceballos@uc.cl"],
			"subject": "Hero Battle simulator",
			"text": text_content})