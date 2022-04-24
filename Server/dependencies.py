from fastapi.templating import Jinja2Templates
from fastapi import Request
import json


class Info():
    def __init__(self) -> None:
        self.CONFIGDIR = 'data/config.json'
        self.SYSTEMVARIABLESDIR = 'data/systemVariables.json'
    
    @staticmethod
    def getConfig(ConfigDir:str) -> dict:
        with open(ConfigDir, 'r') as data:
            config:dict = json.load(data)
        return config

Data = Info()
templates = Jinja2Templates(directory='template')

def https_url_for(request:Request, funcName, **fileName) -> str:
    http_url = request.url_for(funcName, **fileName)

    # Replace 'http' with 'https'
    if Data.getConfig(Data.CONFIGDIR)['Developer']['https']:
        return http_url.replace("http", "https", 1)
    else:
        return http_url

templates.env.globals["https_url_for"] = https_url_for