from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


router = APIRouter()

templates = Jinja2Templates(directory=BASE_DIR/'templates')

@router.get("/", response_class=HTMLResponse)
async def index(request:Request):
    context={
        'request':request,
        'message':'Добро Пожаловать!'
        }

    return templates.TemplateResponse(
        request=request,
        name='index.html', 
        context=context
    )


