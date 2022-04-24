from fastapi import APIRouter, Request
from fastapi.responses import FileResponse

from dependencies import templates

router = APIRouter(responses={404: {'description': 'Not found'}}, 
                   tags=['Application Interface'],
                   prefix='/api')

@router.get('/static/{fileName}', response_class=FileResponse)
async def static(request:Request, fileName:str) -> FileResponse:
    decomposedFileName = fileName.split('.')
    headers={'content-type':'text/plain'}
    if len(decomposedFileName) > 1:
        if decomposedFileName[1] == 'js':
            headers={'content-type':'application/javascript'}
        elif decomposedFileName[1] =='css':
            headers={'content-type':'text/css'}
        elif decomposedFileName[1] =='html':
            headers={'content-type':'text/html'}
    return FileResponse(f'static/{fileName}', headers=headers)