from fastapi import APIRouter, Depends
from fastapi_csrf_protect import CsrfProtect
from starlette.requests import Request

from global_var import templates

router = APIRouter()


@router.get("/")
async def root(request: Request):
    result = {}
    result.update({"request": request})
    return templates.TemplateResponse("index.html", result)


@router.get('/signup', name='task_signup')
def signup(request: Request, csrf_protect: CsrfProtect = Depends()):
    csrf_token = csrf_protect.generate_csrf()
    # result = get_link_variable(request)
    result = {}
    result.update({"request": request})
    result.update({'csrf_token': csrf_token})
    # result.update({'task_signup_post': request.url_for('task_signup_post')})
    return templates.TemplateResponse("signup.html", result)
