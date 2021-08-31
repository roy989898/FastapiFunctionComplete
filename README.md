# Missing part

~~templete~~  
~~auth~~  
~~mulit router file~~  
~~i18n in templete~~
~~csrf~~  
~~validation i18n~~  
Error handle  
logging  
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
https://shian420.pixnet.net/blog/post/350291572-%5Bpython%5D-logging-%E5%B9%AB%E4%BD%A0%E7%B4%80%E9%8C%84%E4%BB%BB%E4%BD%95%E8%A8%8A%E6%81%AF
