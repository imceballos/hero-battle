import requests

from typing import Dict, Any

def request_info_hero(id: int) -> Dict[str, Any]:
    return requests.get(
        f"https://superheroapi.com/api/2183127771827858/{id}"
    ).json()