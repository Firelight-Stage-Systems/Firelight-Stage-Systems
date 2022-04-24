from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from dependencies import templates

router = APIRouter(responses={404: {'description': 'Not found'}}, tags=['HTML'])

@router.get('/', response_class=HTMLResponse)
async def home(request:Request) -> HTMLResponse:
    return templates.TemplateResponse('home.html', {'request':request})