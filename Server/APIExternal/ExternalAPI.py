from fastapi import APIRouter, Request
from fastapi.responses import FileResponse, JSONResponse

from dependencies import templates, Show, ShowState

router = APIRouter(responses={404: {'description': 'Not found'}}, 
                   tags=['Application Interface: External'],
                   prefix='/ExternalAPI')

@router.get('/static/{fileName}', response_class=FileResponse)
def static(request:Request, fileName:str) -> FileResponse:
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

@router.get('/SMPTETimeStamp', response_class=JSONResponse)
def SMPTETimeStamp() -> dict:
    return {"SMPTE":Show.SMPTE}

@router.get('/StartStopShow', response_class=JSONResponse)
def StartStopShow():
    return Show.ShowState

@router.post('/StartStopShow')
def StartStopShow(ShowAPI:ShowState):
    Show.ShowState = ShowAPI