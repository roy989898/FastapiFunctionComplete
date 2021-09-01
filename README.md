# Missing part

~~templete~~  
~~auth~~  
~~mulit router file~~  
~~i18n in templete~~
~~csrf~~  
~~validation i18n~~  
~~Error handle~~  
validation error handle
~~logging~~  
email

# Finish Part

### templete

```python
from global_var import templates


@app.get("/")
async def root(request: Request):
    result = {}
    result.update({"request": request})
    return templates.TemplateResponse("index.html", result)
```

### i18n in templete

```html
{{ 'Hello'  |tran('tc') }}
```

### Auth

```python
# Get he Token
@app.post("/token", response_model=schemas.Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


# Get Current user
@app.get("/users/me/", response_model=schemas.User)
async def read_users_me(current_user: models.User = Depends(get_current_active_user)):
    return current_user
```

### csrf

```python
@router.get('/signup', name='task_signup')
def signup(request: Request, csrf_protect: CsrfProtect = Depends()):
    csrf_token = csrf_protect.generate_csrf()
    # result = get_link_variable(request)
    result = {}
    result.update({'csrf_token': csrf_token})
    return templates.TemplateResponse("signup.html", result)


@router.post('/signup', name='task_signup_post')
async def signup(csrf_token: str = Form(None), csrf_protect: CsrfProtect = Depends(), db: Session = Depends(get_db)
                 ):
    csrf_protect.validate_csrf(csrf_token)
```

### validation i18n

```python

errors: List[Dict[str, Any]] = []
try:
    schemas.SignupForm(
        username=username,
        full_name=full_name,
        isEmailUnique=is_email_unique,
        email=email,
        password=password,
        password2=password2)
except ValidationError as e:
    #  tc ,use what to determine the lang???
    errors = tr.translate(e.errors(), locale="tc")

form_error = get_errors_msgs(errors)


```

### logging

https://github.com/Delgan/loguru#x-faster-than-built-in-logging

log level DEBUG < INFO < WARNING < ERROR / EXCEPTION < CRITICAL   
setup

```python
log_set_up.setup()
# default is log error,rotation at 00:00
```

usage

```python
logger.debug('App start')

```

for exception

```python
logger.add("out.log", backtrace=True, diagnose=True)  # Caution, may leak sensitive data in prod


def func(a, b):
    return a / b


def nested(c):
    try:
        func(5, c)
    except ZeroDivisionError:
        logger.exception("What?!")


nested(0)

```

Would result in:

```
2018-07-17 01:38:43.975 | ERROR    | __main__:nested:10 - What?!
Traceback (most recent call last):

  File "test.py", line 12, in <module>
    nested(0)
    └ <function nested at 0x7f5c755322f0>

> File "test.py", line 8, in nested
    func(5, c)
    │       └ 0
    └ <function func at 0x7f5c79fc2e18>

  File "test.py", line 4, in func
    return a / b
           │   └ 0
           └ 5

ZeroDivisionError: division by zero
```

### Error handle

```python
# catch
@app.exception_handler(MyException)
async def http_exception_handler(request, exc):
    return PlainTextResponse(str('My exception'), status_code=404)


# raise Errro
raise MyException(name='www')


# not catch error
# in main
async def catch_exceptions_middleware(request: Request, call_next):
    try:
        return await call_next(request)
    except Exception:
        # you probably want some kind of logging here
        logger.exception("Global")
        return Response("Internal server error", status_code=500)

```

### validation error handle