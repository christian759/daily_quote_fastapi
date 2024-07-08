from fastapi import FastAPI, Request, BackgroundTasks
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from bs4 import BeautifulSoup
import requests

app = FastAPI()

app.mount('/static', StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

def write_notification():
    url_link = "https://www.inspiringquotes.com/"
    result = requests.get(url_link).text
    doc = BeautifulSoup(result, "html.parser")
    quotes = doc.select(".IQDailyInspiration__quote")[0]
    quote = quotes.text
    author = doc.select(".IQDailyInspiration__author")[0]
    author = author.text
    date = doc.select(".IQDailyInspiration__date")[0]
    date = date.text
    new_list = [quote, author, date]
    return new_list

@app.get("/", response_class=HTMLResponse)
async def home(request: Request, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_notification, )
    return templates.TemplateResponse(name = "index.html",
                                      request=request,
                                      context={"quote": write_notification()[0], "author": write_notification()[1], "date": write_notification()[2]})


