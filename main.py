from fastapi import FastAPI
from typing import Annotated


def get(txt:str):
    return {"result":txt}

def post (txt:Annotated[str,Form(...)]):
    return {"result":txt}



