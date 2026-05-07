from fastapi import APIRouter, Form, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from app.schemas.contact import dictionary, contact_list

router = APIRouter()
templates = Jinja2Templates(directory='templates')


@router.post('/submit/add', response_class=HTMLResponse)
async def create_contact(
    request:Request,
    name: str=Form(),
    age: int=Form(),
    phone: str=Form()
):
    for c in contact_list:
        if c.phone == phone:
            raise HTTPException(status_code=400, detail="Контакт уже существует")
        
    contact_list.append(dictionary(name=name, age=age, phone=phone))

    context = {
        'request':request,
        'contacts': contact_list

    }

    return templates.TemplateResponse(
        request=request,
        name='contacts/contacts.html',
        context=context

    )

