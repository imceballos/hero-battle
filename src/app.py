from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import List, Dict
import base64
import json
import os

from models.model import Battle
from models.schema import File
from business.utils import format_message
from business.api import  send_simple_message




app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/")
def index(request: Request):
    """
    gets the list of files from the directory, creates a list of dictionaries with the name and size fields, and returns an HTML response
    with the generated file list
    """
    battle = Battle()
    battle.start_battle()
    hero_data, activity = battle.info, battle.activity
    json_string = json.dumps(activity)
    encoded_activity = base64.b64encode(json_string.encode('utf-8')).decode('utf-8')
    return templates.TemplateResponse("index.html", {"request": request, "hero_data": hero_data, "activity": activity, "encoded_activity": encoded_activity})

@app.post("/send_email")
def send_email(content: List[File]):
    """
    gets the list of files from the directory, creates a list of dictionaries with the name and size fields, and returns an HTML response
    with the generated file list"""
    decoded_data = base64.b64decode(content[0].activity).decode('utf-8')
    formatted_message = json.loads(decoded_data)
    recent_activity = [format_message(act) for act in formatted_message]
    content_message = " \n".join(recent_activity)
    print(content_message)
    try:
        email = send_simple_message(content_message)
        return {"message": f"Successfully sent"}
    except Exception as e:
        print(e)
        return {"error": str(e)}