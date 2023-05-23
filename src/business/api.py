import requests

from typing import Dict, Any

def request_info_hero(id: int) -> Dict[str, Any]:
    return requests.get(
        f"https://superheroapi.com/api/2183127771827858/{id}"
    ).json()


def send_simple_message(text_content: str):
	return requests.post(
		"https://api.mailgun.net/v3/sandboxc41ef0611f20406598463646bb428f6b.mailgun.org/messages",
		auth=("api", "0440724274eaebdfa3714d80aeb12dc0-07ec2ba2-05c9710b"),
		data={"from": "mailgun@sandboxc41ef0611f20406598463646bb428f6b.mailgun.org",
			"to": ["imceballos@uc.cl"],
			"subject": "Hero Battle simulator",
			"text": text_content})