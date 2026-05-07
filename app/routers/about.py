from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


router = APIRouter()

templates = Jinja2Templates(directory=BASE_DIR/'templates')


@router.get("/")
async def about(request:Request):
    context = {
        'request':request,
        'message': "Информация о приложении"
        }

    return templates.TemplateResponse(
        request=request,
        name='about/about.html',
        context=context
    )