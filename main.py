from datetime import timedelta

from fastapi import FastAPI, Depends, HTTPException
import uvicorn
from fastapi.security import OAuth2PasswordRequestForm
from starlette import status
from starlette.requests import Request

from global_var import templates
from utils.auth.auth import Token, fake_users_db, authenticate_user, ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token, \
    User, get_current_active_user
from utils.db.database import Base, engine
from utils.i18n.language import languages
import models

Base.metadata.create_all(bind=engine)
app = FastAPI()


# register filter
def tran(value, lang='en'):
    return languages[lang][value]


templates.env.filters["tran"] = tran


@app.get("/")
async def root(request: Request):
    result = {}
    result.update({"request": request})
    return templates.TemplateResponse("index.html", result)


@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/users/me/", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user


@app.get("/users/me/items/")
async def read_own_items(current_user: User = Depends(get_current_active_user)):
    return [{"item_id": "Foo", "owner": current_user.username}]


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
