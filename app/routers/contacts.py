from fastapi import APIRouter, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from app.schemas.contact import dictionary, contact_list
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


router = APIRouter()

templates = Jinja2Templates(directory=BASE_DIR/'templates')

@router.get("/", response_class=HTMLResponse)
async def get_contacts(request:Request):
    context = {'request':request,
               'contacts': contact_list
               }
    return templates.TemplateResponse(
        request=request,
        name='contacts/contacts.html',
        context=context
    )

@router.get("/{phone}", response_class=HTMLResponse, name='contact_page_html')
async def get_contact(request:Request, phone:str):
    context = {'request':request,
               'contacts': [contact if contact.phone == phone else None for contact in  contact_list]
               }
    
    return templates.TemplateResponse(
        request=request,
        name='contacts/contact_page.html',
        context=context
    )
    

@router.post('/', response_model=dictionary)
async def add_contact(contact:dictionary):
    for c in contact_list:
        if c.name == contact.name:
            raise HTTPException()
    
    contact_list.append(contact)
    return contact