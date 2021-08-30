from typing import List, Dict, Any

from fastapi import APIRouter, Depends, Form
from pydantic import ValidationError
from requests import Response
from sqlalchemy.orm import Session

import models
import schemas
from fastapi_csrf_protect import CsrfProtect
from starlette.requests import Request

from global_var import templates
from utils.auth import auth
from utils.db.database import get_db
from utils.form.form_util import get_errors_msgs
from utils.i18n.language import tr

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
    result.update({'task_signup_post': request.url_for('task_signup_post')})
    return templates.TemplateResponse("signup.html", result)


@router.post('/signup',
             # responses={404: {'model': task_system_schemas.FormError}}
             name='task_signup_post'

             )
async def signup(response: Response, request: Request, email: str = Form(None), password: str = Form(None),
                 password2: str = Form(None),
                 csrf_token: str = Form(None), csrf_protect: CsrfProtect = Depends(), db: Session = Depends(get_db)):
    csrf_protect.validate_csrf(csrf_token)
    #  validate the form
    errors: List[Dict[str, Any]] = []
    #  check is the email unique

    users: List[models.User] = db.query(models.User).filter(models.User.email == email)
    # TODO check
    emails = await task_system_model.User.filter(email=email)
    is_email_unique = True
    if len(emails) > 0:
        is_email_unique = False

    try:
        # TODO miss scheme
        schemas.SignupForm(isEmailUnique=is_email_unique, email=email, password=password,
                           password2=password2)
    except ValidationError as e:
        #  tc ,use what to determine the lang???
        errors = tr.translate(e.errors(), locale="tc")
        # errors = e.errors()

    if len(errors) == 0:
        #  if no error ,create user with bcrypt
        # TODO create user
        user = task_system_model.User(email=email, password=password_util.get_password_hash(password))
        await user.save()
    #     TODO redirect to?

    form_error = get_errors_msgs(errors)
    # result = get_link_variable(request)
    result = {}
    result.update({"request": request})
    result.update({'csrf_token': csrf_token})
    result.update({'form_error': form_error})
    result.update({'task_signup_post': request.url_for('task_signup_post')})
    return templates.TemplateResponse("SimpleTaskSystem/signup.html", result)
