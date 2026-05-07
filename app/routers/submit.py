from fastapi import APIRouter, Form, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from app.schemas.contact import dictionary, contact_list
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


router = APIRouter()

templates = Jinja2Templates(directory=BASE_DIR/'templates')

@router.get('/add/')
async def add_contact(request:Request):
    context = {'request':request,
               'contacts': contact_list
               }

    return templates.TemplateResponse(
        request=request,
        name='contacts/contacts.html',
        context=context
    )