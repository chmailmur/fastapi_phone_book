import uvicorn
from fastapi import FastAPI
from app.routers.hello import router as hello_router
from app.routers.about import router as about_router
from app.routers.contacts import router as contacts_router
from app.routers.view_form import router as view_form_router 
from app.routers.manager import router as manager_router 



app = FastAPI()

app.include_router(hello_router, tags=['API Hello'])

app.include_router(about_router, tags=['API About'], prefix='/about')

app.include_router(contacts_router, tags=['API Contacts'], prefix='/contacts')

app.include_router(view_form_router, tags=['API form'], prefix='/view_form')

app.include_router(manager_router, tags=['API Contact manager'], prefix='/manager')
