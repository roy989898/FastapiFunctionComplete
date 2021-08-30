from fastapi import APIRouter
from starlette.requests import Request

from global_var import templates

router = APIRouter()


@router.get("/")
async def root(request: Request):
    result = {}
    result.update({"request": request})
    return templates.TemplateResponse("index.html", result)
