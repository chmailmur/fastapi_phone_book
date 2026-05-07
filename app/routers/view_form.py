from fastapi import APIRouter, Form, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from schemas.contact import dictionary, contact_list

router = APIRouter()
templates = Jinja2Templates(directory='templates')

@router.get('/', response_class=HTMLResponse)
async def show_form(request: Request):
    context={
        'request':request,
        'message':'Добавиь контакт'
    }

    return templates.TemplateResponse(
        request=request,
        name='contact_manager/manager.html',
        context=context
    )


@router.post('/')
async def create_contact(
    name: str=Form(),
    age: int=Form(),
    phone: str=Form()
):
    for c in contact_list:
        if c.phone == phone:
            raise HTTPException(status_code=400, detail="Контакт уже существует")
        
    contact_list.append(dictionary(name=name, age=age, phone=phone))

