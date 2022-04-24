from fastapi import APIRouter, Request
from fastapi.responses import FileResponse
import queue

from dependencies import templates, Show

router = APIRouter(responses={404: {'description': 'Not found'}}, 
                   tags=['Application Interface: Internal'],
                   prefix='/InternalAPI')

# Create Event Systems

