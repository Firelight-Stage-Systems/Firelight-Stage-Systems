from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, FileResponse, HTMLResponse

from HTMLSide import MainHTML
from APIExternal import ExternalAPI
from APIInternal import InternalAPI
from dependencies import templates, Data

app = FastAPI()
app.include_router(MainHTML.router)
app.include_router(ExternalAPI.router)
app.include_router(InternalAPI.router)

@app.get('/Empty', response_class=HTMLResponse)
def Empty() -> HTMLResponse:
    return '<!DOCTYPE html><html style="height:0;"><head><title>Nothing has been returned yet</title></head></html>'

@app.get('/favicon.ico')
async def favicon():
    return FileResponse('static/favicon.ico')