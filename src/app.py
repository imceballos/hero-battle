from fastapi import FastAPI, Request, Form, File, UploadFile, Depends, HTTPException, status
from starlette.responses import RedirectResponse

from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import List, Dict
import os

from models.model import Battle

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
    hero_data = battle.info
    activity = battle.activity
    print(activity)
    return templates.TemplateResponse("index.html", {"request": request, "hero_data": hero_data, "activity": activity})